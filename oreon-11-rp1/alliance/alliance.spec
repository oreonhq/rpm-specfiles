%global source0_hash 811f201881af46d9d36f1c60b184c136fd2b8bebbe932a29e07ced40394ecc10

%global snapdate 20160506
%global commit d8c05cd022a15586e946da6e5d19d861a489ff5e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           alliance
Version:        5.1.1
Release:        35.%{snapdate}git%{shortcommit}%{?dist}
Summary:        VLSI EDA System
License:        GPL-2.0-only
URL:            https://soc-extras.lip6.fr/en/alliance-abstract-en/
Source:         http://www-asim.lip6.fr/pub/alliance/distribution/latest/alliance-%{version}.tar.bz2
Source1:        alliance.fedora

Source2:       alliance-tutorials-go-all.sh
Source3:       alliance-tutorials-go-all-clean.sh
Source4:       alliance-examples-go-all.sh
Source5:       alliance-examples-go-all-clean.sh

# Update alliance-5.1.1 to commit %%{shortcommit} from
# https://www-soc.lip6.fr/git/alliance.git
Patch00: 0000-alliance-5.1.1-git%{shortcommit}.patch

Patch01: 0001-Remove-stray-files.patch
Patch02: 0002-Update-autostuff.patch
Patch03: 0003-Consolidate-installation-dirs.patch
Patch04: 0004-Misc-installation-dirs-fixes.patch
Patch05: 0005-Use-inttypes-macros-to-print-int32_t.patch
Patch06: 0006-Use-ring_yy-instead-of-yy.patch
Patch07: 0007-Eliminate-CFLAGS.patch
Patch08: 0008-Rework-Makefile.ams.patch
Patch09: 0009-Misc.-doc-fixes.patch
Patch10: 0010-Fedora-profiles.patch
# Bashisms in /etc/profile.d/alc_env.csh
Patch11: 0011-Use-setenv-instead-of-set-RHBZ-1337691.patch
# Flex compatibility issues
Patch12: 0012-Remove-yylineno.patch
# GCC-10 incompatibilities
Patch13: 0013-GCC-10-fixes.patch

BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  libstdc++-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXt-devel
BuildRequires:  m4
BuildRequires:  tex(epsf.sty)
BuildRequires:  tex(latex)
BuildRequires:  tex(picinpar.sty)
BuildRequires:  tex(subfigure.sty)
BuildRequires:  tex(wrapfig.sty)
BuildRequires:  transfig
BuildRequires:  /usr/bin/convert
BuildRequires:  /usr/bin/dvipdf
BuildRequires:  autoconf automake libtool

%if 0%{?rhel}
BuildRequires:  openmotif-devel
BuildRequires:  pkgconfig
%else
BuildRequires:  motif-devel
%endif
Requires:       xorg-x11-fonts-misc
# RHBZ 442379
Requires(post): %{name}-libs%{?_isa} = %{version}-%{release}

%description
Alliance is a complete set of free cad tools and portable libraries for VLSI
design. It includes a vhdl compiler and simulator, logic synthesis tools,
and automatic place and route tools. A complete set of portable cmos libraries
is provided. Alliance is the result of a twelve year effort spent at SoC
department of LIP6 laboratory of the Pierre & Marie Curie University (Paris
VI, France). Alliance has been used for research projects such as the 875 000
transistors StaCS superscalar microprocessor and 400 000 transistors ieee
Gigabit HSL Router.

Alliance provides CAD tools covering most of all the digital design flow:

 * VHDL Compilation and Simulation
 * Model checking and formal proof
 * RTL and Logic synthesis
 * Data-Path compilation
 * Macro-cells generation
 * Place and route
 * Layout edition
 * Netlist extraction and verification
 * Design rules checking

Alliance is listed among Fedora Electronic Lab (FEL) packages.

%package        libs
Summary:        Alliance VLSI CAD System - Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       electronics-menu

%description    libs
Architecture dependent files for the Alliance VLSI CAD Sytem.

%package        devel
Summary:        Alliance VLSI CAD System - Development libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
%{summary}

%package        doc
Summary:        Alliance VLSI CAD System - Documentations
BuildArch:      noarch
Requires:       gnuplot
BuildRequires:  tetex-latex
BuildRequires:  make

%description    doc
Documentation and tutorials for the Alliance VLSI CAD Sytem.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}
%patch -P00 -p2

%patch -P01 -p2
%patch -P02 -p2
%patch -P03 -p2
%patch -P04 -p2
%patch -P05 -p2
%patch -P06 -p2
%patch -P07 -p2
%patch -P08 -p2
%patch -P09 -p2
%patch -P10 -p2
%patch -P11 -p2
%patch -P12 -p2
%patch -P13 -p2

pushd src > /dev/null

# Don't build attila
rm -r attila

# Setup auto*stuff
./autostuff

