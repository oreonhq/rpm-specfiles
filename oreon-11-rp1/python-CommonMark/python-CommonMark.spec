%global source0_hash 452f9dc859be7f06631ddcb328b6919c67984aca654e5fefb3914d54691aed60

%global pypi_name CommonMark
%global desc Pure Python port of jgm’s stmd.js, a Markdown parser and renderer for the\
CommonMark specification, using only native modules. Once both this project and\
the CommonMark specification are stable we will release the first 1.0 version\
and attempt to keep up to date with changes in stmd.js.\
\
We are currently at the same development stage (actually a bit ahead because we\
have implemented HTML entity conversion and href URL escaping) as stmd.js. Since\
Python versions pre-3.4 use outdated (i.e. not HTML5 spec) entity conversion,\
I’ve converted the 3.4 implementation into a single file, entitytrans.py which\
so far seems to work (all tests pass on 2.7, 3.3, and 3.4).

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        25%{?dist}
Summary:        Python parser for the CommonMark Markdown spec

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://files.pythonhosted.org/packages/60/48/a60f593447e8f0894ebb7f6e6c1f25dafc5e89c5879fdc9360ae93ff83f0/commonmark-0.9.1.tar.gz

Patch0:         0001-Rename-cmark-entrypoint.patch

BuildArch:      noarch

%description
%{desc}

%package utils
Summary:        Command-line tools built using %{name}

%description utils
%{desc}

This package contains the 'commonmark' command.

%package doc
Summary:        Documentation for python-%{pypi_name}

%description doc
%{desc}

Documentation package.

%package -n     python%{python3_pkgversion}-%{pypi_name}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-hypothesis
Suggests:       python-CommonMark-doc
Suggests:       %{name}-utils == %{version}-%{release}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n commonmark-%{version}

# Fix non executable scripts
sed -i '1{\@^#!/usr/bin/env python@d}' commonmark/tests/run_spec_tests.py
sed -i '1{\@^#!/usr/bin/env python@d}' commonmark/cmark.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l commonmark

%check
%pyproject_check_import

export PYTHONIOENCODING=UTF-8
PYTHONPATH=$(pwd) %{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%license LICENSE

%files utils
%license LICENSE
%{_bindir}/commonmark

%files doc
%license LICENSE
%doc README.rst spec.txt

%changelog
%autochangelog
