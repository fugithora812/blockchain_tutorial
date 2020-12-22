"use strict";

const url_get    = 'http://localhost:8080/api/v1/liquors'

// ヘッダを追加する
// function setHeader(req, res, next) {
//   res.setHeader('Access-Control-Allow-Origin', '*');
//   next();
// }

// module.exports = {
//   server: {
//     middleware: {
//       0: setHeader
//     }
//   }
// }

// 新しく入荷されたお酒を表示する
function getNewLiquors() {
  fetch(url_get, {
    method: "GET",
    mode: "cors",
    headers: {
      "Access-Control-Allow-Method": "GET"
    }
  }).then(function (liquors) {
    // 読み込むデータをJSONに設定
    console.log(liquors);
    return liquors.text();
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
    for (let i = 0; i < displayQuantity; i++) {
      let newLiquor = JSON.stringify(json[i]);

      let displayLiquor = document.getElementById("newArrive");
      displayLiquor.innerHTML = `<a href="javascript:void(0);" onclick="fade();">${newLiquor}</a>`;
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
function searchLiquor(liquorName) {
  const url_search = `http://localhost:8080/api/v1/liquors/${liquorName}/get`

  fetch(url_search).then(function (liquors) {
    // 読み込むデータをJSONに設定
    return liquors.json();
  }).then(function (json) {
    // データ読み出し、表示

  });
}

// 在庫の取り置き
function reserveLiquor(liquorName) {
  const url_reserve = `http://localhost:8080/api/v1/liquors/${liquorName}/post`

  fetch(url_reserve).then(function (liquors) {
    // 読み込むデータをJSONに設定
    return liquors.json();
  }).then(function (json) {
    // 処理結果の表示

  });
}

// 取り置きダイアログ表示時のフェード処理
function fade() {
      var target = document.getElementById("fadeLayer");
      target.style.visibility = "visible";
}


window.onload = getNewLiquors;
