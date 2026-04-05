Name:    keditbookmarks
Summary: Bookmark organizer and editor
Version: 25.12.3
Release:	2%{?dist}

# Documentation is GFDL, rest GPLv2 and GPLv3 (note: NOT any later version)
# Automatically converted from old format: GPLv2 and GPLv3 and GFDL - review is highly recommended.
License: GPL-2.0-only AND GPL-3.0-only AND LicenseRef-Callaway-GFDL
URL:     https://www.kde.org/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Crash)

BuildRequires: cmake(Qt6Core)

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description
keditbookmarks is a bookmark organizer and editor.


%package libs
Summary:       Runtime libraries for %{name}
Requires:      %{name} = %{version}-%{release}
%description libs
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html --with-man

## unpackaged files
rm -fv %{buildroot}%{_kf6_libdir}/libkbookmarkmodel_private.so


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license COPYING*
%{_kf6_bindir}/keditbookmarks
%{_kf6_bindir}/kbookmarkmerger
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/config.kcfg/keditbookmarks.kcfg
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_mandir}/man1/kbookmarkmerger.1*

%files libs
%{_kf6_libdir}/libkbookmarkmodel_private.so.*


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
