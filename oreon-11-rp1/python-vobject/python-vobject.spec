%global source0_hash db00a7f4db49397155dd8a6871e8a2a0175a6eba5a654c30e910f82b29514b58

%global modname vobject
%global sum A python library for manipulating vCard and vCalendar files

Name:           python-vobject
Version:        0.9.8
Release:        7%{?dist}
Summary:        %{sum}

License:        Apache-2.0
URL:            https://py-vobject.github.io/
Source0:        https://pypi.python.org/packages/source/v/vobject/%{modname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  git

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

%check
%{__python3} tests.py

%files -n python3-%{modname}
%doc README.md
# ACKNOWLEDGEMENTS.txt
%license LICENSE-2.0.txt
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*
%{_bindir}/change_tz
%{_bindir}/ics_diff

%changelog
%autochangelog
