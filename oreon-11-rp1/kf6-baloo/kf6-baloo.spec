%global framework baloo

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-%{framework}
Summary: A Tier 3 KDE Frameworks 6 module that provides indexing and search functionality
Version: 6.24.0
Release:	6%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND bzip2-1.0.6
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

# Upstream Patches

## upstreamable patches
# http://bugzilla.redhat.com/1235026
Patch100: baloo-5.67.0-baloofile_config.patch

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Solid)

BuildRequires:  lmdb-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel

# for systemd-related macros
BuildRequires:  systemd

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6FileMetaData)
Requires:       qt6-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        file
Summary:        File indexing and search for Baloo
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kf5-baloo-file < 6
%description    file
%{summary}.

%package        libs
Summary:        Runtime libraries for %{name}
%description    libs
%{summary}.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 \
    -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir}
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6

# baloodb not installed unless BUILD_EXPERIMENTAL is enabled, so omit translations
#rm -fv %{buildroot}%{_datadir}/locale/*/LC_MESSAGES/baloodb5.*

%find_lang baloodb6
%find_lang baloo_file6
%find_lang baloo_file_extractor6
%find_lang balooctl6
%find_lang balooengine6
%find_lang baloosearch6
%find_lang balooshow6
%find_lang kio6_baloosearch
%find_lang kio6_tags
%find_lang kio6_timeline

cat kio6_tags.lang kio6_baloosearch.lang kio6_timeline.lang \
    balooctl6.lang balooengine6.lang baloosearch6.lang \
    balooshow6.lang baloodb6.lang \
    > %{name}.lang

cat baloo_file6.lang baloo_file_extractor6.lang \
    > %{name}-file.lang

%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/baloosearch6
%{_kf6_bindir}/balooshow6
%{_kf6_bindir}/balooctl6
%{_kf6_datadir}/qlogging-categories6/%{framework}*

%files file -f %{name}-file.lang
%config(noreplace) %{_kf6_sysconfdir}/xdg/autostart/baloo_file.desktop
%{_userunitdir}/kde-baloo.service
%{_libexecdir}/kf6/baloo_file
%{_libexecdir}/kf6/baloo_file_extractor

%files libs
%license LICENSES/*
%{_kf6_libdir}/libKF6Baloo.so.*
%{_kf6_libdir}/libKF6BalooEngine.so.*
%{_kf6_plugindir}/kio/baloosearch.so
%{_kf6_plugindir}/kio/tags.so
%{_kf6_plugindir}/kio/timeline.so
%{_kf6_plugindir}/kded/baloosearchmodule.so
%{_kf6_qmldir}/org/kde/baloo

%files devel
%{_kf6_libdir}/libKF6Baloo.so
%{_kf6_libdir}/cmake/KF6Baloo/
%{_kf6_libdir}/pkgconfig/KF6Baloo.pc
%{_kf6_includedir}/Baloo/
%{_kf6_datadir}/dbus-1/interfaces/org.kde.baloo.*.xml
%{_kf6_datadir}/dbus-1/interfaces/org.kde.Baloo*.xml


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- inline cmake --build (no qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop Qt6 qdoc -html packaging (kf6 macros skip qt6 prepare_docs pass)

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Qt6 qdoc: -html file list via find, tags/index in -devel

* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Drop -DQDOC_BIN=/bin/true now that qt6-qttools qdoc is patched (QTBUG-142742)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)

