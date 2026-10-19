%global source0_hash 6119cb776a247468df0956bd5d528e27fd6ebb0fb0955439c45cb0a2f317406b
%global debug_package %{nil}
%define apricotsdir %{_datadir}/apricots
Name: apricots
Version:  0.2.9
Release:        4%{?dist}
Summary:        2D air combat game
License: GPL-2.0-only
URL: https://github.com/moggers87/apricots
Source0:        https://github.com/moggers87/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1: apricots.png
Source2: apricots.desktop
ExcludeArch: ppc64le aarch64
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  alure-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openal-soft-devel
# /oreon:deps
%description
It's a game where you fly a little plane around the screen and
shoot things and drop bombs on enemy targets, and it's meant to be quick 
and fun.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

./bootstrap
./configure --prefix=%{_prefix}
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 apricots/data/apricots.cfg %{buildroot}%{_sysconfdir}
rm %{buildroot}%{_datadir}/apricots/apricots.cfg
ln -s ../../..%{_sysconfdir}/apricots.cfg %{buildroot}%{_datadir}/apricots/apricots.cfg
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/24x24/apps
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
