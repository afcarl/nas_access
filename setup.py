#
# This file is autogenerated during plugin quickstart and overwritten during
# plugin makedist. DO NOT CHANGE IT if you plan to use plugin makedist to update 
# the distribution.
#

from setuptools import setup, find_packages

kwargs = {'author': '',
 'author_email': '',
 'classifiers': ['Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering'],
 'description': 'OpenMDAO interface to NASA HEC systems at Ames Research Center.',
 'download_url': '',
 'entry_points': '[openmdao.component]\nnas_access.test.test_nas_access.Echo=nas_access.test.test_nas_access:Echo\nnas_access.test.nas_test.Simulation=nas_access.test.nas_test:Simulation\n\n[openmdao.container]\nnas_access.test.test_nas_access.Echo=nas_access.test.test_nas_access:Echo\nnas_access.test.nas_test.Simulation=nas_access.test.nas_test:Simulation',
 'include_package_data': True,
 'install_requires': ['openmdao.main'],
 'keywords': ['openmdao'],
 'license': '',
 'maintainer': '',
 'maintainer_email': '',
 'name': 'nas_access',
 'package_data': {'nas_access': ['sphinx_build/html/index.html',
                                 'sphinx_build/html/.buildinfo',
                                 'sphinx_build/html/py-modindex.html',
                                 'sphinx_build/html/objects.inv',
                                 'sphinx_build/html/searchindex.js',
                                 'sphinx_build/html/search.html',
                                 'sphinx_build/html/pkgdocs.html',
                                 'sphinx_build/html/usage.html',
                                 'sphinx_build/html/genindex.html',
                                 'sphinx_build/html/srcdocs.html',
                                 'sphinx_build/html/tutorial.html',
                                 'sphinx_build/html/_sources/usage.txt',
                                 'sphinx_build/html/_sources/pkgdocs.txt',
                                 'sphinx_build/html/_sources/tutorial.txt',
                                 'sphinx_build/html/_sources/index.txt',
                                 'sphinx_build/html/_sources/srcdocs.txt',
                                 'sphinx_build/html/_static/plus.png',
                                 'sphinx_build/html/_static/comment-bright.png',
                                 'sphinx_build/html/_static/comment.png',
                                 'sphinx_build/html/_static/down-pressed.png',
                                 'sphinx_build/html/_static/sidebar.js',
                                 'sphinx_build/html/_static/doctools.js',
                                 'sphinx_build/html/_static/ajax-loader.gif',
                                 'sphinx_build/html/_static/default.css',
                                 'sphinx_build/html/_static/down.png',
                                 'sphinx_build/html/_static/jquery.js',
                                 'sphinx_build/html/_static/underscore.js',
                                 'sphinx_build/html/_static/minus.png',
                                 'sphinx_build/html/_static/up-pressed.png',
                                 'sphinx_build/html/_static/up.png',
                                 'sphinx_build/html/_static/pygments.css',
                                 'sphinx_build/html/_static/searchtools.js',
                                 'sphinx_build/html/_static/file.png',
                                 'sphinx_build/html/_static/basic.css',
                                 'sphinx_build/html/_static/websupport.js',
                                 'sphinx_build/html/_static/comment-close.png',
                                 'sphinx_build/html/_modules/index.html',
                                 'sphinx_build/html/_modules/nas_access/protocol.html',
                                 'sphinx_build/html/_modules/nas_access/rje.html',
                                 'sphinx_build/html/_modules/nas_access/proxy.html',
                                 'sphinx_build/html/_modules/nas_access/wrapper.html',
                                 'sphinx_build/html/_modules/nas_access/test/scp.html',
                                 'sphinx_build/html/_modules/nas_access/test/ssh.html',
                                 'sphinx_build/html/_modules/nas_access/test/test_nas_access.html',
                                 'sphinx_build/html/_modules/nas_access/test/nas_test.html',
                                 'sphinx_build/html/_images/dataflow.png',
                                 'sphinx_build/html/_images/putty-auth.png',
                                 'sphinx_build/html/_images/putty-session.png',
                                 'sphinx_build/html/_images/putty-user.png',
                                 'sphinx_build/html/_images/putty-gen.png',
                                 'test/__init__.py',
                                 'test/nas_test.py',
                                 'test/test_nas_access.py',
                                 'test/.coverage',
                                 'test/ssh.py',
                                 'test/scp.py']},
 'package_dir': {'': 'src'},
 'packages': ['nas_access', 'nas_access.test'],
 'url': '',
 'version': '0.6.2',
 'zip_safe': False}


setup(**kwargs)

