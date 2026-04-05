%global framework kded

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-%{framework}
Version: 6.24.0
Release:	4%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon with extensible daemon for system-level services

License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Service)
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
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Use kf6 cmake build/install macros (avoid qt6 prepare_docs / install_html_docs)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
