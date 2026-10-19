%global source0_hash 56d26fa0ba325fe2f7d7a95d33491fdcfa7f89dea3127f55732514f90a884ac0
%undefine   __brp_mangle_shebangs
Name:		magic
Version:	8.3.683
Release:        1%{?dist}
Summary:        A very capable VLSI layout tool
License:	HPND-UC-export-US AND TCL AND HPND
URL:		http://opencircuitdesign.com/%{name}/index.html
Source0:        http://opencircuitdesign.com/%{name}/archive/%{name}-%{version}.tgz
%dnl Source:	https://github.com/RTimothyEdwards/magic/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch1:	%{name}-7.4.35-64bit.patch
Patch2:	%{name}-8.3.538-remove-termio.patch
Requires:	tcsh
Requires:	electronics-menu
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libGLw-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  pkgconfig(tk)
BuildRequires:  tcsh
# /oreon:deps
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
WISH_EXE=$(ls -1d %{_bindir}/wish8.* | tail -n 1)
%configure \
	--with-wish=$WISH_EXE \
	--with-tcl=%{_libdir} \
	--with-tk=%{_libdir} \
	--with-tcllibs=%{_libdir} \
	--with-tklibs=%{_libdir} \
	%{nil}
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
rm -f %{buildroot}%{_mandir}/man1/extcheck.1*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n magic-doc -f %{oreon_filedir}/magic-doc.list

%changelog

%autochangelog
