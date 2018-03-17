# mainディレクトリのsay.pyのFooクラスとHogeクラスを呼び出す
from main.say import Foo, Hoge

def test_foo_say():
	assert Foo().say() == 'foo'

def test_foo_say2():
	assert Foo().say2() == 'foo' # わざとエラー

def test_hoge_say():
	assert 'hoge'

def test_hoge2_say():
	assert 'hoge2'