%global source0_hash dee5bcc0566ba2dc95b9c3b4cadd5e8b3bb2798a54a2a8d8652708915fe45d50
%global _hardened_build 1
%global minorversion 0.6
%global xfceversion 4.16
Name:           xfce4-mpc-plugin
Version:        0.6.0
Release:        1%{?dist}
Summary:        MPD client for the Xfce panel
License:        ISC
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz
Requires:       xfce4-panel >= %{xfceversion}
# oreon:deps
BuildRequires:  exo-devel
BuildRequires:  gcc-c++
BuildRequires:  libmpd-devel
BuildRequires:  libxfce4ui-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  xfce4-panel-devel
# /oreon:deps
%description
A simple client plugin for MPD, the Music Player Daemon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
