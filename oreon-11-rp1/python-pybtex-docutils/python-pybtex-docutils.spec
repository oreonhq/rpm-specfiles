%global source0_hash 3a7ebdf92b593e00e8c1c538aa9a20bca5d92d84231124715acc964d51d93c6b

Name:           python-pybtex-docutils
Version:        1.0.3
Release:        12%{?dist}
Summary:        Docutils backend for pybtex

# The content is MIT.  Other licenses are due to files copied in by Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/basic.css: BSD-2-Clause
# _static/classic.css: BSD-2-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sidebar.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        MIT AND BSD-2-Clause
URL:            https://pybtex-docutils.readthedocs.io/
VCS:            git:https://github.com/mcmtroffaes/pybtex-docutils.git
Source:         %pypi_source pybtex-docutils

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(install): -l pybtex_docutils

BuildRequires:  make
BuildRequires:  python3-docs
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist sphinx}

%global common_desc %{expand:This package contains a docutils backend for pybtex, a BibTeX-compatible
bibliography processor written in Python.  Bibliographic references in BibTeX
format (or any other format supported by pybtex) can be inserted into python
documentation to be rendered by docutils.}

%description
%common_desc

%package -n python3-pybtex-docutils
Summary:        Docutils backend for pybtex
Provides:       bundled(js-jquery)
Provides:       bundled(js-underscore)

%description -n python3-pybtex-docutils
%common_desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pybtex-docutils-%{version}

%conf
# Update the sphinx theme name
sed -i "s/'default'/'classic'/" doc/conf.py

# Use local objects.inv for intersphinx
sed -i "s|\('http://docs\.python\.org/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" doc/conf.py

%build -a
PYTHONPATH=$PWD/src make -C doc html
rst2html --no-datestamp README.rst README.html

%check
%pytest -v test

%files -n python3-pybtex-docutils -f %{pyproject_files}
%doc README.html doc/_build/html/*

%changelog
%autochangelog
