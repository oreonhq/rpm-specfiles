%global source0_hash c61127347184d18f9541e322c30de4a3202d545b34962e4d0215f3fc1e845d32
%undefine __cmake_in_source_build
%global _changelog_trimtime %(date +%s -d "1 year ago")
Summary:        KDE Photo Album
Name:	 kphotoalbum
Version: 6.2.0
Release:        1%{?dist}
License: (GPL-2.0-only OR GPL-3.0-only) AND LicenseRef-Callaway-GFDL
URL:	 http://kphotoalbum.org/
Source0:        https://download.kde.org/stable/kphotoalbum/%{version}/kphotoalbum-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(KDcrawQt6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Marble)
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(exiv2)
# /oreon:deps
%description
A photo album tool. Focuses on three key points:
  * It must be easy to describe a number of images at a time. 
  * It must be easy to search for images. 
  * It must be easy to browse and View the images.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-html
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kphotoalbum.*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kphotoalbum.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kphotoalbum-import.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kphotoalbum.open-raw.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
