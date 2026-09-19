%global source0_hash 51c130642abb677e919df84cd5e9f81517f6360306b818afcdac06a4e692cff7

%global commit fd546d82a23f2673c3045b3a4b5685dfd2dd825a
%global gitdate 20260219
%global versuffix ^%{gitdate}git%{sub %{commit} 1 7}

Name:       kbibtex
Version:    0.10.50%{?versuffix}
Release:    1%{?dist}
Summary:    A BibTeX editor for KDE
# CC0-1.0: desktop file, appstream metadata
# BSD-2-Clause is used only in tests
License:    GPL-2.0-or-later AND CC0-1.0
URL:        https://userbase.kde.org/KBibTeX
%if 0%{?commit:1}
Source0:    https://invent.kde.org/office/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0:    http://download.kde.org/stable/KBibTeX/%{version}/%{name}-%{version}.tar.xz
%endif

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
# Qt6
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6NetworkAuth)
%ifarch %{qt6_qtwebengine_arches}
BuildRequires:  cmake(Qt6WebEngineWidgets)
%endif
# KF6
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6WidgetsAddons)
# other deps
BuildRequires:  poppler-qt6-devel
BuildRequires:  libicu-devel
BuildRequires:  shared-mime-info

Requires:       bibutils
Requires:       hicolor-icon-theme

%description
The program KBibTeX is a bibliography editor for KDE. Its main purpose is to
provide a user-friendly interface to BibTeX files.

%package  libs
Summary:  Runtime files for %{name}
%description libs
The program KBibTeX is a bibliography editor for KDE. Its main purpose is to
provide a user-friendly interface to BibTeX files.

This package provides the runtime libraries for %{name}

%package  devel
Summary:  Development files for KBibTeX
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: cmake(KF6Config)
Requires: cmake(KF6I18n)
Requires: cmake(KF6KIO)
Requires: cmake(KF6WidgetsAddons)

%description devel
The %{name}-devel package contains libraries and header files necessary for
developing programs using KBibTeX libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 %{?commit:-n %{name}-%{commit}}

%build
%{cmake_kf6} -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-html --with-man

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%doc README.md ChangeLog
%{_kf6_bindir}/%{name}
%{_kf6_bindir}/%{name}-cli
%{_kf6_plugindir}/parts/%{name}part.so
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/%{name}/
%{_datadir}/mime/packages/bibliography.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/qlogging-categories6/%{name}.categories
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/org.kde.%{name}.appdata.xml

%files libs
%license LICENSES/*.txt
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/KBibTeX/
%{_libdir}/cmake/KBibTeX/
%{_libdir}/lib%{name}*.so

%changelog
%autochangelog
