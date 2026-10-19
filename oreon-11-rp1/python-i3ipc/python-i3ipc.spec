%global source0_hash 54af180fac6e3e16c65747884ae4479f0df034c45ed02523f8300f98c99eb29e
%bcond_with     tests
Name:           python-i3ipc
Version:        2.2.1
Release:        1%{?dist}
Summary:        An improved Python library to control i3wm
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/altdesktop/i3ipc-python
BuildArch:      noarch
Source0:        https://github.com/altdesktop/i3ipc-python/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Adapt-test-launcher-for-our-envirnoment.patch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  i3
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-setuptools
BuildRequires:  python3-xlib
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description

%package -n python3-i3ipc
Summary:        An improved Python library to control i3wm
%description -n python3-i3ipc

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n i3ipc-python-%{version}

sed -i '/^#!/d' i3ipc/connection.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles python3-i3ipc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

%python3 run-tests.py --timeout 20
%endif
%files -f %{oreon_filedir}/main.list
%files -n python3-i3ipc -f %{oreon_filedir}/python3-i3ipc.list

%changelog

%autochangelog
