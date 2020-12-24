"use strict";

// TOP画面に新着のお酒を表示する
function getNewLiquors() {
  const url_get    = 'http://localhost:8080/api/v1/liquors'

  fetch(url_get).then(function (liquors) {
    // 読み込むデータをJSONに設定
    return liquors.json();
  }).then(function (json) {
    // ToDo: ver2.0.0 全種類データ読み出し・表示
    // let displayQuantity = 3;
    // for (let i = 0; i < displayQuantity; i++) {
    //   let newLiquor = json[i].liquorName;
    //   let arriveDateString = json[i].arrivalDay;

    //   let displayLiquor = document.getElementById("newArrive");
    //   displayLiquor.innerHTML = `<a href="javascript:void(0);" onclick="fade();">${newLiquor} 入荷日：${arriveDateString}</a>`
    // }

    // ver1.0.0 商品名のみ表示
    let displayQuantity = 3;
    let htmlArray = [];
    for (let i = 0; i < displayQuantity; i++) {
      let displayLiquor = document.getElementById("liquors");
      htmlArray[i] = `<a href="javascript:void(0);" id="liquor${i}" onclick="fade(${i});">${json[i]}</a><br>`;
      displayLiquor.innerHTML += htmlArray[i]
    }
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

    if (liquorName == "") {
      let notFound = document.getElementById("resultDiv");
      notFound.innerHTML = '<p>NOT FOUND<p>該当する商品がありません';
    } else {
      liquor.innerHTML += `${liquorName}`;
    }

  });
}

// 在庫の取り置き処理を実行する
function reserveLiquor(liquorName) {
  const url_reserve = `http://localhost:8080/api/v1/liquors/reserve?liquorName=${liquorName}`

  fetch(url_reserve).then(function (liquors) {
    // Promiseオブジェクトを1文字ずつテキスト化
    return liquors.text();
  }).then(function (booltxt) {
    // 処理結果の表示
    let reserveResult = document.getElementById("reservation");
    if (booltxt[0] == "t") {
      // swal("SUCCESS", "取り置き成功しました", "success")
      reserveResult.innerHTML = `<p id="popTitle">SUCCESS</p>\
                              <p>取り置き成功しました</p> \
                              <input type="button" id="reserveSuccess" value="OK" onclick="backTop()">`;
    } else {
      reserveResult.innerHTML = `<p id="popTitle">SORRY...</p>\
                                  <p>取り置き失敗しました</p> \
                                  <input type="button" id="yesReserve" value="Retry" onclick="reserveLiquor('${liquorName}')">\
                                  <input type="button" id="noReserve" value="Cancel" onclick="reserveCancel()">`;
    }
  });

}

// 取り置きキャンセルのポップアップ表示しTOP画面に戻す
function reserveCancel() {
  let reserveCancel = document.getElementById("reservation");
  reserveCancel.innerHTML = '<p id="popTitle">CANCELED</p>\
                              <p>取り置きをキャンセルしました</p>\
                              <input type="button" id="noReserve" value="OK" onclick="backTop()">';
}

// 画面をフェードして取り置きダイアログを表示する -NEW ARRIVE用
function fade(liquorNumber) {
  let reservation = document.getElementById("fadeLayer");
  reservation.style.visibility = "visible";

  let liquorName = document.getElementById(`liquor${liquorNumber}`).innerHTML;

  reservation.innerHTML = `<div id="block"><div id="reservation"> \
                        <p id="popTitle"> RESERVATION: ${liquorName}</p> \
                        <p>取り置き依頼しますか？<p>\
                        <input type="button" id="yesReserve" value="YES" onclick="reserveLiquor('${liquorName}')">\
                        <input type="button" id="noReserve" value="NO" onclick="reserveCancel()"></div ></div > `;
}

// 画面をフェードして取り置きダイアログを表示する -SEARCH RESULT用
function fadeResult() {
  let reservation = document.getElementById("fadeLayer");
  reservation.style.visibility = "visible";

  let liquorName = document.getElementById(`result`).innerHTML;

  reservation.innerHTML = `<div id="block"><div id="reservation"> \
                        <p> RESERVATION: ${liquorName}</p> \
                        <p>取り置き依頼しますか？<p>\
                        <input type="button" id="yesReserve" value="YES" onclick="reserveLiquor('${liquorName}')">\
                        <input type="button" id="noReserve" value="NO" onclick="reserveCancel()"></div ></div > `;
}

// フェードを消してトップ画面に戻す
function backTop() {
  let makeInvisible = document.getElementById("fadeLayer");
  makeInvisible.style.visibility = "hidden";
}


// 画面ロード時に商品を表示
window.onload = getNewLiquors;
