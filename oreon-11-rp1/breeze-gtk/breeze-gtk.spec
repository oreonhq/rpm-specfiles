%global source1_hash b689408c77bc7ac8819004f46fb2acab7b11a3fefe36ef9316a6bcf6f3f3f511
%global stable_kf6 stable
%global source0_hash 4e0e913b0515de75492155d028c086c4a522a3f68ebb6f4fab10f8bc646cd518
Name:    breeze-gtk
Version: 6.7.5
Release:        1%{?dist}
Summary:        Breeze widget theme for GTK
License: BSD-3-Clause AND CC0-1.0
URL:     https://invent.kde.org/plasma/%{name}
Source0:        http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
BuildArch:      noarch
Requires: %{name}-gtk2 = %{version}-%{release}
Requires: %{name}-gtk3 = %{version}-%{release}
Requires: %{name}-gtk4 = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gtk2-engines
BuildRequires:  kf6-rpm-macros
BuildRequires:  plasma-breeze-devel
BuildRequires:  python3-cairo-devel
BuildRequires:  sassc
# /oreon:deps
%description
%{summary}.

%package common
Summary:        Breeze widget theme for GTK common files
Conflicts:      breeze-gtk < 5.20.2-2
%description common
%{summary}.

%package gtk2
Summary:        Breeze widget theme for GTK 2
Requires:       gtk2-engines
Requires:       %{name}-common = %{version}-%{release}
Supplements:    (plasma-breeze and gtk2)
%description gtk2
%{summary}.

%package gtk3
Summary:        Breeze widget theme for GTK 3
Requires:       %{name}-common = %{version}-%{release}
Supplements:    (plasma-breeze and gtk3)
%description gtk3
%{summary}.

%package gtk4
Summary:        Breeze widget theme for GTK 4
Requires:       %{name}-common = %{version}-%{release}
Supplements:    (plasma-breeze and gtk4)
%description gtk4
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles breeze-gtk-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles breeze-gtk-gtk2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles breeze-gtk-gtk3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles breeze-gtk-gtk4 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n breeze-gtk-common -f %{oreon_filedir}/breeze-gtk-common.list
%files -n breeze-gtk-gtk2 -f %{oreon_filedir}/breeze-gtk-gtk2.list
%files -n breeze-gtk-gtk3 -f %{oreon_filedir}/breeze-gtk-gtk3.list
%files -n breeze-gtk-gtk4 -f %{oreon_filedir}/breeze-gtk-gtk4.list

%changelog

%autochangelog
