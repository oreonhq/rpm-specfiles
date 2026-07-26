%global source0_hash a29b86a8ec91d4abc83b420e547da27470847d0efe808aa6e75147aa0adb82f2

Name:           xbindkeys
Version:        1.8.7
Release:        14%{?dist}

Summary:        Binds keys or mouse buttons to shell commands under X
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/xbindkeys/
Source:         http://www.nongnu.org/xbindkeys/xbindkeys-%{version}.tar.gz
Patch1:         xbindkeys-1.8.7-guile-3.0.patch
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  guile30-devel
BuildRequires:  libX11-devel
Requires:       tk

%description
xbindkeys is a program that allows you to launch shell commands
with your keyboard or mouse under X. It links commands to keys
or mouse buttons using a simple configuration file, and is
independent of the window manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
LDFLAGS="-lpthread" %{make_build}

%install
%{make_install}

%files
%license COPYING
%doc AUTHORS INSTALL NEWS README xbindkeysrc*
%attr(0755, root, root) %{_bindir}/xbindkeys*
%attr(0644, root, root) %{_mandir}/man?/*

%changelog
%autochangelog
