const Liquor = artifacts.require("./Liquor.sol");

module.exports = function(deployer) {
  deployer.deploy(Liquor);
};