# The configure.ins confuse rpm
# rename them into configure.in~
sed -i -e 's/configure.in/configure.in~/g' autostuff
for x in $(find */* -name configure.in); do
mv $x $x~
done

chmod +x configure

cp -p %{SOURCE1} .
sed -i "s|ALLIANCE_TOP/bin|%{_libdir}/alliance/bin|" distrib/*.desktop

# ------------------------------------------------------------------------------

## Convert to UTF-8
for nonUTF8 in \
  FAQ \
  alcban/man1/alcbanner.1 \
  distrib/doc/alc_origin.1 \
  loon/doc/loon.1 \
  boog/doc/boog.1 \
  m2e/doc/man1/m2e.1 \
  documentation/overview/overview.tex \
  documentation/alliance-examples/tuner/build_tuner \
  documentation/alliance-examples/tuner/README \
  documentation/alliance-examples/tuner/tuner.vbe \
  documentation/alliance-examples/mipsR3000/sce/mips_dpt.c \
  documentation/alliance-examples/mipsR3000/asm/mips_defs.h \
; do \
  %{_bindir}/iconv -f ISO-8859-1 -t utf-8 $nonUTF8 > $nonUTF8.conv
  mv -f $nonUTF8.conv $nonUTF8
done

pushd documentation/alliance-examples/
#wrong-file-end-of-line-encoding
sed -i 's/\r//' mipsR3000/asm/*
popd

find documentation/tutorials/ \
   \( -name *.vbe  -o \
    -name *.pat  -o \
    -name *.vhdl -o \
    -name *.vst  -o \
    -name *.c \) \
    -exec chmod 0644 {} ';'
popd > /dev/null

%build
# The C parts use implicit ints, implicit function declarations,
# and old-style function declarations heavily.
%global build_type_safety_c 0
export CFLAGS="%build_cflags -std=gnu89"
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
pushd src > /dev/null
%configure --enable-alc-shared             \
           --disable-static                \
           --prefix=%{_libdir}/%{name}     \
           --bindir=%{_libdir}/%{name}/bin \
           --libdir=%{_libdir}/%{name}/lib \
           --includedir=%{_libdir}/%{name}/include \
           --docdir=%{_pkgdocdir} \
           --mandir=%{_mandir}

# Is not parallel-build-safe
make
popd

%install
pushd src > /dev/null
%make_install

# Add automated scripts to examples
#install -pm 755 %{SOURCE4} alliance-examples/go-all.sh
#install -pm 755 %{SOURCE5} alliance-examples/go-all-clean.sh

#pushd alliance-examples/
#    # FEL self test for alliance
#    #./go-all.sh 2>&1 | tee self-test-examples.log
#    # clean temporary files
#    ./go-all-clean.sh
#popd

find %{buildroot} -name '*.la' -delete -print

# Adding icons for the menus
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
cp -p distrib/*.png \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

# desktop files with enhanced menu from electronics-menu now on Fedora
# thanks Peter Brett
for d in distrib/*.desktop; do
desktop-file-install --dir %{buildroot}%{_datadir}/applications/ $d
done

# protecting hardcoded links
#ln -sf ../../..%{_datadir}/%{name}/cells %{buildroot}%{_prefix}/cells
#ln -sf ../../..%{_datadir}/%{name}/etc   %{buildroot}%{_prefix}/etc
#ln -sf ../../..%{_datadir}/%{name}/man   %{buildroot}%{_prefix}/man

# rename manpages to avoid conflicts
# RHBZ 252941
pushd $RPM_BUILD_ROOT%{_mandir} > /dev/null
/usr/bin/rename .1 .1alc man1/*
/usr/bin/rename .3 .3alc man3/*
/usr/bin/rename .5 .5alc man5/*
# Reflect man page renamer to man page includes
sed -i -e 's,^\(.so man[13]/alc_.*.[13]\)$,\1alc,' man*/*
popd > /dev/null

# Rename alliance subdir into html
mv %{buildroot}%{_pkgdocdir}/alliance %{buildroot}%{_pkgdocdir}/html
# Directly install files to go into 5%{_pkgdocdir}
install -m 644 README CHANGES FAQ alliance.fedora %{buildroot}%{_pkgdocdir}

%{__mkdir} -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
cat > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf << EOF
# Alliance VLSI design system
%{_libdir}/%{name}/lib
EOF

%{_fixperms} %{buildroot}/*
popd > /dev/null

%post
source %{_sysconfdir}/profile.d/alc_env.sh

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_pkgdocdir}/README
%{_pkgdocdir}/CHANGES
%{_pkgdocdir}/FAQ
%{_pkgdocdir}/alliance.fedora
%license src/LICENCE src/COPYING*

%{_datadir}/alliance
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/applications/*.desktop
%dir %{_libdir}/alliance
%{_libdir}/alliance/bin
%{_mandir}/man1/*.1*
%config(noreplace) %{_sysconfdir}/alliance
%config(noreplace) %{_sysconfdir}/profile.d/alc_env.*

%files devel
%dir %{_libdir}/alliance
%{_libdir}/alliance/include
%dir %{_libdir}/alliance/lib
%{_libdir}/alliance/lib/*.so
%{_mandir}/man3/*.3*

%files libs
%dir %{_libdir}/alliance
%dir %{_libdir}/alliance/lib
%{_libdir}/alliance/lib/lib*.so.*
%{_mandir}/man5/*.5*
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/*

%files doc
%{_pkgdocdir}

%changelog
%autochangelog
