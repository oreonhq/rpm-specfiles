%global source0_hash 172672126592b6e7e572806c2c8eb56ea5afccdc706596130e8b8b9acd8d555e

#global candidate rc0
# Currently fails
%define with_tests 0

Name:      python-can
Version:   4.6.1
Release:   %autorelease
Summary:   Controller Area Network (CAN) support for Python
License:   LGPL-3.0-only
URL:       https://github.com/hardbyte/python-can
Source0:   %{url}/archive/%{version}.tar.gz#/%{name}-%{version}%{?candidate:%{candidate}}.tar.gz

# Allow wrapt 2.x
# https://github.com/hardbyte/python-can/pull/1980
Patch:     %{url}/pull/1980.patch

BuildArch: noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(msgpack)
%if 0%{?with_tests}
BuildRequires:  python3-nose
BuildRequires:  python3-mock
%endif

%description
The Controller Area Network is a bus standard designed to allow microcontrollers
and devices to communicate with each other. It has priority based bus
arbitration, reliable deterministic communication. It is used in cars, trucks,
boats, wheelchairs and more.

The can package provides controller area network support for Python developers;
providing common abstractions to different hardware devices, and a suite of
utilities for sending and receiving messages on a can bus.

%package -n python3-can
Summary:        Controller Area Network (CAN) support for Python 3
%{?python_provide:%python_provide python3-can}

%description -n python3-can
The Controller Area Network is a bus standard designed to allow microcontrollers
and devices to communicate with each other. It has priority based bus
arbitration, reliable deterministic communication. It is used in cars, trucks,
boats, wheelchairs and more.

The can package provides controller area network support for Python developers;
providing common abstractions to different hardware devices, and a suite of
utilities for sending and receiving messages on a can bus.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?candidate:%{candidate}}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files can

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-can -f %{pyproject_files}
%license LICENSE.txt
%{_bindir}/can_*

%changelog
%autochangelog
