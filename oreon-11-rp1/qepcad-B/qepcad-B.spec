%global source0_hash 075db8950ef2a6d11f099b85820363f7b4d61f4aff3425cb799d7567dc1254fc

Name:           qepcad-B
Version:        1.74
Release:        12%{?dist}
Summary:        Quantifier elimination tool

License:        ISC
URL:            https://www.usna.edu/Users/cs/wcbrown/qepcad/B/QEPCAD.html
Source:         https://www.usna.edu/Users/cs/wcbrown/qepcad/INSTALL/%{name}.%{version}.tgz
# Don't require users to set the "qe" or "SINGULARPATH" environment variables.
# Not for upstream.
Patch:          %{name}-env.patch
# Add gcc attributes for better efficiency and warnings. Upstream: 20 Nov 2013.
Patch:          %{name}-attr.patch
# Fix use of uninitialized variables. Upstream: 20 Nov 2013.
Patch:          %{name}-uninit.patch
# Fix a non-void function where control can fall off the end. Upstream:
# 20 Nov 2013.
Patch:          %{name}-return.patch
# Fix abstract base classes with non-virtual destructors. Upstream:
# 20 Nov 2013.
Patch:          %{name}-destructor.patch
# Add parentheses to disambiguate mixed boolean operators. Upstream:
# 20 Nov 2013.
Patch:          %{name}-parens.patch
# Fix some mixed signed/unsigned operations. Upstream: 20 Nov 2013.
Patch:          %{name}-signed.patch
# Fix syntactically incorrect expressions. Upstream: 20 Nov 2013.
Patch:          %{name}-syntax.patch
# Remove unused variables and static functions.
Patch:          %{name}-unused.patch
# Tell Singular not to steal the TTY (bz 1257471)
Patch:          %{name}-tty.patch
# Adapt to GCC 6
Patch:          %{name}-gcc6.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(glut)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(xext)
BuildRequires:  saclib-devel

# Subprocesses are spawned to run executables from these packages
Requires:       bash
Requires:       coreutils
Requires:       Singular

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
# FIXME: %%{?_smp_mflags} doesn't work
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
#Install the binaries
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 source/qepcad %{buildroot}%{_bindir}
install -p -m 0755 plot2d/ADJ2D_plot %{buildroot}%{_bindir}
install -p -m 0755 cad2d/cad2d %{buildroot}%{_bindir}

# Install the default settings file
mkdir -p %{buildroot}%{_datadir}/qepcad
sed 's,^#S.*,SINGULAR %{_libdir}/Singular,' default.qepcadrc > \
  %{buildroot}%{_datadir}/qepcad/default.qepcadrc
touch -r default.qepcadrc %{buildroot}%{_datadir}/qepcad/default.qepcadrc

# Install qepcad.help and the expected symbolic links
mkdir -p %{buildroot}%{_datadir}/qepcad/bin
cp -p source/qepcad.help %{buildroot}%{_datadir}/qepcad/bin
ln -s %{_bindir}/ADJ2D_plot %{buildroot}%{_datadir}/qepcad/bin
ln -s %{_bindir}/cad2d %{buildroot}%{_datadir}/qepcad/bin
ln -s %{_bindir}/qepcad %{buildroot}%{_datadir}/qepcad/bin

%files
%doc LOG
%license LICENSE
%{_bindir}/qepcad
%{_bindir}/ADJ2D_plot
%{_bindir}/cad2d
%{_datadir}/qepcad/

%changelog
%autochangelog
