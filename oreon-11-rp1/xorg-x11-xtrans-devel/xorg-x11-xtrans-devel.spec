%global source0_hash faafea166bf2451a173d9d593352940ec6404145c5d1da5c213423ce4d359e92

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# NOTE: This package contains only C source and header files and pkg-config
# *.pc files, and does not contain any ELF binaries or DSOs, so we disable
# debuginfo generation.
%global debug_package %{nil}

Summary: X.Org X11 developmental X transport library
Name: xorg-x11-xtrans-devel
Version: 1.6.0
Release: 2%{?dist}
License: HPND AND HPND-sell-variant AND MIT AND MIT-open-group AND X11
URL: http://www.x.org
BuildArch: noarch

Source0: https://xorg.freedesktop.org/archive/individual/lib/xtrans-%{version}.tar.xz

# Fedora specific patch
Patch1: xtrans-1.0.3-avoid-gethostname.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros

%description
X.Org X11 developmental X transport library

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n xtrans-%{version}
%patch -P1 -p1 -b .my-name-is-unix

%build
# yes, this looks horrible, but it's to get the .pc file in datadir
%configure --libdir=%{_datadir} --disable-docs
# Running 'make' not needed.

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%doc AUTHORS COPYING ChangeLog README.md
%dir %{_includedir}/X11
%dir %{_includedir}/X11/Xtrans
%{_includedir}/X11/Xtrans/Xtrans.c
%{_includedir}/X11/Xtrans/Xtrans.h
%{_includedir}/X11/Xtrans/Xtransint.h
%{_includedir}/X11/Xtrans/Xtranslcl.c
%{_includedir}/X11/Xtrans/Xtranssock.c
%{_includedir}/X11/Xtrans/Xtransutil.c
%{_includedir}/X11/Xtrans/transport.c
%{_datadir}/aclocal/xtrans.m4
%{_datadir}/pkgconfig/xtrans.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-2
- Prepare for Oreon 11 (RP1)
