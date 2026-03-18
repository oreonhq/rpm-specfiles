%global base_name libktorrent


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-libktorrent
Summary: Library providing torrent downloading code
Version: 23.08.5
Release: 6%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/network/%{base_name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz

## upstream patches

BuildRequires: boost-devel
BuildRequires: gettext
BuildRequires: gmp-devel >= 6.0.0
BuildRequires: libgcrypt-devel >= 1.4.5
BuildRequires: cmake(Qca-qt5)
BuildRequires: cmake(Qt5Network)

# kf5 deps
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Solid)

%description
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: boost-devel
# mse/bigint.h:#include <gmp.h>
Requires: gmp-devel%{?_isa}
Requires: libgcrypt-devel
Requires: cmake(KF5Archive)
Requires: cmake(KF5Config)
Requires: cmake(KF5KIO)
Requires: cmake(Qt5Network)
%description devel
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang libktorrent5

%ldconfig_scriptlets

%files -f libktorrent5.lang
%doc ChangeLog
%license LICENSES/*
%{_kf5_libdir}/libKF5Torrent.so.6*
%{_kf5_libdir}/libKF5Torrent.so.%{version}

%files devel
%{_kf5_includedir}/libktorrent/
%{_kf5_libdir}/libKF5Torrent.so
%{_kf5_libdir}/cmake/KF5Torrent/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-6
- Prepare for Oreon 11 (RP1)
