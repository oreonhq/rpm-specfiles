%global source0_hash b645d5d17c967fd09c3d7abdfc262740a95870dd66bd3e5f4c0382da097d8510

%global framework kdav

%global stable_kf6 stable
%global majmin_ver_kf6 6.28


Name:    kf6-%{framework}
Version: 20.04.3
Release:        1%{?dist}
Summary: A DAV protocol implementation with KJobs

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Gui)

BuildRequires:  cmake(KF6I18n) >= %{version}
BuildRequires:  cmake(KF6CoreAddons) >= %{version}
BuildRequires:  cmake(KF6KIO) >= %{version}
BuildRequires:  pkgconfig(xkbcommon)

Requires:  kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
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
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%doc README*
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*%{framework}.*
%{_kf6_libdir}/libKF6DAV.so.6
%{_kf6_libdir}/libKF6DAV.so.%{version}

%files devel
%{_kf6_includedir}/KDAV/
%{_kf6_libdir}/libKF6DAV.so
%{_kf6_libdir}/cmake/KF6DAV/


%changelog
%autochangelog
