%global source0_hash 54af180fac6e3e16c65747884ae4479f0df034c45ed02523f8300f98c99eb29e

# disable tests due to intermittent failures
# https://github.com/altdesktop/i3ipc-python/issues/149
%bcond_with     tests

Name:           python-i3ipc
Version:        2.2.1
Release:        20%{?dist}
Summary:        An improved Python library to control i3wm
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/altdesktop/i3ipc-python
BuildArch:      noarch

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/altdesktop/i3ipc-python/pull/76
Patch0:         0001-Adapt-test-launcher-for-our-envirnoment.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
# Test deps
BuildRequires:  i3
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-timeout
BuildRequires:  python3-xlib
BuildRequires:  xorg-x11-server-Xvfb
%endif

%global _description %{expand:
i3's interprocess communication (or ipc) is the interface i3wm uses to receive
commands from client applications such as i3-msg. It also features
a publish/subscribe mechanism for notifying interested parties of window
manager events.

i3ipc-python is a Python library for controlling the window manager. This
project is intended to be useful for general scripting, and for applications
that interact with the window manager like status line generators, notification
daemons, and pagers.}

%description %{_description}

%package -n python3-i3ipc
Summary:        %{summary}

%description -n python3-i3ipc %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n i3ipc-python-%{version}

sed -i '/^#!/d' i3ipc/connection.py

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
%python3 run-tests.py --timeout 20
%endif

%files -n python3-i3ipc
%license LICENSE
%doc README.rst
%{python3_sitelib}/i3ipc/
%{python3_sitelib}/i3ipc-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
