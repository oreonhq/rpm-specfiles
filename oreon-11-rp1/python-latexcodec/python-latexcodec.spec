%global source0_hash e78a6911cd72f9dec35031c6ec23584de6842bfbc4610a9678868d14cdfb0357
Name:           python-latexcodec
Version:        3.0.1
Release:        1%{?dist}
Summary:        Lexer and codec to work with LaTeX code in Python
License:        MIT
URL:            https://latexcodec.readthedocs.io/
VCS:            git:https://github.com/mcmtroffaes/latexcodec.git
Source0:        https://files.pythonhosted.org/packages/source/l/latexcodec/latexcodec-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-latexcodec = %{version}-%{release}
# /oreon:deps
%description
This package contains a lexer and codec to work with LaTeX code in Python.

%package -n python3-latexcodec
Summary:        Lexer and codec to work with LaTeX code in Python
%description -n python3-latexcodec
This package contains a lexer and codec to work with LaTeX code in Python.

%package doc
License:        MIT AND BSD-2-Clause
Summary:        Documentation for %{name}
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n latexcodec-%{version} -p1

%conf
# Update the sphinx theme name
sed -i 's/default/classic/' doc/conf.py

# Use local objects.inv for intersphinx
sed -i "s|\('http://docs\.python\.org/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" doc/conf.py

%build

%pyproject_wheel
PYTHONPATH=$PWD make -C doc html
rm -f doc/_build/html/.buildinfo
rst2html --no-datestamp LICENSE.rst LICENSE.html
%install
%pyproject_install
%oreon_autofiles python3-latexcodec usr/lib/python3*/site-packages/latexcodec* usr/lib64/python3*/site-packages/latexcodec* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/latexcodec* usr/lib64/python3*/site-packages/latexcodec* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v
%files
%files -n python3-latexcodec -f %{oreon_filedir}/python3-latexcodec.list
%files -n python-latexcodec-doc -f %{oreon_filedir}/python-latexcodec-doc.list

%changelog

%autochangelog
