%global source0_hash e5c96840ba21e7afa6e0635b21cc117552898b14628d9555f2a600c77884747d

Name:    ksanecore
Summary: Library providing logic to interface scanners
Version: 26.04.3
Release: 1%{?dist}

License: BSD and LGPLv2.1-only and LGPLv3.0-only
URL:     https://invent.kde.org/libraries/ksanecore
Source0: https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++

BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)

BuildRequires: pkgconfig(sane-backends)

Conflicts: %{name} < 24.01
Obsoletes: %{name}-common < 24.12.0
Obsoletes: %{name}-qt5 < 24.12.0
Obsoletes: %{name}-qt6 < 24.12.0

%description
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Gui)
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
%doc README.md
%license LICENSES/*
%{_libdir}/libKSaneCore6.so.{1,%{maj_ver_kf6}.*}

%files devel
%{_includedir}/KSaneCore6/
%{_libdir}/cmake/KSaneCore6/
%{_libdir}/libKSaneCore6.so

%changelog
%autochangelog
