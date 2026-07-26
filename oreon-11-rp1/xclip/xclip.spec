%global source0_hash 58d4c08d1e2d71f510a1d21a39e822cd012e8c0e8baf8d5809c26da1ac72df93

%global commit 11cba613840b0d0e76dc2ea6d4ec7cc5f23daf88
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		xclip
Version:	0.13
Release:	26.git%{shortcommit}%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Summary:	Command line clipboard grabber
URL:		http://sourceforge.net/projects/xclip
# Source0:	https://github.com/astrand/xclip/archive/%%{version}.tar.gz
Source0:	https://github.com/astrand/xclip/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:		xclip-fix-segfault-bz1947285.patch
BuildRequires:	make
BuildRequires:	libXmu-devel, libICE-devel, libX11-devel, libXext-devel
BuildRequires:	autoconf, automake, libtool

%description
xclip is a command line utility that is designed to run on any system with an
X11 implementation. It provides an interface to X selections ("the clipboard")
from the command line. It can read data from standard in or a file and place it
in an X selection for pasting into other X applications. xclip can also print
an X selection to standard out, which can then be redirected to a file or
another program.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{commit}
%patch -P0 -p1 -b .1947285
autoreconf -ifv

%build
%configure
make CDEBUGFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man

%files
%license COPYING
%doc README
%{_bindir}/xclip
%{_bindir}/xclip-copyfile
%{_bindir}/xclip-cutfile
%{_bindir}/xclip-pastefile
%{_mandir}/man1/xclip*.1*

%changelog
%autochangelog
