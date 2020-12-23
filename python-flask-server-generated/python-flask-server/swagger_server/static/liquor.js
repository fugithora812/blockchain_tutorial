"use strict";

// TOP画面に新着のお酒を表示する
function getNewLiquors() {
  const url_get    = 'http://localhost:8080/api/v1/liquors'

  fetch(url_get).then(function (liquors) {
    // 読み込むデータをJSONに設定
    return liquors.json();
  }).then(function (json) {
    // データ読み出し、表示
    // let displayQuantity = 3;
    // for (let i = 0; i < displayQuantity; i++) {
    //   let newLiquor = json[i].liquorName;
    //   let arriveDateString = json[i].arrivalDay;

    //   let displayLiquor = document.getElementById("newArrive");
    //   displayLiquor.innerHTML = `<a href="javascript:void(0);" onclick="fade();">${newLiquor} 入荷日：${arriveDateString}</a>`
    // }

    let displayQuantity = 3;
    let htmlArray = [];
    for (let i = 0; i < displayQuantity; i++) {
      let displayLiquor = document.getElementById("liquors");
      htmlArray[i] = `<a href="javascript:void(0);" id="liquor${i}" onclick="fade(${i});">${json[i]}</a><br>`;
      displayLiquor.innerHTML += htmlArray[i]
    }

  });

  // let displayLiquor = document.getElementById("newArrive");
  // displayLiquor.innerHTML = "<p>hello</p>";
}

// 人気のお酒を表示する
function getPopularLiquor() {
  fetch(url_get).then(function (liquors) {
    // 読み込むデータをJSONに設定
    return liquors.json();
  }).then(function (json) {
    // データ読み出し、表示

  });
}

// 在庫の検索・表示
function searchLiquor() {
  let liquorObj = document.getElementById("wantThis");
  let liquorName = liquorObj.value;
  console.log(liquorName);

  const url_search = `http://localhost:8080/api/v1/liquors/search?liquorName=${liquorName}`;

  fetch(url_search).then(function (liquors) {
    // 読み込むデータをJSONに設定
    console.log(liquors);
    return liquors.json();
  }).then(function (json) {

    let liquorName = "";
    for (let i = 0; i < json.length; i++) {
      liquorName += json[i];
    }

    let resultLiquor = document.getElementById("searchResult");
    resultLiquor.innerHTML = `<div id="resultDiv">SEARCH RESULT<br><a href="javascript:void(0);" id="result" onclick="fadeResult();"></a></div>`;

    let liquor = document.getElementById("result");
    liquor.innerHTML += `${liquorName}`;

  });
}

// 在庫の取り置き
function reserveLiquor(liquorName) {
  const url_reserve = `http://localhost:8080/api/v1/liquors/reserve?liquorName=${liquorName}`

  fetch(url_reserve).then(function (liquors) {
    // 読み込むデータをJSONに設定
    return liquors.text();
  }).then(function (bool) {
    // 処理結果の表示
    let reserveResult = document.getElementById("reservation");
    if (bool[0] == "t") {
      reserveResult.innerHTML = `<p>SUCCESS</p>\
                                  <p>取り置き成功しました</p> \
                                  <input type="button" id="noReserve" value="確認" onclick="backTop()">`;
    } else {
      reserveResult.innerHTML = `<p>FAILED...</p>\
                                  <p>取り置き失敗しました</p> \
                                  <input type="button" id="yesReserve" value="再試行" onclick="reserveLiquor('${liquorName}')">\
                                  <input type="button" id="noReserve" value="キャンセル" onclick="backTop()">`;
    }
  });
}

// 画面をフェードして取り置きダイアログを表示
// NEW ARRIVE用
function fade(liquorNumber) {
  let reservation = document.getElementById("fadeLayer");
  reservation.style.visibility = "visible";

  let liquorName = document.getElementById(`liquor${liquorNumber}`).innerHTML;

  reservation.innerHTML = `<div id="block"><div id="reservation"> \
                        <p> RESERVATION: ${liquorName}</p> \
                        <p>取り置き依頼しますか？<p>\
                        <input type="button" id="yesReserve" value="はい" onclick="reserveLiquor('${liquorName}')">\
                        <input type="button" id="noReserve" value="いいえ" onclick="backTop()"></div ></div > `;
}

// SEARCH RESULT用
function fadeResult() {
  let reservation = document.getElementById("fadeLayer");
  reservation.style.visibility = "visible";

  let liquorName = document.getElementById(`result`).innerHTML;

  reservation.innerHTML = `<div id="block"><div id="reservation"> \
                        <p> RESERVATION: ${liquorName}</p> \
                        <p>取り置き依頼しますか？<p>\
                        <input type="button" id="yesReserve" value="はい" onclick="reserveLiquor('${liquorName}')">\
                        <input type="button" id="noReserve" value="いいえ" onclick="backTop()"></div ></div > `;
}

// 取り置き依頼をキャンセルした際、トップ画面に戻す
function backTop() {
  let makeInvisible = document.getElementById("fadeLayer");
  makeInvisible.style.visibility = "hidden";
}


window.onload = getNewLiquors;
