%global source0_hash 515eb95d5d2a51b495df01adf56ef0af703c5d344bb49bc2a6390ef57bba027b
%undefine __cmake_in_source_build
Name:           kdesvn
Version:        2.1.0
Release:        1%{?dist}
Summary:        Subversion client for KDE
License:        GPL-2.0-or-later
URL:            https://github.com/KDE/kdesvn
Source0:        http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}-1.tar.xz
# oreon:deps
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake3
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  neon-devel
BuildRequires:  subversion-devel
# /oreon:deps
%description
KDESvn is a frontend to the subversion vcs. In difference to most other
tools it uses the subversion C-Api direct via a c++ wrapper made by Rapid
SVN and doesn't parse the output of the subversion client. So it is a real
client itself instead of a frontend to the command line tool.

It is designed for the K-Desktop environment and uses all of the goodies
it has. It is planned for future that based on the native client some plugins
for konqueror and/or kate will made.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
sed -i -e '/release version="2.0" date="2016-12-10"/d' src/org.kde.kdesvn.appdata.xml
%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-html
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
