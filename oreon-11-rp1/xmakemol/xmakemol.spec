%global source0_hash 9c498221ab839124f86a94b6115bdf66d966f954131b3afbb523b85edf0f8766
Name:           xmakemol
Version:        5.16
Release:        1%{?dist}
Summary:        Program for visualizing atomic and molecular systems
License:        GPL-2.0-or-later
URL:            https://www.nongnu.org/xmakemol/
Source0:        http://savannah.nongnu.org/download/xmakemol/xmakemol-%{version}.tar.gz
Patch0:         xmakemol-5.16-fsf.patch
Patch1:         xmakemol-5.16-fix_vectors_on_atoms.patch
Patch2:         xmakemol-5.16-h-bond.patch
Patch3:         xmakemol-5.16-print_torsions.patch
Patch4:         xmakemol-5.16-extern.patch
Patch5:         xmakemol-5.16-widget.patch
Patch6:         xmakemol-5.16-pointertype.patch
# oreon:deps
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  libICE-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXpm-devel
BuildRequires:  make
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libGLw-devel
BuildRequires:  motif-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
XMakemol is a mouse-based program, written using the LessTif widget
set, for viewing and manipulating atomic and other chemical
systems. It reads XYZ input and renders atoms, bonds and hydrogen
bonds.  Features include:
- Animating multiple frame files
- Interactive measurement of bond lengths, bond angles and torsion angles
- Control over atom/bond sizes
- Exporting to Xpm, Encapsulated PostScript and XYZ formats
- Toggling the visibility of groups of atoms
- Editing the positions of subsets of atoms

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -N
%patch -P0 -p1 -b .fsf
%patch -P1 -p0 -b .vecat
%patch -P2 -p1 -b .hbond
%patch -P3 -p1 -b .torsion
%patch -P4 -p1 -b .extern
%patch -P5 -p1 -b .widget
%patch -P6 -p1 -b .pointertype

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
