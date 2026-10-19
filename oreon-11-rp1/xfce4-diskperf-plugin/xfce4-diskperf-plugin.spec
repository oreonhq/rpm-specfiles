%global source0_hash 3833920a3a4a81b3c676c4fab6dd178f4a222d66f316a0783a9149a0153b7fb6
%global _hardened_build 1
%global minorversion 2.8
%global xfceversion 4.16
Name:           xfce4-diskperf-plugin
Version:        2.8.0
Release:        1%{?dist}
Summary:        Disk performance plugin for the Xfce panel
License:        LicenseRef-Callaway-BSD
URL:            http://goodies.xfce.org/panel-plugins/{%name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.xz
Requires:       xfce4-panel >= %{xfceversion}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  xfce4-panel-devel
# /oreon:deps
%description
The DiskPerf plugin displays disk/partition performance (bytes transfered per
second) based on data provided by the kernel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
