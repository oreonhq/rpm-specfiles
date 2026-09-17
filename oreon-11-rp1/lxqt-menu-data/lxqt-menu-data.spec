%global source0_hash 397f810674e3d55fe46312272289820518d4dbe1b3e475e1e1196b4f1a332f7e

Name:           lxqt-menu-data
Summary:        Menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt
Version:        2.3.0
Release:        2%{?dist}
BuildArch:      noarch
License:        LGPL-2.1-or-later
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  perl
BuildRequires:  lxqt-build-tools

%description
Freedesktop.org compliant menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc CHANGELOG README.md
%{_datadir}/cmake/lxqt-menu-data/
%{_datadir}/desktop-directories/lxqt-*.directory
%{_sysconfdir}/xdg/menus/lxqt-*.menu

%changelog
%autochangelog
