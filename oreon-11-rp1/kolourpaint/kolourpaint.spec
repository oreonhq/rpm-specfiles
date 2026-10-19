%global source0_hash e2ae301feb5e0ccb7634421b7e320808590fcf7c5bf4c4eb3c60d87bd68caca3
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:    kolourpaint
Summary:        An easy-to-use paint program
Version: 26.08.1
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD 
URL:     https://www.kde.org/applications/graphics/kolourpaint/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KSaneWidgets6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
%{summary}.

%package  libs
Summary:  Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
License: LicenseRef-Callaway-LGPLv2
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
rm -fv %{buildroot}%{_libdir}/libkolourpaint_lgpl.so
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n kolourpaint-libs -f %{oreon_filedir}/kolourpaint-libs.list

%changelog

%autochangelog
