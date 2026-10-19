%global source0_hash 64139546537f280be44be7e0c7b2025cd67ed39b2b4b4235b78b099039ef4673
Name:           progman
Version:        1.1
Release:        1%{?dist}
Summary:        Simple X11 window manager modeled after Program Manager
License:        MIT
URL:            https://github.com/jcs/progman
Source0:        https://github.com/jcs/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  /usr/bin/xxd
BuildRequires:  gcc
BuildRequires:  gdk-pixbuf2-xlib-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXpm-devel
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
progman is a simple X11 window manager modeled after Program Manager from the
Windows 3 era. It is descended from aewm by Decklin Foster and retains its MIT
license.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Do not strip binaries on install so we can get debuginfo
sed -e 's/install -s/install -p/' -i Makefile

%build

%set_build_flags
%make_build
%install
export PREFIX="%{buildroot}%{_prefix}"
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
