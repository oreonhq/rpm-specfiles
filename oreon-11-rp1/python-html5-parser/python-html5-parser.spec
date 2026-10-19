%global source0_hash 3d7f89841aa48b976311f43863178c34c141abcf1dd45b67a7339e61cffe5306
%global srcname html5-parser
Name:           python-%{srcname}
Version:        0.4.12
Release:        1%{?dist}
Summary:        A fast, standards compliant, C based, HTML 5 parser for python
License:        Apache-2.0 AND LicenseRef-Callaway-MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtest-devel
BuildRequires:  libxml2-devel
BuildRequires:  pkgconf
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-chardet
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-setuptools
# /oreon:deps
%description
A fast, standards compliant, C based, HTML 5 parser for python

%package -n python3-%{srcname}
Summary:        A fast, standards compliant, C based, HTML 5 parser for python
%{?python_provide:%python_provide python3-%{srcname}}
Provides:      bundled(sigil-gumbo) = 0.9.3-20170601git0830e1145fe08
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__python3} setup.py test
%files -f %{oreon_filedir}/main.list
%files -n python3-html5-parser -f %{oreon_filedir}/python3-html5-parser.list

%changelog

%autochangelog
