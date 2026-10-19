%global source0_hash 61aa0e2955e8b5cf321ef14a5fd72f0e953da51a390d456e929b74fc5efcb74a
Name:           chayang
Version:        0.1.0
%global forgeurl https://git.sr.ht/~emersion/chayang
%global tag v%{version}
%forgemeta
Release:        1%{?dist}
Summary:        Gradually dim the screen on wlroots-based compositors
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{tag}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
# /oreon:deps
%description
Gradually dim the screen.
Can be used to implement a grace period before locking the session.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
