Name:     skanpage
Version:  25.12.3
Release:	2%{?dist}
Summary:  Utility to scan images and multi-page documents
License:  BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only

URL:      https://invent.kde.org/utilities/%{name}
Source0:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## Upstream patches

## Downstream patches
# gcc fails to compile this project with -fopenmp even though it seems unused?
# Patch100: disable-openmp.patch

# https://invent.kde.org/utilities/skanpage/-/commit/9d94de32a3a1a9bb9ead8ae8c06743b2052beef7
# The previous commit made qtwebengine a mandatory requirement :(
ExclusiveArch: %{qt6_qtwebengine_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Pdf)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  cmake(KSaneCore6)
BuildRequires:  cmake(KF6KIO)

BuildRequires:  cmake(Tesseract) >= 4
BuildRequires:  cmake(Leptonica)

Requires: qt6-qtquickcontrols2
Requires: kf6-kirigami
Requires: kquickimageeditor-qt6

Recommends: sane-backends-drivers-scanners


%description
Skanpage is a multi-page scanning application built 
using the libksane library and a QML interface. 
It supports saving to image and PDF files.

%prep
%autosetup -p1

%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.kde.%{name}.appdata.xml


%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.%{name}.desktop
%{_metainfodir}/org.kde.%{name}.appdata.xml

%{_kf6_datadir}/qlogging-categories6/%{name}.categories
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_kf6_datadir}/icons/hicolor/48x48/apps/%{name}.png

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
