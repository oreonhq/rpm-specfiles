%global source0_hash 3eeb013b0c83013bbf984bd77c91c8fb7d14bfc259bfeca2153f708968b36337

Name:		fcitx-fbterm
Version:	0.2.0
Release:	33%{?dist}
Summary:	Fbterm Support for Fcitx
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://code.google.com/p/fcitx/
Source0:	http://fcitx.googlecode.com/files/%{name}-%{version}.tar.xz

BuildRequires:	gcc
BuildRequires:	cmake, fcitx-devel, gettext, intltool, libxml2-devel
BuildRequires:	dbus-glib-devel, pkgconfig
Requires:	fcitx

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

%files
%doc AUTHORS README
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-helper

%changelog
%autochangelog
