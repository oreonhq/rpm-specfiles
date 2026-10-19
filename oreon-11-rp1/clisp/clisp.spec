%global source3_hash 14ba67b8e07f448dd7866cdcbb9ac64a57ac8ca7a9f34c97b5a8f351f5301468
%global source2_hash 5707ad14399a4f39dc4953ee36931a1b3e31e63e20a8b7f28ecaf45c054a8e31
%global source1_hash 601fb7a2fc8c733fe7c7808af80b05a5d50608a1bcff47442c787dcb0152d92c
%global source0_hash 0e9a636a5e0e2e446eabd734bb4f74fec3945b847c98ddd29c8f6cfc6a0e9339
%global srcname clisp
%global commit  f66220939ea7d36fd085384afa4a0ec44597d499
%global date    20250504
%global forgeurl https://gitlab.com/gnu-clisp/clisp
%global instdir %{name}-%{version}+
%global _lto_cflags %{nil}
%bcond gtk2 %[!(0%{?rhel} > 9)]
Name:		clisp
Summary:        ANSI Common Lisp implementation
Version:	2.49.95
%forgemeta
License:	GPL-2.0-or-later AND (GPL-2.0-or-later OR GFDL-1.2-or-later) AND LGPL-2.1-or-later AND HPND AND X11
Release:        7%{?dist}
URL:		http://www.clisp.org/
VCS:		git:%{forgeurl}.git
Source0:        %{forgeurl}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
Source1:	https://gitlab.com/sam-s/clhs/-/raw/master/clhs.el
Source2:	http://translationproject.org/latest/clisp/sv.po
Source3:	http://translationproject.org/latest/clisp/de.po
Patch0:		%{name}-format.patch
Patch1:		%{name}-register-volatile.patch
Patch2:		%{name}-pts-access.patch
Patch3:		%{name}-siginterrupt.patch
Patch4:		%{name}-iconv-close.patch
Patch5:		%{name}-encoding-leak.patch
Patch6:		%{name}-undefined-behavior-sort.patch
Patch7:		%{name}-undefined-behavior-eval.patch
Patch8:		%{name}-undefined-behavior-io.patch
Patch9:		%{name}-ppc64le-alignment.patch
Patch10:	%{name}-readline.patch
Patch100:	%{name}-no-inline.patch
%if %{with gtk2}
%endif
Requires:	emacs-filesystem
Requires:	vim-filesystem
Provides:	bundled(gnulib)
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  diffutils
BuildRequires:  emacs
BuildRequires:  fcgi-devel
BuildRequires:  ffcall-devel
BuildRequires:  gcc
BuildRequires:  gdbm-devel
BuildRequires:  gettext-devel
BuildRequires:  ghostscript
BuildRequires:  glibc-langpack-en
BuildRequires:  glibc-langpack-fr
BuildRequires:  glibc-langpack-ja
BuildRequires:  glibc-langpack-zh
BuildRequires:  groff
BuildRequires:  gtk2-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXft-devel
BuildRequires:  libdb-devel
BuildRequires:  libglade2-devel
BuildRequires:  libpq-devel
BuildRequires:  libsigsegv-devel
BuildRequires:  libsvm-devel
BuildRequires:  libunistring-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  pari-devel
BuildRequires:  pari-gp
BuildRequires:  readline-devel
BuildRequires:  vim-filesystem
BuildRequires:  zlib-devel
# /oreon:deps
%description
ANSI Common Lisp is a high-level, general-purpose programming language.  GNU
CLISP is a Common Lisp implementation by Bruno Haible of Karlsruhe University
and Michael Stoll of Munich University, both in Germany.  It mostly supports
the Lisp described in the ANSI Common Lisp standard.  It runs on most Unix
workstations (GNU/Linux, FreeBSD, NetBSD, OpenBSD, Solaris, Tru64, HP-UX,
BeOS, NeXTstep, IRIX, AIX and others) and on other systems (Windows NT/2000/XP,
Windows 95/98/ME) and needs only 4 MiB of RAM.

It is Free Software and may be distributed under the terms of GNU GPL, while
it is possible to distribute commercial proprietary applications compiled with
GNU CLISP.

The user interface comes in English, German, French, Spanish, Dutch, Russian
and Danish, and can be changed at run time.  GNU CLISP includes an
interpreter, a compiler, a debugger, CLOS, MOP, a foreign language interface,
sockets, i18n, fast bignums and more.  An X11 interface is available through
CLX, Garnet, CLUE/CLIO.  GNU CLISP runs Maxima, ACL2 and many other Common
Lisp packages.

%package devel
Summary:	Development files for CLISP
Provides:	%{name}-static = %{version}-%{release} 
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libsigsegv-devel%{?_isa}
%description devel
Files necessary for linking CLISP programs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%autopatch -M99 -p0
%ifarch %{power64}
%autopatch 100 -p0
%endif

%conf
cp -p %{SOURCE1} emacs
cp -p %{SOURCE2} %{SOURCE3} src/po

# We only link against libraries in system directories, so we need -L dir in
# place of -Wl,-rpath -Wl,dir
cp -p src/build-aux/config.rpath config.rpath.orig
sed -i -e 's/${wl}-rpath ${wl}/-L/g' src/build-aux/config.rpath

# Do not use -Werror, or we get build failures on every new gcc version
sed -i '/CFLAGS -Werror/d' modules/berkeley-db/configure

# Do not override our choice of optimization flags
sed -i "/CFLAGS/s/'-O'/''/;/Z_XCFLAGS/s/' -O'//" src/makemake.in

# When building modules, put -Wl,--as-needed before the libraries to link
sed -i "s/CC='\${CC}'/CC='\${CC} -Wl,--as-needed'/" src/makemake.in

