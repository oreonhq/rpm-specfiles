%global source0_hash cedf2e66f9d2844727bff450b7cd7972c2122a05734a5300a10844a24682bb20

%undefine   __brp_mangle_shebangs

Name:		magic
Version:	8.3.623
Release:	1%{?dist}
Summary:	A very capable VLSI layout tool

# LICENSE: HPND-UC-export-US: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/504
# calma/:  HPND-UC-export-US: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/504
# bplane/bpBins.c and etc: TCL
# drc/DRCcif.c: HPND
# scmos/COPYRIGHT: NPND
# SPDX confirmed
License:	HPND-UC-export-US AND TCL AND HPND
URL:		http://opencircuitdesign.com/%{name}/index.html

Source:	http://opencircuitdesign.com/%{name}/archive/%{name}-%{version}.tgz
%dnl Source:	https://github.com/RTimothyEdwards/magic/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch1:	%{name}-7.4.35-64bit.patch
# https://sourceware.org/pipermail/libc-alpha/2025-March/165574.html
# glibc 2.42 removes termio.h
Patch2:	%{name}-8.3.538-remove-termio.patch

BuildRequires:	make
BuildRequires:	gcc

BuildRequires:	cairo-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel
BuildRequires:	libGLw-devel
BuildRequires:	libXext-devel
BuildRequires:	libXi-devel
BuildRequires:	libXmu-devel
%if 0%{?fedora} >= 44
BuildRequires:	pkgconfig(tk) >= 9
%else
BuildRequires:	pkgconfig(tk) <= 8.999
%endif
BuildRequires:	m4
BuildRequires:	desktop-file-utils
%if 0%{?fedora}
BuildRequires:	zlib-devel
%endif

BuildRequires:	tcsh

Requires:	tcsh
# Special FEL Gnome/KDE menu structure
Requires:	electronics-menu

%description
Magic is a venerable VLSI layout tool. Magic VLSI remains
popular with universities and small companies.

Magic is widely cited as being the easiest tool to use for
circuit layout, even for people who ultimately rely on commercial
tools for their product design flow.

%package doc
Summary:	Documentation for magic, A very capable VLSI layout tool
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains the documentation of magic in the postscript
and some tutorials.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# tarball includes unneeded symlink, so we firstly
# create a directory and expand tarball there.
%setup -q -T -c %{name}-%{version} -a 0
cd %{name}-%{version}

find readline \( -name \*.h -or -name \*.c \) -delete
rm -rf risp

sed -i.cflags -e 's|CFLAGS=.*CFLAGS|:|' configure

sed -i.nocpp \
	scripts/configure.in scripts/configure \
	-e 's|-lstdc++||' \
	%{nil}

sed -i.arch scripts/defs.mak.in \
	-e 's|^INSTALL_LIBDIR.*$|INSTALL_LIBDIR\t=%{_libdir}|'

sed -i "s|/usr/local/bin/tclsh|%{_bindir}/tclsh|" tcltk/strip_reflibs.tcl
sed -i "s|package require -exact|package require|" tcltk/tkcon.tcl

%if "x%{?__isa_bits}" == "x64"
%patch -P 1 -p0 -b .64bit
%endif
%patch -P 2 -p1 -b .glibc_244

#sed -i utils/magsgtty.h -e 's|termio.h|termios.h|'

# Doesn't seem to need these.
sed -i scripts/configure \
	-e 's| -lfontconfig -lfreetype||'

%global __global_cflags_orig %__global_cflags
%global __global_cflags %__global_cflags_orig -Werror=implicit-function-declaration -Werror=implicit-int

# Not C23 compliant yet
%global optflags_orig %optflags
%global optflags %optflags_orig -std=gnu17

%build
cd %{name}-%{version}

%if 0%{?fedora} >= 44
WISH_EXE=$(ls -1d %{_bindir}/wish9.* | tail -n 1)
%else
WISH_EXE=$(ls -1d %{_bindir}/wish8.* | tail -n 1)
%endif
%configure \
	--with-wish=$WISH_EXE \
	--with-tcl=%{_libdir} \
	--with-tk=%{_libdir} \
	--with-tcllibs=%{_libdir} \
	--with-tklibs=%{_libdir} \
	%{nil}

#%make %%{?_smp_mflags}
# Parallel make _silently_ fails
unlink commands/readline || :
make -j1 -k \
    UNUSED_MODULES=""

%install
cd %{name}-%{version}
make install \
	DESTDIR=%{buildroot} \
	INSTALL="%{__install} -c -p" \
	CP="%{__cp} -p"

desktop-file-install \
	--vendor "" \
	--dir %{buildroot}%{_datadir}/applications/ \
	%{SOURCE1}

# applying timestamps
cp -pr \
	README* \
	TODO \
	VERSION \
	scmos/ \
	..

cp -pr %{buildroot}%{_libdir}/%{name}/{doc/,tutorial} ..
rm -rf %{buildroot}%{_libdir}/%{name}/{doc/,tutorial}

rm -f doc/html/Makefile

chmod -x %{buildroot}%{_libdir}/%{name}/tcl/console.tcl

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -cpm 0644 %{SOURCE2} \
	%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# Remove manpage currently unused for TCL building
# to avoid file conflict (bug 1330507)
rm -f %{buildroot}%{_mandir}/man1/extcheck.1*

%files
%doc	README*
%doc	TODO
%doc	VERSION
%{_bindir}/%{name}
%{_bindir}/ext2sim
%{_bindir}/ext2spice

%dir	%{_libdir}/%{name}/
%dir	%{_libdir}/%{name}/tcl/
%{_libdir}/%{name}/sys/
%{_libdir}/%{name}/tcl/bitmaps/
%{_libdir}/%{name}/tcl/*tcl
%{_libdir}/%{name}/tcl/*.so
%{_libdir}/%{name}/tcl/magicdnull
%{_libdir}/%{name}/tcl/magicexec

%{_mandir}/man?/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%files doc
%doc	doc/
%doc	tutorial/
%doc	scmos/

%changelog
%autochangelog
