import nox


@nox.session(python=['2.7', '3.5', '3.6', '3.7', '3.8', '3.9', '3.10'])
def tests(session):
    session.install('-r', 'requirements/test.txt', '-e', '.')
    session.run('pytest')
