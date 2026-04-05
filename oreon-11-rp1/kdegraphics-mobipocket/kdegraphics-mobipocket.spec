Name:    kdegraphics-mobipocket
Summary: A collection of plugins to handle mobipocket files
Version: 25.12.3
Release:	2%{?dist}

License: GPL-2.0-or-later AND CC0-1.0 AND LGPL-2.1-or-later
URL:     https://www.kde.org/applications/graphics/
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

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
%autosetup


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
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
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
