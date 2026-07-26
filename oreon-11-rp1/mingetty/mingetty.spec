%global source0_hash 0f55c90ba4faa913d91ef99cbf5cb2eb4dbe2780314c3bb17953f849c8cddd17

Summary:    A compact getty program for virtual consoles only
Name:       mingetty
Version:    1.08
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
Release:    41%{?dist}
URL: http://sourceforge.net/projects/mingetty/
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Bug #635412
Patch1:     mingetty-1.08-check_chroot_chdir_nice.patch
Patch2:     mingetty-1.08-openlog_authpriv.patch
# Bug #551754
Patch3:     mingetty-1.08-limit_tty_length.patch
# Bug #647143
Patch4:     mingetty-1.08-Allow-login-name-up-to-LOGIN_NAME_MAX-length.patch
# Bug #691406
Patch5:     mingetty-1.08-Clear-scroll-back-buffer-on-clear-screen.patch
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make

%description
The mingetty program is a lightweight, minimalist getty program for
use only on virtual consoles.  Mingetty is not suitable for serial
lines (you should use the mgetty program in that case).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
%global _hardened_build 1
make "CFLAGS=-Wall -D_GNU_SOURCE %{__global_cflags}" "LDFLAGS=%{__global_ldflags}"

%install
install -d $RPM_BUILD_ROOT/{sbin,%{_mandir}/man8}
install -m 0755 mingetty $RPM_BUILD_ROOT/sbin/
install -m 0644 mingetty.8 $RPM_BUILD_ROOT/%{_mandir}/man8/

%files
%license COPYING
/sbin/mingetty
%{_mandir}/man8/mingetty.*

%changelog
%autochangelog
