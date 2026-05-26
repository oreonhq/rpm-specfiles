%global pkgname util-macros
%global debug_package %{nil}

Summary: X.Org X11 Autotools macros
Name: xorg-x11-util-macros
Version: 1.20.2
Release: 4%{?dist}
License: HPND-sell-variant AND MIT
URL: http://www.x.org
BuildArch: noarch
Source0:  https://www.x.org/pub/individual/util/util-macros-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 9ac269eba24f672d7d7b3574e4be5f333d13f04a7712303b1821b2a51ac82e8e
%global source0_file util-macros-1.20.2.tar.xz
# oreon url source checksums end

BuildRequires: make

Requires: autoconf automake pkgconfig

%description
X.Org X11 autotools macros required for building the various packages that
comprise the X Window System.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/util-macros-1.20.2.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9ac269eba24f672d7d7b3574e4be5f333d13f04a7712303b1821b2a51ac82e8e" || { echo "oreon: Source0 SHA256 mismatch for util-macros-1.20.2.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
