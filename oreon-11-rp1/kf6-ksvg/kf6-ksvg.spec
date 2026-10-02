%global source1_hash c44a64430b31affd617589c693722c1f4433f45ed39f8c9cfe83a7e44f5733b4

%global source0_hash 7b7aba4e9baa88bfb303977e139e8a105b5cd243443029ee773954307b51eb91

%global framework ksvg

%global stable_kf6 stable
%global majmin_ver_kf6 6.30

%ifarch aarch64
# Smaller aarch64 VMs OOM (cc1plus Killed, bogus assembler errors) with flto + high -j
%global _lto_cflags %{nil}
%global _smp_mflags -j2
%endif

Name:    kf6-ksvg
Summary: Components for handling SVGs
Version: 6.30.0
Release:        1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig


# upstream patches

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules >= %{version}

BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Svg)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: cmake(KF6Archive) >= %{version}
BuildRequires: cmake(KF6Config) >= %{version}
BuildRequires: cmake(KF6CoreAddons) >= %{version}
BuildRequires: cmake(KF6GuiAddons) >= %{version}
BuildRequires: cmake(KF6Kirigami2) >= %{version}
BuildRequires: cmake(KF6ColorScheme) >= %{version}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{framework}-%{version}

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%files
%license LICENSES/*
%{_kf6_libdir}/libKF6Svg.so.*
%{_kf6_libdir}/qt6/qml/org/kde/ksvg
%{_kf6_datadir}/qlogging-categories6/ksvg.categories

%files devel
%{_kf6_includedir}/KSvg
%{_kf6_libdir}/cmake/KF6Svg
%{_kf6_libdir}/libKF6Svg.so


%changelog
%autochangelog
