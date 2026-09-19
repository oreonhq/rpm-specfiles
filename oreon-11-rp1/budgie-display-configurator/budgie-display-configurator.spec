%global source0_hash 745d9e02cbaacffffad4c6efc765478710f33a4bb97a48c5eda7f9cbc122060e

Name: budgie-display-configurator
Version: 0.0.1
Release: 3%{?dist}
Summary: Graphical display configuration tool for Budgie Desktop

License: MPL-2.0
URL:     https://forge.moderndesktop.dev/BuddiesOfBudgie/budgie-display-configurator
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

Requires:      budgie-desktop-services
Requires:      kf6-kirigami%{?_isa}

%description
Graphical display configuration tool for Budgie Desktop

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/org.buddiesofbudgie.DisplayConfig
%{_datadir}/applications/org.buddiesofbudgie.DisplayConfig.desktop

%changelog
%autochangelog
