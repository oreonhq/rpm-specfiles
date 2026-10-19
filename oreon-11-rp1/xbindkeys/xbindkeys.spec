%global source0_hash a29b86a8ec91d4abc83b420e547da27470847d0efe808aa6e75147aa0adb82f2
Name:           xbindkeys
Version:        1.8.7
Release:        14%{?dist}
Summary:        Binds keys or mouse buttons to shell commands under X
License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/xbindkeys/
Source0:        http://www.nongnu.org/xbindkeys/xbindkeys-%{version}.tar.gz
Patch1:         xbindkeys-1.8.7-guile-3.0.patch
Requires:       tk
# oreon:deps
BuildRequires:  gcc
BuildRequires:  guile30-devel
BuildRequires:  libX11-devel
BuildRequires:  make
# /oreon:deps
%description
xbindkeys is a program that allows you to launch shell commands
with your keyboard or mouse under X. It links commands to keys
or mouse buttons using a simple configuration file, and is
independent of the window manager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
LDFLAGS="-lpthread" %{make_build}
%install
%{make_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
