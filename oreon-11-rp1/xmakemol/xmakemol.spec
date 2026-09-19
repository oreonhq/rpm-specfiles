%global source0_hash 9c498221ab839124f86a94b6115bdf66d966f954131b3afbb523b85edf0f8766

Name:           xmakemol
Version:        5.16
Release:        24%{?dist}
Summary:        Program for visualizing atomic and molecular systems
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.nongnu.org/xmakemol/
Source0:        http://savannah.nongnu.org/download/xmakemol/xmakemol-%{version}.tar.gz

# Fix FSF address
Patch0:         xmakemol-5.16-fsf.patch
# Patches from debian
Patch1:         xmakemol-5.16-fix_vectors_on_atoms.patch
Patch2:         xmakemol-5.16-h-bond.patch
Patch3:         xmakemol-5.16-print_torsions.patch
# Fix multiple definition of bbox
Patch4:         xmakemol-5.16-extern.patch
# Fix BZ#1914657, crash about NULL widget class
Patch5:         xmakemol-5.16-widget.patch
# Fix BZ#2261809, initialization of XmString from incompatible pointer type
Patch6:         xmakemol-5.16-pointertype.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libGLw-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXpm-devel
BuildRequires:  libICE-devel
BuildRequires:  zlib-devel
BuildRequires:  motif-devel
BuildRequires:  freeglut-devel

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

%files
%license COPYING
%doc AUTHORS NEWS PROBLEMS README
%{_datadir}/xmakemol/
%{_bindir}/xmakemol
%{_mandir}/man1/xmakemol.1.*
%{_bindir}/xmake_anim.pl

%changelog
%autochangelog
