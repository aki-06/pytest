# mainディレクトリのcalc.pyのCalcクラスを呼び出す
from main.calc import Calc

def test_add_01():
	assert Calc(9, 2).add() == 11

def test_add_02():
	assert Calc(-9, 2).add() == -7

def test_dif_01():
	assert Calc(9, 2) == 7

def test_dif_02():
	assert Calc(-9, 2) == -11

def test_seki_01():
	assert Calc(9, 2) == 18

def test_seki_02():
	assert Calc(-9, 2) == -18

def test_shou_01():
	assert Calc(9, 2) == 4.5

def test_shou_02():
	assert Calc(-9, 2) == -4.5