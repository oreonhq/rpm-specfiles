%global source0_hash dcb87eaa875aa7a041ca8f49a38c4a8264eb73e5f8b421767b9d541f61a0c050
%global with_tests 0
Name:           python-ntplib
Version:        0.4.0
Release:        1%{?dist}
Summary:        Python module that offers a simple interface to query NTP servers
License:        MIT
URL:            http://pypi.python.org/pypi/ntplib/
Source0:        https://github.com/cf-natali/ntplib/archive/refs/tags/%{version}.tar.gz#/ntplib-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ntplib = %{version}-%{release}
# /oreon:deps
%description
The ntplib is a python module that offers a simple interface to query NTP
servers. It also provides utility functions to translate NTP fields' values to
text (mode, leap indicator...). Since it's pure Python, and only depends on core
modules, it should work on any platform with a Python implementation.

%package -n python3-ntplib
Summary:        Python 3 module that offers a simple interface to query NTP servers
BuildRequires:	python3-devel
%description -n python3-ntplib
The ntplib is a python module that offers a simple interface to query NTP
servers. It also provides utility functions to translate NTP fields' values to
text (mode, leap indicator...). Since it's pure Python, and only depends on core
modules, it should work on any platform with a Python implementation.

Python 3 version.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n ntplib-%{?version}

%build

%pyproject_wheel
%install
%pyproject_install
%if 0%{?with_tests}
%{__python3} test_ntplib.py
%oreon_autofiles python3-ntplib usr/lib/python3*/site-packages/ntplib* usr/lib64/python3*/site-packages/ntplib* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ntplib* usr/lib64/python3*/site-packages/ntplib* usr/bin/*
%endif
%files
%files -n python3-ntplib -f %{oreon_filedir}/python3-ntplib.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.3-40
- Import
