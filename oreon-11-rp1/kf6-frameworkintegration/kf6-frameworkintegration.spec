%global source0_hash 817c49b2f6abbfe624e32f9a21ffcac7edf6e0486a0883050a1441e2fef3c932

%global framework frameworkintegration

%global stable_kf6 stable
%global majmin_ver_kf6 6.30


Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 4 workspace and cross-framework integration plugins
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6NewStuff) >= %{version}
BuildRequires:  cmake(KF6Package) >= %{version}
BuildRequires:  kf6-rpm-macros
BuildRequires:  libXcursor-devel
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(KF6Config) >= %{version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{version}
BuildRequires:  cmake(KF6I18n) >= %{version}
BuildRequires:  cmake(KF6IconThemes) >= %{version}
BuildRequires:  cmake(KF6KIO) >= %{version}
BuildRequires:  cmake(KF6Notifications) >= %{version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{version}
BuildRequires:  cmake(AppStreamQt) >= 1.0
BuildRequires:  cmake(packagekitqt6)
BuildRequires:  cmake(KF6ColorScheme) >= %{version}
Requires:  kf6-filesystem

%description
Framework Integration is a set of plugins responsible for better integration of
Qt applications when running on a KDE Plasma workspace.

Applications do not need to link to this directly.

%package        libs
Summary:        Runtime libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6IconThemes)
Requires:       cmake(KF6ConfigWidgets)

%description    devel
The %{name}-devel package contains files to develop for %{name}.


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
%{_kf6_datadir}/knotifications6/plasma_workspace.notifyrc
%dir %{_kf6_libexecdir}/kpackagehandlers
%{_kf6_libexecdir}/kpackagehandlers/knshandler

%files libs
%{_kf6_libdir}/libKF6Style.so.*
%{_kf6_plugindir}/FrameworkIntegrationPlugin.so
%{_kf6_libexecdir}/kpackagehandlers/appstreamhandler

%files devel
%{_kf6_includedir}/FrameworkIntegration/
%{_kf6_includedir}/KStyle/
%{_kf6_libdir}/libKF6Style.so
%{_kf6_libdir}/cmake/KF6FrameworkIntegration/


%changelog
%autochangelog
