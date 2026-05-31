%global source0_hash 2eb3688fc52244330c4837f0e446122b9726da777a3f301fe3b0c73f92202036

Name:		python-libevdev
Version:	0.13.1
Release:	2%{?dist}
Summary:	Python bindings to the libevdev evdev device wrapper library

# SPDX
License:	MIT
URL:		https://pypi.python.org/pypi/libevdev/
Source0:        https://gitlab.freedesktop.org/libevdev/python-libevdev/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

%description
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.

%package -n	python3-libevdev
Summary:	Python bindings to the libevdev evdev device wrapper library

BuildRequires:	python3-devel python3dist(hatchling)
Requires:	libevdev

%{?python_provide:%python_provide python3-libevdev}

%description -n	python3-libevdev
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.


%generate_buildrequires
%pyproject_buildrequires


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1


%build
%pyproject_wheel


%install
%pyproject_install


%files -n	python3-libevdev
%license COPYING
%{python3_sitelib}/libevdev/
%{python3_sitelib}/libevdev-%{version}.dist-info

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.13.1-2
- Prepare for Oreon 11 (RP1)
