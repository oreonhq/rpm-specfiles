%global source0_hash aef1e893477afd200f83e6cdd3907be0d4fa14c074c3b71dc00514855045925e
Name:		xtrlock
URL:		https://salsa.debian.org/debian/xtrlock
Version:	2.18
Release:        2%{?dist}
License:	GPL-3.0-or-later
Summary:        Minimal X display lock program
Source0:        https://salsa.debian.org/debian/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libcap-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
# /oreon:deps
%description
Xtrlock is a very minimal X display lock program. It doesn't
obscure the screen, it is completely idle while the display is locked
and you don't type at it, and it doesn't do funny things to the X
access control lists.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build -f Makefile.noimake CFLAGS="-DSHADOW_PWD=1 -DLIBCAP=1 %{build_cflags}" \
  LDLIBS="-lcap -lX11 -lcrypt"
%install
%make_install install.man -f Makefile.noimake BINDIR=%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
