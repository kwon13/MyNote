import hanspell.spell_checker as checker
a="성능 웰케 좋냐 ㅋㅋㅋ"
result=checker.check(u'{}'.format(a))
print(result.as_dict()['checked'])