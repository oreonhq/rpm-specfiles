Name:    libkcddb 
Version: 25.12.3
Release:	2%{?dist}
Summary: CDDB retrieval library

# Automatically converted from old format: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later - review is highly recommended.
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/multimedia/libkcddb

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6WidgetsAddons)

BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)

BuildRequires: pkgconfig(libmusicbrainz5)

Requires:  %{name}-doc = %{version}-%{release}

# kcmshell5
Recommends:   kde-cli-tools

# when split occured (kdemultimedia to libkcddb)
Conflicts: kdemultimedia-libs < 6:4.8.80
# translations moved here (kf5-libkcddb)
Conflicts: kde-l10n < 17.03
Obsoletes: kf5-libkcddb-kcm < 24.01.85


%description
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# when split occured
Conflicts: kdemultimedia-devel < 6:4.8.80
%description devel
%{summary}.

%package doc
Summary: Documentation for %{name}
# Automatically converted from old format: GFDL - review is highly recommended.
License: LicenseRef-Callaway-GFDL
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
# now ahead of kf5-libkcddb
Conflicts: kf5-libkcddb-doc < 24.01.85
Obsoletes: kf5-libkcddb-doc < 24.01.85
%description doc
Documentation for %{name}.


%prep
%autosetup -p1


%build

%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-man
%find_lang %{name}-doc --all-name --with-html --without-mo

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_libdir}/libKCddb6.so.5*
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_cddb.so
%{_kf6_datadir}/applications/kcm_cddb.desktop
%{_kf6_datadir}/config.kcfg/libkcddb5.kcfg
%{_kf6_datadir}/qlogging-categories6/*

%files devel
%{_kf6_libdir}/libKCddb6.so
%{_includedir}/KCddb6/
%{_kf6_libdir}/cmake/KCddb6/
%{_qt6_archdatadir}/mkspecs/modules/qt_KCddb.pri

%files doc -f %{name}-doc.lang


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
