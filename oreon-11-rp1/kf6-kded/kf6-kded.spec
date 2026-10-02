%global source0_hash 0adf6e22300cee74d57e790b5db844f03a1366a4d6315edbaa49174b12bf1861

%global framework kded

%global stable_kf6 stable
%global majmin_ver_kf6 6.30

Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon with extensible daemon for system-level services

License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config) >= %{version}
BuildRequires:  cmake(KF6CoreAddons) >= %{version}
BuildRequires:  cmake(KF6Crash) >= %{version}
BuildRequires:  cmake(KF6DBusAddons) >= %{version}
BuildRequires:  cmake(KF6DocTools) >= %{version}
BuildRequires:  cmake(KF6Service) >= %{version}
BuildRequires:  kf6-rpm-macros

BuildRequires:  qt6-qtbase-devel

BuildRequires:  systemd
Requires:  kf6-filesystem

%description
KDED stands for KDE Daemon which isn't very descriptive. KDED runs
in the background and performs a number of small tasks. Some of these
tasks are built in, others are started on demand.

Custom KDED modules can be provided by 3rd party frameworks and
applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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
%find_lang kded6 --with-man
# create/own this
mkdir -p %{buildroot}%{_kf6_plugindir}/kded

%post
%systemd_user_post  plasma-kded.service

%preun
%systemd_user_preun plasma-kded.service

%files -f kded6.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_bindir}/kded6
%{_kf6_datadir}/applications/org.kde.kded6.desktop
%{_kf6_datadir}/dbus-1/services/*.service
%{_kf6_mandir}/man8/kded6.8*
%dir %{_kf6_plugindir}/kded/
%{_userunitdir}/plasma-kded6.service

%files devel
%{_kf6_libdir}/cmake/KF6KDED/
%{_kf6_datadir}/dbus-1/interfaces/*.xml

%changelog
%autochangelog
