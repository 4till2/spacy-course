def test():
    assert (
        'with nlp.disable_pipes("tagger", "parser")' in __solution__
        or 'with nlp.disable_pipes("parser", "tagger")' in __solution__
    ), "你是否在nlp.disable_pipes中调用了正确的组件？"

    __msg__.good(
	"完美！现在我们已经练习了一些技巧来提高性能，我们可以学习下一个章节，"
	"训练一些spaCy的神经网络模型了。"
    )
