%global source0_hash 397f810674e3d55fe46312272289820518d4dbe1b3e475e1e1196b4f1a332f7e
Name:           lxqt-menu-data
Summary:        Menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt
Version:        2.3.0
Release:        1%{?dist}
BuildArch:      noarch
License:        LGPL-2.1-or-later
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools
BuildRequires:  perl
# /oreon:deps
%description
Freedesktop.org compliant menu files for LXQt Panel, Configuration Center and PCManFM-Qt/libfm-qt.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
