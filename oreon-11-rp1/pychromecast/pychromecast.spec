%global source0_hash ce9f966c4d555165a1b30e6c5879794760248535e31498a190ca20111d40a4d8
Name:           pychromecast
Version:        14.0.10
Release:        1%{?dist}
Summary:        Python library to communicate with the Google Chromecast
License:        MIT
URL:            https://github.com/home-assistant-libs/pychromecast
Source0:        https://github.com/home-assistant-libs/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 83.0
BuildRequires:  python3dist(setuptools) >= 65.6
BuildRequires:  python3dist(wheel) < 0.47.0
BuildRequires:  python3dist(wheel) >= 0.37.1
Requires:       python3-pychromecast = %{version}-%{release}
# /oreon:deps
%description
Library for Python 3 to communicate with the Google Chromecast. It
currently supports:

-  Auto discovering connected Chromecasts on the network
-  Start the default media receiver and play any online media
-  Control playback of current playing media
-  Implement Google Chromecast api v2
-  Communicate with apps via channels
-  Easily extendable to add support for unsupported namespaces
-  Multi-room setups with Audio cast devices

%package -n python3-chromecast
Summary:  Library for Python 3 to communicate with the Google Chromecast
%{?python_provide:%python_provide python3-chromecast}
%description -n python3-chromecast
Library for Python 3 to communicate with the Google Chromecast. It
currently supports:

-  Auto discovering connected Chromecasts on the network
-  Start the default media receiver and play any online media
-  Control playback of current playing media
-  Implement Google Chromecast api v2
-  Communicate with apps via channels
-  Easily extendable to add support for unsupported namespaces
-  Multi-room setups with Audio cast devices

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-chromecast usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%py3_check_import pychromecast
%files
%files -n python3-chromecast -f %{oreon_filedir}/python3-chromecast.list

%changelog

%autochangelog
