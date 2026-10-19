%global source0_hash 075db8950ef2a6d11f099b85820363f7b4d61f4aff3425cb799d7567dc1254fc
Name:           qepcad-B
Version:        1.74
Release:        12%{?dist}
Summary:        Quantifier elimination tool
License:        ISC
URL:            https://www.usna.edu/Users/cs/wcbrown/qepcad/B/QEPCAD.html
Source0:        https://www.usna.edu/Users/cs/wcbrown/qepcad/INSTALL/%{name}.%{version}.tgz
Patch:          %{name}-env.patch
Patch:          %{name}-attr.patch
Patch:          %{name}-uninit.patch
Patch:          %{name}-return.patch
Patch:          %{name}-destructor.patch
Patch:          %{name}-parens.patch
Patch:          %{name}-signed.patch
Patch:          %{name}-syntax.patch
Patch:          %{name}-unused.patch
Patch:          %{name}-tty.patch
Patch:          %{name}-gcc6.patch
ExcludeArch:    %{ix86}
Requires:       bash
Requires:       coreutils
Requires:       Singular
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(xext)
BuildRequires:  saclib-devel
# /oreon:deps
%description
QEPCAD is an implementation of quantifier elimination by partial cylindrical
algebraic decomposition due originally to Hoon Hong, and subsequently added on
to by many others.  It is an interactive command-line program written in
C/C++, and based on the SACLIB library.  This is QEPCAD B version 1.x, the "B"
designating a substantial departure from the original QEPCAD and
distinguishing it from any development of the original that may proceed in a
different direction.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n qesource -p0

%conf
# Adapt to the Fedora saclib package
sed -i 's,\${saclib}/lib/saclib.\.a,-lsaclib,' source/Makefile cad2d/Makefile

# Embed the library path
sed -i 's,@LIBDIR@,%{_libdir},' source/main/BEGINQEPCAD.c

# Use the right build flags
sed -i 's|-O4|%{build_cxxflags} -Wno-unused-label %{build_ldflags}|' plot2d/Makefile

%build

export saclib=%{_prefix}
export qe=$PWD
export CCo=g++
export FLAGS='%{build_cxxflags} -I%{_includedir}/saclib -Wno-unused-label'
export FLAGSo="$FLAGS"
export SPECIFLAGS="-I%{_includedir}/saclib"
export SPECLFLAGS='%{build_ldflags}'
make -C extensions/sfext
make -C extensions/adj2d
make -C extensions/rend
make -C extensions/newadj
make -C extensions/lift2D
make -C source opt FLAGSo="$FLAGS"
make -C plot2d
make -C cad2d opt FLAGSo="$FLAGS"
%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 source/qepcad %{buildroot}%{_bindir}
install -p -m 0755 plot2d/ADJ2D_plot %{buildroot}%{_bindir}
install -p -m 0755 cad2d/cad2d %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/qepcad
sed 's,^#S.*,SINGULAR %{_libdir}/Singular,' default.qepcadrc > \
  %{buildroot}%{_datadir}/qepcad/default.qepcadrc
touch -r default.qepcadrc %{buildroot}%{_datadir}/qepcad/default.qepcadrc
mkdir -p %{buildroot}%{_datadir}/qepcad/bin
cp -p source/qepcad.help %{buildroot}%{_datadir}/qepcad/bin
ln -s %{_bindir}/ADJ2D_plot %{buildroot}%{_datadir}/qepcad/bin
ln -s %{_bindir}/cad2d %{buildroot}%{_datadir}/qepcad/bin
ln -s %{_bindir}/qepcad %{buildroot}%{_datadir}/qepcad/bin
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
