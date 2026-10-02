%global source0_hash 4a133decdb0d3731dbaa1d3625b30f057089e5c59c8326ff88a047cef35b2efb

%global framework knotifyconfig

%global stable_kf6 stable
%global majmin_ver_kf6 6.30


Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 3 module for KNotify configuration

License: CC0-1.0 AND LGPL-2.0-only
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Completion) >= %{version}
BuildRequires:  cmake(KF6Config) >= %{version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{version}
BuildRequires:  cmake(KF6I18n) >= %{version}
BuildRequires:  cmake(KF6KIO) >= %{version}
BuildRequires:  cmake(KF6Notifications) >= %{version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{version}
BuildRequires:  cmake(KF6XmlGui) >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(Qt6TextToSpeech)
Requires:  kf6-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*%{framework}.*
%{_kf6_libdir}/libKF6NotifyConfig.so.*

%files devel
%{_kf6_includedir}/KNotifyConfig/
%{_kf6_libdir}/libKF6NotifyConfig.so
%{_kf6_libdir}/cmake/KF6NotifyConfig/


%changelog
%autochangelog
