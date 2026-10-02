%global source0_hash e532ebd4cbfc8d6d79c6c38c556f1871315fedae8db2b69b574b9c496f171473

%global framework kglobalaccel

%global stable_kf6 stable
%global majmin_ver_kf6 6.30


Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 3 integration module for global shortcuts

# The following are in the LICENSES folder but go unused: LGPL-2.1-only, LGPL-3.0-only, LicenseRef-KDE-Accepted-LGPL
License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Config) >= %{version}
BuildRequires:  cmake(KF6CoreAddons) >= %{version}
BuildRequires:  cmake(KF6Crash) >= %{version}
BuildRequires:  cmake(KF6DBusAddons) >= %{version}
BuildRequires:  cmake(KF6WindowSystem) >= %{version}
BuildRequires:  qt6-qtbase-private-devel
# for systemd-related macros
BuildRequires:  systemd
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel

Requires:       kf6-filesystem

%description
%{summary}.

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
# unpackaged files
%if 0%{?flatpak:1}
rm -fv %{buildroot}%{_prefix}/lib/systemd/user/plasma-kglobalaccel.service
%endif

%find_lang_kf6 kglobalaccel6_qt

%files -f kglobalaccel6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6GlobalAccel.so.*

%files devel
%{_kf6_includedir}/KGlobalAccel/
%{_kf6_libdir}/libKF6GlobalAccel.so
%{_kf6_libdir}/cmake/KF6GlobalAccel/
%{_kf6_datadir}/dbus-1/interfaces/*


%changelog
%autochangelog
