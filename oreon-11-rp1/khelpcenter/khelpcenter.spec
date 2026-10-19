%global source0_hash b1101a10cee699cc2cfcebdda2c7fd0d0b444998a50886845ae057acddca6c79
%global stable_kf6 stable
Name:    khelpcenter
Summary:        Show documentation for KDE applications
Epoch:   1
Version: 26.04.3
Release:        1%{?dist}
License: GPL-2.0-only OR GPL-3.0-only
URL:     https://invent.kde.org/system/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
ExclusiveArch: %{qt6_qtwebengine_arches}
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  ffmpeg-free-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libxml2-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  xapian-core-devel
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
install -D -m0644 -t %{buildroot}%{_datadir}/services/ khelpcenter.desktop
install -D -m0644 -t %{buildroot}%{_datadir}/kde4/services/ khelpcenter.desktop
install -D -m0644 -t %{buildroot}%{_datadir}/kservices5/ khelpcenter.desktop
%find_lang %{name} --all-name --with-html
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
