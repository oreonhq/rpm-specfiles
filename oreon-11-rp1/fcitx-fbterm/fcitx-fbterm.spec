%global source0_hash 3eeb013b0c83013bbf984bd77c91c8fb7d14bfc259bfeca2153f708968b36337
Name:		fcitx-fbterm
Version:	0.2.0
Release:        1%{?dist}
Summary:        Fbterm Support for Fcitx
License:	GPL-2.0-or-later
URL:		http://code.google.com/p/fcitx/
Source0:        http://fcitx.googlecode.com/files/%{name}-%{version}.tar.xz
Requires:	fcitx
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dbus-glib-devel
BuildRequires:  fcitx-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
# /oreon:deps
%description
Fcitx-fbterm is a Wrapper for Fcitx in fbterm,
a fast Framebuffer based terminal emulator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
