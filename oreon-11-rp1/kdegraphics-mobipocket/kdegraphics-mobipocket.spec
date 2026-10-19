%global source0_hash 26cf058d441ec1a23768a47026960a0b7b77ca40dc7de51c89a9b4d463851f92
%global stable_kf6 stable
Name:    kdegraphics-mobipocket
Summary:        A collection of plugins to handle mobipocket files
Version: 26.04.3
Release:        1%{?dist}
License: GPL-2.0-or-later AND CC0-1.0 AND LGPL-2.1-or-later
URL:     https://www.kde.org/applications/graphics/
Obsoletes: qmobipocket < 16.12.0
Provides:  qmobipocket = %{version}-%{release}
Provides:  qmobipocket%{?_isa} = %{version}-%{release}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: qmobipocket-devel < 16.12.0
Provides:  qmobipocket-devel = %{version}-%{release}
Provides:  qmobipocket-devel%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
	-DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kdegraphics-mobipocket-devel -f %{oreon_filedir}/kdegraphics-mobipocket-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
