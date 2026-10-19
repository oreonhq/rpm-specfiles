%global source0_hash e8a68f2c86f99e34c86acf7325fe6d19c8175935f2521314552dce63be22f164
Name:           multiwatch
Version:        1.0.1
Release:        1%{?dist}
Summary:        Forks and watches multiple instances of a program in the same context
License:        MIT
URL:            https://redmine.lighttpd.net/projects/multiwatch/wiki
Source0:        https://download.lighttpd.net/multiwatch/releases-1.x/multiwatch-%{version}.tar.xz
Patch0:         multiwatch-1.0.0-fix_signal.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libev-devel
BuildRequires:  make
# /oreon:deps
%description
Multiwatch forks multiple instance of one application and keeps them running.
It is made to be used with spawn-fcgi, so all forks share the same fastcgi
socket (no web server restart needed if you increase/decrease the number of
forks), and it is easier than setting up multiple daemontool supervised
instances.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
