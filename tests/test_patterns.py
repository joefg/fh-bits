from fh_bits.patterns import pipeline

def test_pipeline_works():
    p = pipeline.compose(
        lambda x: x + 1,
        lambda x: 2 * x,
        lambda x: -x
    )
    assert p(1) == -4

def test_pipeline_works_on_all_iterables():
    def f(n): return 2 * n
    p = pipeline.compose(
        lambda x: x + 1,
        f,
        lambda x: -x
    )
    assert p(1) == -4
