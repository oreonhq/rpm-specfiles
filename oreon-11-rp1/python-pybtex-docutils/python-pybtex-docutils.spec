%global source0_hash 3a7ebdf92b593e00e8c1c538aa9a20bca5d92d84231124715acc964d51d93c6b
Name:           python-pybtex-docutils
Version:        1.0.3
Release:        12%{?dist}
Summary:        Docutils backend for pybtex
License:        MIT AND BSD-2-Clause
URL:            https://pybtex-docutils.readthedocs.io/
VCS:            git:https://github.com/mcmtroffaes/pybtex-docutils.git
Source0:        https://files.pythonhosted.org/packages/source/p/pybtex-docutils/pybtex-docutils-%{version}.tar.gz
BuildArch:      noarch
%global common_desc %{expand:This package contains a docutils backend for pybtex, a BibTeX-compatible
bibliography processor written in Python.  Bibliographic references in BibTeX
format (or any other format supported by pybtex) can be inserted into python
documentation to be rendered by docutils.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pybtex-docutils = %{version}-%{release}
# /oreon:deps
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

%build

%pyproject_wheel
PYTHONPATH=$PWD/src make -C doc html
rst2html --no-datestamp README.rst README.html
%install
%pyproject_install
%oreon_autofiles python3-pybtex-docutils usr/lib/python3*/site-packages/pybtex_docutils* usr/lib64/python3*/site-packages/pybtex_docutils* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pybtex_docutils* usr/lib64/python3*/site-packages/pybtex_docutils* usr/bin/*

%check

%pytest -v test
%files
%files -n python3-pybtex-docutils -f %{oreon_filedir}/python3-pybtex-docutils.list

%changelog

%autochangelog
