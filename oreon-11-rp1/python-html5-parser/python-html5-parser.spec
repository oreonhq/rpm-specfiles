%global source0_hash 3d7f89841aa48b976311f43863178c34c141abcf1dd45b67a7339e61cffe5306

%global srcname html5-parser

Name:           python-%{srcname}
Version:        0.4.12
Release:        10%{?dist}
Summary:        A fast, standards compliant, C based, HTML 5 parser for python

# html5-parser-0.4.4/gumbo/utf8.c is MIT
# Automatically converted from old format: ASL 2.0 and MIT - review is highly recommended.
License:        Apache-2.0 AND LicenseRef-Callaway-MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  libxml2-devel
BuildRequires:  pkgconf
# For tests
BuildRequires:  python3-lxml >= 3.8.0
BuildRequires:  gtest-devel
BuildRequires:  python3-chardet
BuildRequires:  python3-beautifulsoup4

%description
A fast, standards compliant, C based, HTML 5 parser for python

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

# This package bundles sigil-gumbo a fork of gumbo
# Base project: https://github.com/google/gumbo-parser
# Forked from above: https://github.com/Sigil-Ebook/sigil-gumbo
# It also patches that bundled copy with other changes.
# sigil-gumbo bundled here was added 20170601
Provides:      bundled(sigil-gumbo) = 0.9.3-20170601git0830e1145fe08
# sigil-gumbo forked off gumbo-parser at this commit in 20160216
Provides:      bundled(gumbo-parser) = 0.9.3-20160216git69b580ab4de04

%description -n python3-%{srcname}
A fast, standards compliant, C based, HTML 5 parser for python

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

export debug=True
%autosetup -n %{srcname}-%{version} -p1

# remove shebangs from library files
sed -i -e '/^#!\//, 1d' src/html5_parser/*.py

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/*

%changelog
%autochangelog
