%global source0_hash 376033a2f4e6cf96b89130c12196e1c20ffe99300347593bec233aa472d74891

Name:           multiwatch
Version:        1.0.0
Release:        16%{?dist}
Summary:        Forks and watches multiple instances of a program in the same context
License:        MIT
URL:            https://redmine.lighttpd.net/projects/multiwatch/wiki
Source0:        https://download.lighttpd.net/multiwatch/releases-1.x/multiwatch-%{version}.tar.xz

# https://git.lighttpd.net/lighttpd/multiwatch/commit/bdd50b7910ebfd04f70e39cb688e3a4851505ac4.patch
Patch0:         multiwatch-1.0.0-fix_signal.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  libev-devel

%description
Multiwatch forks multiple instance of one application and keeps them running.
It is made to be used with spawn-fcgi, so all forks share the same fastcgi
socket (no web server restart needed if you increase/decrease the number of
forks), and it is easier than setting up multiple daemontool supervised
instances.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/multiwatch
%{_mandir}/man1/multiwatch.1.*

%changelog
%autochangelog
