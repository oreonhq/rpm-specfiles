%if 0%{?fedora}
%global p7zip 1
%endif


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    ark
Summary: Archive manager
Version: 25.12.3
Release: 1%{?dist}

# icons are LGPL-3.0-only
# code is GPL-2.0-or-later
License: GPL-2.0-or-later AND LGPL-3.0-only
URL:     https://www.kde.org/applications/utilities/ark/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches

## upstream patches

BuildRequires: bzip2-devel
BuildRequires: desktop-file-utils

BuildRequires: extra-cmake-modules >= 5.71
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6BreezeIcons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Pty)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: libappstream-glib
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libzip)
BuildRequires: qt6-qtbase-devel
BuildRequires: zlib-devel

# when split occured
Conflicts: kdeutils-common < 6:4.7.80

# translations moved here
Conflicts: kde-l10n < 17.03

Obsoletes: kdeutils-ark < 6:4.7.80
Provides:  kdeutils-ark = 6:%{version}-%{release}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# Dependencies for archive plugins.
# could split .desktop like okular to support these via
# TryExec=<foo> instead someday -- Rex
Requires: bzip2
Requires: gzip
%if 0%{?p7zip}
Requires: p7zip-plugins
%endif
Requires: unzip
# optional/soft dependencies
%if 0%{?fedora} > 23
Suggests: lha
Recommends: unar
%endif

%description
Ark is a program for managing various archive formats.

Archives can be viewed, extracted, created and modified from within Ark.
The program can handle various formats such as tar, gzip, bzip2, zip,
rar and lha (if appropriate command-line programs are installed).

%package libs
Summary: Runtime libraries for %{name}
# libkerfuffle is BSD-2-Clause, plugins are mix of BSD-2-Clause AND GPL-2.0-or-later
# kerfuffle/qstringtokenizer.* is MIT
License: BSD-2-Clause AND GPL-2.0-or-later AND MIT
Requires: %{name} = %{version}-%{release}
Obsoletes: kdeutils-ark-libs < 6:4.7.80
Provides:  kdeutils-ark-libs = 6:%{version}-%{release}
Provides: ark-part = %{version}-%{release}
Provides: ark-part%{?_isa} = %{version}-%{release}
%description libs
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man

# unpackaged files
rm -fv %{buildroot}%{_kf6_libdir}/libkerfuffle.so


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.ark.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.ark.desktop


%files -f %{name}.lang
%license COPYING*
%{_sysconfdir}/xdg/arkrc
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_bindir}/ark
%{_kf6_datadir}/config.kcfg/ark.kcfg
%{_kf6_metainfodir}/org.kde.ark.appdata.xml
%{_kf6_datadir}/applications/org.kde.ark.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/ark.*
%{_mandir}/man1/ark.1*

%files libs
%{_kf6_libdir}/libkerfuffle.so.*
%{_kf6_plugindir}/parts/arkpart.so
%{_kf6_qtplugindir}/kerfuffle/
%{_kf6_plugindir}/kio_dnd/extracthere.so
%{_kf6_plugindir}/kfileitemaction/compressfileitemaction.so
%{_kf6_plugindir}/kfileitemaction/extractfileitemaction.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
