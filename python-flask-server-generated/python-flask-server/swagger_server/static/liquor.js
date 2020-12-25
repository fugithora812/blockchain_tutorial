"use strict";

// TOP画面に新しいお酒を数点表示する
function getNewLiquors() {
  const url_get = 'http://localhost:8080/api/v1/liquors'

  fetch(url_get).then(function (liquors) {
    // 読み込むデータをJSONに設定
    return liquors.json();
  }).then(function (json) {
    // ver1.1.0 全種類データ読み出し・表示
    let htmlArray = [];
    let displayQuantity = json.length;

    // 重複判定用の配列tempLiquors
    let tempLiquors = [];

    let displayLiquor = document.getElementById("newArrive");
    for (let i = 0; i < displayQuantity; i++) {
      let newLiquor = json[i].liquorName;

      // 商品名の重複を排除
      if (!(tempLiquors.includes(newLiquor))) {
        tempLiquors.push(newLiquor);

        htmlArray[i] = `<li><a href="javascript:void(0);" onclick="fade(${i});" id="liquor${i}">${newLiquor}</a></li><br>`
        displayLiquor.innerHTML += htmlArray[i];
      }
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
    return liquors.json();
  }).then(function (json) {

    let liquorName = "";
    let sellerName = "";
    for (let i = 0; i < json.length; i++) {
      liquorName = json[i].liquorName;
      sellerName = json[i].sellerName;
    }

    let resultLiquor = document.getElementById("searchResult");
    resultLiquor.innerHTML = `<div id="resultDiv"><p id="popTitle">SEARCH RESULT</p><a href="javascript:void(0);" id="result" onclick="fadeResult();"></a></div>`;

    let liquor = document.getElementById("result");
    let notFound = document.getElementById("resultDiv");
    if (liquorName == "") {

      notFound.innerHTML = '<p id="popTitle">NOT FOUND</p>該当する商品がありません';
    } else {
      liquor.innerHTML += `${liquorName}`;
      notFound.innerHTML += `(取扱店：${sellerName})`
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
                                  <input type="button" id="noReserve" value="Cancel" onclick="backTop()">`;
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

// 登録店舗を表示
function getSellers() {
  const url_get = 'http://localhost:8080/api/v1/liquors'

  fetch(url_get).then(function (liquors) {
    // 読み込むデータをJSONに設定
    return liquors.json();
  }).then(function (json) {
    // ver1.1.0 全種類データ読み出し・表示
    let htmlArray = [];
    let displayQuantity = json.length;

    // 重複判定用の配列sellers
    let sellers = [];

    let displayLiquor = document.getElementById("popularSeller");
    for (let i = 0; i < displayQuantity; i++) {
      let sellerName = json[i].sellerName;

      // 店舗の重複を排除
      if (!(sellers.includes(sellerName))) {
        sellers.push(sellerName);

        htmlArray[i] = `<li><a href="javascript:void(0);" onclick="sellerLiquor('${sellerName}');" id="liquor${i}">${sellerName}</a></li><br>`
        displayLiquor.innerHTML += htmlArray[i];
      }
    }
  });
}

// 同一取扱店舗の商品を一括表示
function sellerLiquor(clickedSeller) {
  // フェード処理
  let sellerLiquor = document.getElementById("fadeLayer");
  sellerLiquor.style.visibility = "visible";
  sellerLiquor.innerHTML = `<div id='block'><div id='toDisplayLiquor'><p id="popTitle">SELLER: ${clickedSeller}</p></div></div>`;

  const url_get = 'http://localhost:8080/api/v1/liquors'

  fetch(url_get).then(function (liquors) {
    // 読み込むデータをJSONに設定
    return liquors.json();
  }).then(function (json) {
    // ver1.1.0 全種類データ読み出し・表示
    let htmlArray = [];
    let displayQuantity = json.length;

    let displayLiquor = document.getElementById("toDisplayLiquor");
    for (let i = 0; i < displayQuantity; i++) {
      let sellerName = json[i].sellerName;

      if (sellerName == clickedSeller) {
        let newLiquor = json[i].liquorName;

        htmlArray[i] = `<li><a href="javascript:void(0);" onclick="fade(${i});" id="liquor${i}">${newLiquor}</a></li><br>`
        displayLiquor.innerHTML += htmlArray[i];
      }
    }
    displayLiquor.innerHTML += `<input type="button" id="backTop" value="TOP" onclick="backTop()">`
  });
}


// 画面ロード時に商品, 登録店舗を表示
window.addEventListener("load", getNewLiquors);
window.addEventListener("load", getSellers);
