%global source0_hash 09ef8da0cfc6cd8e41b87306ed41a74fcbcf8b65ac98781f95f0d0ac4f97f658

%global commit 56b0c4d9eb3fdf8829fee3c46ccd442c5348eacb
%global shortcommit %(c=%{commit}; echo ${c:0:8})
Name:           kookbook
Version:        0.2.1^20240530.56b0c4d9
Release:        5%{?dist}
Summary:        Cookbook creator

License:        MIT
URL:            https://apps.kde.org/kookbook
Source:         https://invent.kde.org/utilities/%{name}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires: cups-devel
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: qt6-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Test)

Requires: %{name}-extras = %{version}-%{release}

%description
Simple application viewer based on markdown formatted recipes.

%package extras
Summary:    Shared additional files for Kookbook
Requires:   hicolor-icon-theme
BuildArch:  noarch

%description extras
Files used by Kookbook packages.

%package touch
Summary:    Cookbook creator for touch screens
Requires:   %{name}-extras = %{version}-%{release}

%description touch
Touch screen optimized application viewer for markdown formatted
recipes.

%package krecipes-convert
Summary:    Convert krecipes files to kookbook format
Requires:   %{name}-extras = %{version}-%{release}
BuildArch:  noarch

%description krecipes-convert
Example program showing how to convert krecipes files to
kookbook markdown format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install

mv %{buildroot}%{_kf6_datadir}/applications/%{name}touch.desktop \
   %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}touch.desktop

# Installed as documentation
rm %{buildroot}/%{_datadir}/%{name}/doc/krecipes.py

%check
%ctest --verbose --output-on-failure
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}touch.desktop

 
%files
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files extras
%license COPYING
%doc README
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svgz

%files touch
%{_kf6_bindir}/%{name}touch
%{_kf6_datadir}/applications/org.kde.%{name}touch.desktop

%files krecipes-convert
%doc converter/krecipes.py

%changelog
%autochangelog
