%global source0_hash 92bd496e8fcc2e891fa2e871b35575198af72838717bc07221678461ea92b469
Name:          group-service
Version:       1.4.0
Release:        1%{?dist}
Summary:        Dbus Group management CLI tool
License:       GPL-3.0-or-later 
URL:           https://github.com/zhuyaliang/%{name}
Source0:        https://github.com/zhuyaliang/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%{?systemd_requires}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(systemd)
BuildRequires:  polkit-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Dbus Group management CLI tool

%package devel
Summary:  Support for developing back-ends for group-service
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains libraries and header files needed for
group-service back-ends development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post group-admin-daemon.service
%preun

%systemd_preun group-admin-daemon.service
%postun

%systemd_postun group-admin-daemon.service
%files -f %{oreon_filedir}/main.list
%files -n group-service-devel -f %{oreon_filedir}/group-service-devel.list

%changelog

%autochangelog
