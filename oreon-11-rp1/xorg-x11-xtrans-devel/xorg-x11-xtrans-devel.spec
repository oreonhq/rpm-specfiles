%global source0_hash faafea166bf2451a173d9d593352940ec6404145c5d1da5c213423ce4d359e92
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
%global debug_package %{nil}
Summary:        X.Org X11 developmental X transport library
Name: xorg-x11-xtrans-devel
Version: 1.6.0
Release:        1%{?dist}
License: HPND AND HPND-sell-variant AND MIT AND MIT-open-group AND X11
URL: http://www.x.org
BuildArch: noarch
Source0:        https://www.x.org/archive/individual/lib/xtrans-%{version}.tar.xz
Patch1: xtrans-1.0.3-avoid-gethostname.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 developmental X transport library

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n xtrans-%{version}
%patch -P1 -p1 -b .my-name-is-unix

%build

%configure --libdir=%{_datadir} --disable-docs
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-2
- Prepare for Oreon 11 (RP1)
