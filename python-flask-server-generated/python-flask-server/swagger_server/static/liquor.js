"use strict";

const url_get    = 'http://localhost:8080/api/v1/liquors/get'

// 新しく入荷されたお酒を表示する
function getNewLiquors() {
  fetch(url_get).then(function (liquors) {
    // 読み込むデータをJSONに設定
    return liquors.json();
  }).then(function (json) {
    // データ読み出し、表示

  });
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
