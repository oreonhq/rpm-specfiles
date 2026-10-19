%global source0_hash 32a7a4bdb786914445589595273beffbbf9b6a0a3a3dc2cf19ea96114bd2abd7
%global srcname zipstream
%global desc zipstream.py is a zip archive generator based on python 3.3's zipfile.py.\
It was created to generate a zip file generator for streaming (ie web apps).
Name:           python-%{srcname}
Version:        1.1.4
Release:        1%{?dist}
Summary:        ZIP archive generator for Python
License:        GPL-3.0-or-later
URL:            https://github.com/allanlei/%{name}
Source0:        https://github.com/allanlei/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-zipstream = %{version}-%{release}
# /oreon:deps
%description
%{desc}

%package -n python3-%{srcname}
Summary:        ZIP archive generator for Python
BuildRequires:  python3-devel
%description -n python3-%{srcname}
%{desc}
Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/zipstream* usr/lib64/python3*/site-packages/zipstream* usr/bin/*

%check

%pyproject_check_import
%{__python3} -m unittest discover -v
%files
%files -n python3-zipstream -f %{oreon_filedir}/python3-zipstream.list

%changelog

%autochangelog
