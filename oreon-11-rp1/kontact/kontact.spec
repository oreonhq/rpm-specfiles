%global source0_hash 5be086d1e47793f78bbe607fd9e9c171212db8649bb92d9463dd739800e86424
%global stable_kf6 stable
Name:    kontact
Summary:        Personal Information Manager
Version: 26.08.1
Release:        1%{?dist}
License: GPL-2.0-only AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/pim/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: kaddressbook
Requires: kmail
Requires: korganizer
# oreon:deps
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KPim6GrantleeTheme)
BuildRequires:  cmake(KPim6KontactInterface)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6PimCommon)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Kontact is the integrated solution to your personal information management
(PIM) needs. It combines well-known KDE applications like KMail, KOrganizer
and KAddressBook into a single interface to provide easy access to mail,
scheduling, address book and other PIM functionality.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

for f in %{buildroot}%{_kf6_datadir}/applications/*.desktop ; do
  desktop-file-validate $f
done
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n kontact-libs -f %{oreon_filedir}/kontact-libs.list

%changelog

%autochangelog