# Enable firefox to be the default browser for displaying documentation
sed -i 's/;; \((setq \*browser\* .*)\)/\1/' src/cfgunix.lisp

# Unpack the CLX manual
tar -C modules/clx -xzf modules/clx/clx-manual.tar.gz
chmod -R go+r modules/clx/clx-manual
chmod a-x modules/clx/clx-manual/html/doc-index.cgi

# On some koji builders, something is already listening on port 9090, which
# causes a spurious test failure.  Change to port 9096 for the test.
sed -i 's/9090/9096/g' tests/socket.tst

%build

./configure --prefix=%{_prefix} \
	    --libdir=%{_libdir} \
	    --mandir=%{_mandir} \
	    --infodir=%{_infodir} \
	    --docdir=%{_pkgdocdir} \
	    --fsstnd=redhat \
	    --with-module=asdf \
	    --with-module=berkeley-db \
	    --with-module=bindings/glibc \
	    --with-module=clx/new-clx \
	    --with-module=dbus \
	    --with-module=fastcgi \
	    --with-module=gdbm \
%if %{with gtk2}
	    --with-module=gtk2 \
%endif
	    --with-module=libsvm \
	    --with-module=pari \
	    --with-module=postgresql \
	    --with-module=rawsock \
	    --with-module=zlib \
	    --with-libreadline-prefix=$PWD/readline \
	    --with-ffcall \
	    --config \
	    build \
	    CPPFLAGS='-I/usr/include/libsvm' \
	    CFLAGS='%{build_cflags} -Wa,--noexecstack' \
	    LDFLAGS='-Wl,--as-needed -Wl,-z,relro -Wl,-z,noexecstack'
cd build
sed -i 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' libtool
make
cd -
%install
make -C build DESTDIR=%{buildroot} install
cp -a build/full %{buildroot}%{_libdir}/%{instdir}
rm -f %{buildroot}%{_pkgdocdir}/doc/clisp.{dvi,1,ps}
rm -f %{buildroot}%{_pkgdocdir}/{COPYRIGHT,GNU-GPL}
cp -p doc/mop-spec.pdf %{buildroot}%{_pkgdocdir}/doc
cp -p doc/*.png %{buildroot}%{_pkgdocdir}/doc
cp -p doc/Why-CLISP* %{buildroot}%{_pkgdocdir}/doc
cp -p doc/regexp.html %{buildroot}%{_pkgdocdir}/doc
find %{buildroot}%{_libdir} -name '*.dvi' -exec rm -f {} \+
%find_lang %{name}
%find_lang %{name}low
cat %{name}low.lang >> %{name}.lang
pushd %{buildroot}%{_emacs_sitelispdir}
%{_emacs_bytecompile} *.el
popd
cp -p config.rpath.orig %{buildroot}%{_libdir}/%{instdir}/build-aux/config.rpath
chmod a+x %{buildroot}%{_libdir}/%{instdir}/build-aux/depcomp
for mk in $(find %{buildroot}%{_libdir} -name Makefile); do
  sed -e "s,$PWD/modules,%{_libdir}/%{instdir}," \
      -e "s,$PWD/build/clisp,%{_bindir}/clisp," \
      -e "s,$PWD/build/linkkit,%{_libdir}/%{instdir}/linkkit," \
      -i $mk
done
for mk in %{buildroot}%{_libdir}/%{instdir}/{base,full}/makevars; do
  sed -e "s, -I$PWD[^']*,," \
      -e "s,%{_libdir}/lib\([[:alnum:]]*\)\.so,-l\1,g" \
      -i $mk
done
for dir in %{buildroot}%{_libdir}/%{instdir}/*; do
  cp -p build/$(basename $dir)/config.h $dir || :
done
cp -p build/config.h %{buildroot}%{_libdir}/%{instdir}
cp -p build/clx/new-clx/config.h \
   %{buildroot}%{_libdir}/%{instdir}/clx/new-clx
pushd %{buildroot}%{_libdir}/%{instdir}/full
for obj in calls gettext readline regexi; do
  rm -f ${obj}.o
  ln -s ../base/${obj}.o ${obj}.o
done
for obj in libgnu libnoreadline lisp; do
  rm -f ${obj}.a
  ln -s ../base/${obj}.a ${obj}.a
done
for obj in fastcgi fastcgi_wrappers; do
  rm -f ${obj}.o
  ln -s ../fastcgi/${obj}.o ${obj}.o
done
for obj in cpari pari; do
  rm -f ${obj}.o
  ln -s ../pari/${obj}.o ${obj}.o
done
rm -f bdb.o
ln -s ../berkeley-db/bdb.o bdb.o
rm -f clx.o
ln -s ../clx/new-clx/clx.o clx.o
rm -f dbus.o
ln -s ../dbus/dbus.o dbus.o
rm -f gdbm.o
ln -s ../gdbm/gdbm.o gdbm.o
%if %{with gtk2}
rm -f gtk.o
ln -s ../gtk2/gtk.o gtk.o
%endif
rm -f libsvm.o
ln -s ../libsvm/libsvm.o libsvm.o
rm -f linux.o
ln -s ../bindings/glibc/linux.o linux.o
rm -f postgresql.o
ln -s ../postgresql/postgresql.o postgresql.o
rm -f rawsock.o
ln -s ../rawsock/rawsock.o rawsock.o
rm -f zlib.o
ln -s ../zlib/zlib.o zlib.o
popd
ln -s ../../src/modules.c build/base/modules.c
ln -s ../../src/modules.c build/full/modules.c
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make -C build check
make -C build extracheck
make -C build base-mod-check
%files -f %{oreon_filedir}/main.list
%files -n clisp-devel -f %{oreon_filedir}/clisp-devel.list

%changelog

%autochangelog
