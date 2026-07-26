%global source0_hash b23c60a7ddd9f6db4dd7f55ac55fcca8a558fa68aaf8fa5cb89e1eaf692f23ed

Name:           krename
Version:        5.0.2
Release:        14%{?dist}
Epoch:          1
Summary:        Powerful batch file renamer
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://invent.kde.org/utilities/krename
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
# Add support for PoDoFo-0.10
Patch0:         https://github.com/KDE/krename/commit/056d614dc2166cd25749caf264b1b4d9d348f4d4.patch
Patch1:         https://github.com/KDE/krename/commit/930e995dbcadc796424d261f75c90e98f02fc0b4.patch
#Support for exiv2 >= 0.28.0
Patch2:         https://invent.kde.org/utilities/krename/-/commit/e7dd767a9a1068ee1fe1502c4d619b57d3b12add.patch

BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5JS)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  taglib-devel
BuildRequires:  exiv2-devel
BuildRequires:  podofo-devel
BuildRequires:  freetype-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
KRename is a very powerfull batch file renamer by KDE. It allows you to easily
rename hundreds or even more files in one go. The filenames can be created by
parts of the original filename, numbering the files or accessing hundreds of
informations about the file, like creation date or Exif informations of an
image.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}.lang
%license COPYING COPYING-CMAKE-SCRIPTS
%doc AUTHORS README.md TODO
%{_bindir}/%{name}
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/kservices5/ServiceMenus/%{name}*.desktop

%changelog
%autochangelog
