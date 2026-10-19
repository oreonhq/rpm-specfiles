%global source0_hash ac44e5d7e2079d84c1d52c50a615b9bec4b1ba958608c4c7fe40cbf33247b38e
%global modname vobject
%global sum A python library for manipulating vCard and vCalendar files
Name:           python-vobject
Version:        0.9.9
Release:        1%{?dist}
Summary:        A python library for manipulating vCard and vCalendar files
License:        Apache-2.0
URL:            https://py-vobject.github.io/
Source0:        https://pypi.python.org/packages/source/v/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  git
BuildRequires:  python3-dateutil
BuildRequires:  python3-devel
BuildRequires:  python3-pytz
BuildRequires:  python3-setuptools
# /oreon:deps
%description
VObject is intended to be a full featured python library for parsing and
generating vCard and vCalendar files.

%package -n         python3-%{modname}
Summary:            %{sum}
Requires:           python3-dateutil
Requires:           python3-setuptools
BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-dateutil
BuildRequires:      python3-pytz
%{?python_provide:%python_provide python3-%{modname}}
%description -n python3-vobject
VObject is intended to be a full featured python library for parsing and
generating vCard and vCalendar files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1
rm vobject/win32tz.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__python3} tests.py
%files -f %{oreon_filedir}/main.list
%files -n python3-vobject -f %{oreon_filedir}/python3-vobject.list

%changelog

%autochangelog
