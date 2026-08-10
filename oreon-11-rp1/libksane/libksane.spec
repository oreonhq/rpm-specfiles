%global source0_hash ca86e492328262cc6d89c1b131139edeb6b4e1eeb15b84fba8a172fe09a25f70

Name:    libksane
Summary: SANE Library interface for KDE
Version: 26.04.3
Release: 1%{?dist}

License: CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/graphics/%{name}
Source0: https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gettext

BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KSaneCore6)

BuildRequires: pkgconfig(sane-backends)

Conflicts: kf5-libksane < 24.01
Obsoletes: kf5-libksane < 24.01
Obsoletes: %{name}-common < 24.12.0
Obsoletes: %{name}-qt5 < 24.12.0
Obsoletes: %{name}-qt6 < 24.12.0


%description
%{summary}.


%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Widgets)
Obsoletes: kf5-libksane-devel < 24.01
Obsoletes: %{name}-qt5-devel < 24.12.0
Obsoletes: %{name}-qt6-devel < 24.12.0

%description devel
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1


%build
%global _vpath_builddir %{_target_platform}-qt6
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build


%install
%global _vpath_builddir %{_target_platform}-qt6
%cmake_install

%find_lang %{name} --all-name --with-html


%files -f %{name}.lang
%doc AUTHORS
%license COPYING*
%license LICENSES/*
%{_datadir}/icons/hicolor/*/actions/*
%{_libdir}/libKSaneWidgets6.so.{6,%{version}}

%files devel
%{_includedir}/KSaneWidgets6/
%{_libdir}/libKSaneWidgets6.so
%{_libdir}/cmake/KSaneWidgets6/

%changelog
%autochangelog

