%global source0_hash 0b588ecea9222f5b625d0af0c87ae31daf3cdba1532cf0bbb36f93d6e854849b

Name:           avl
Version:        3.52
Release:        3%{?dist}
Summary:        Aerodynamic and flight-dynamic analysis of rigid aircrafts

# Plotlib is LGPLv2+, the rest is GPLv2+
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            http://web.mit.edu/drela/Public/web/avl/
Source0:        http://web.mit.edu/drela/Public/web/avl/avl%{version}.tgz
# The package does not ship a license file
Source1:        LICENSE.GPL
Source2:        LICENSE.LGPL

BuildRequires:  gcc-gfortran
BuildRequires:  libharu-devel
BuildRequires:  libX11-devel
BuildRequires:  openblas-devel
BuildRequires:  make
Requires:       xorg-x11-fonts-misc

%description
AVL is a program for the aerodynamic and flight-dynamic analysis of rigid aircraft
of arbitrary configuration. It employs an extended vortex lattice model for
the lifting surfaces, together with a slender-body model for fuselages and nacelles.
General nonlinear flight states can be specified. The flight dynamic analysis
combines a full linearization of the aerodynamic model about any flight state,
together with specified mass properties.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n AVL3.52rel09032025
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
%make_build -C plotlib gfortranDP CFLAGS="%{optflags} -DUNDERSCORE -DDBL_ARGS" FFLAGS="%{optflags}"
%make_build -C eispack -f Makefile.gfortran FLG="%{optflags}"
%make_build -C bin FFLAGS="%{optflags}"

%install
install -Dpm 0755 bin/avl %{buildroot}%{_bindir}/avl

%files
%doc version_notes.txt avl_doc*.txt session1.txt session2.txt
%license LICENSE.GPL LICENSE.LGPL
%{_bindir}/avl

%changelog
%autochangelog
