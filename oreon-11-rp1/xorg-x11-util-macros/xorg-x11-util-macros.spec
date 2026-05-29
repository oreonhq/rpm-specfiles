%global source0_hash 9ac269eba24f672d7d7b3574e4be5f333d13f04a7712303b1821b2a51ac82e8e

%global pkgname util-macros
%global debug_package %{nil}

Summary: X.Org X11 Autotools macros
Name: xorg-x11-util-macros
Version: 1.20.2
Release: 4%{?dist}
License: HPND-sell-variant AND MIT
URL: http://www.x.org
BuildArch: noarch
Source0:        https://www.x.org/pub/individual/util/util-macros-1.20.2.tar.xz

BuildRequires: make

Requires: autoconf automake pkgconfig

%description
X.Org X11 autotools macros required for building the various packages that
comprise the X Window System.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{pkgname}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%files
%doc COPYING ChangeLog
%{_datadir}/aclocal/xorg-macros.m4
%{_datadir}/pkgconfig/xorg-macros.pc
%{_datadir}/util-macros

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.20.2-4
- Prepare for Oreon 11 (RP1)
