%global source0_hash b17f8242309e1502119c48b1ef5059a396a3068596a84fb79fdef6d9e2cd4f49

%global framework kcrash

%global stable_kf6 stable
%global majmin_ver_kf6 6.30


Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 2 addon for handling application crashes

License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6CoreAddons) >= %{version}
BuildRequires:  cmake(KF6WindowSystem) >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  libX11-devel
BuildRequires:  qt6-qtbase-devel

%description
KCrash provides support for intercepting and handling application crashes.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1


%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Crash.so.*

%files devel
%{_kf6_includedir}/KCrash/
%{_kf6_libdir}/libKF6Crash.so
%{_kf6_libdir}/cmake/KF6Crash/


%changelog
%autochangelog
