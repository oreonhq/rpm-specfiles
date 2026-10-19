%global source0_hash 2eb3688fc52244330c4837f0e446122b9726da777a3f301fe3b0c73f92202036
Name:		python-libevdev
Version:	0.13.1
Release:        2%{?dist}
Summary:        Python bindings to the libevdev evdev device wrapper library
License:	MIT
URL:		https://pypi.python.org/pypi/libevdev/
Source0:        https://gitlab.freedesktop.org/libevdev/python-libevdev/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-libevdev = %{version}-%{release}
# /oreon:deps
%description
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.

%package -n	python3-libevdev
Summary:	Python bindings to the libevdev evdev device wrapper library
BuildRequires:	python3-devel python3dist(hatchling)
Requires:	libevdev
%{?python_provide:%python_provide python3-libevdev}
# oreon:reqs
Requires:       python3dist(typing-extensions) >= 4.0
# /oreon:reqs
%description -n	python3-libevdev
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-libevdev usr/lib/python3*/site-packages/libevdev* usr/lib64/python3*/site-packages/libevdev* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/libevdev* usr/lib64/python3*/site-packages/libevdev* usr/bin/*

%files
%files -n python3-libevdev -f %{oreon_filedir}/python3-libevdev.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.13.1-2
- Prepare for Oreon 11 (RP1)
