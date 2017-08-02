from distutils.core import setup

setup(
    name="wsgi-monitor3",
    version="1.0",
    description="Auto-reload WSGI server when files change.",
    url="http://github.org/flanaman/wsgi-monitor3",
    author="MarkFlanagan",
    authoremail="mark.mflanagan@gmail.com",
    py_modules=[
        "wsgi_monitor3",
    ],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
)
