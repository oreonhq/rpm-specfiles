%global source0_hash none

%global stable_kf6 stable


Name:    kdegraphics-mobipocket
Summary: A collection of plugins to handle mobipocket files
Version: 26.04.1
Release: 1%{?dist}

License: GPL-2.0-or-later AND CC0-1.0 AND LGPL-2.1-or-later
URL:     https://www.kde.org/applications/graphics/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Core5Compat)

Obsoletes: qmobipocket < 16.12.0
Provides:  qmobipocket = %{version}-%{release}
Provides:  qmobipocket%{?_isa} = %{version}-%{release}

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%license LICENSES/*
%{_libdir}/libQMobipocket6.so.3*
%{_datadir}/qlogging-categories6/qmobipocket.categories

%files devel
%{_libdir}/libQMobipocket6.so
%{_includedir}/QMobipocket6/
%{_libdir}/cmake/QMobipocket6/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
