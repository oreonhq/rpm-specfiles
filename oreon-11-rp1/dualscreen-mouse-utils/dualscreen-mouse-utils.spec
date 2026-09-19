%global source0_hash 51c94b382e3b32ea8ccbcb3f2ef8972acc68329aec3c4fcaeaf7f55fda166303

Summary: Utilities for use with dual head setups using independent screens
Name: dualscreen-mouse-utils
Version: 0.5
Release: 35%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL: http://digamma.cs.unm.edu/trac.dmohr/wiki/DualscreenMouseUtils
Source0: http://dsp.mcbf.net/releases/dualscreen-mouse-utils-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: libX11-devel
BuildRequires: make

%description
Utilities for use with old-school dual head setups: namely not
twinview / one big desktop, but rather two X screens.

mouse-switchscreen:
  Change the mouse cursor from one screen to the other. Remembers the previous
  mouse position for each screen.

mouse-wrapscreen:
  If you have an xorg.conf where both X screens are "separated" on the X
  coordinates, then the mouse cursor cannot cross. Which is sometimes desired,
  and sometimes not. Using mouse-wrapscreen you can configure them to be
  "uncrossable", and then run it in the background when you do want to be able
  to cross the cursor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -m 755 mouse-wrapscreen mouse-switchscreen %{buildroot}%{_bindir}/

%files 
%doc gpl.txt README
%{_bindir}/*

%changelog
%autochangelog
