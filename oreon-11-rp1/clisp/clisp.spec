%global source0_hash 0e9a636a5e0e2e446eabd734bb4f74fec3945b847c98ddd29c8f6cfc6a0e9339

# Upstream has not made a new release since 2010
%global srcname clisp
%global commit  f66220939ea7d36fd085384afa4a0ec44597d499
%global date    20250504
%global forgeurl https://gitlab.com/gnu-clisp/clisp

# There is a plus on the end for unreleased versions, not for released versions
%global instdir %{name}-%{version}+

# This package uses toplevel ASMs which are incompatible with LTO
%global _lto_cflags %{nil}

%bcond gtk2 %[!(0%{?rhel} > 9)]

Name:		clisp
Summary:	ANSI Common Lisp implementation
Version:	2.49.95

%forgemeta

# The project as a whole is GPL-2.0-or-later.  Exceptions:
# - Some documentation is dual-licensed as GPL-2.0-or-later OR GFDL-1.2-or-later
# - src/gllib is LGPL-2.1-or-later
# - src/socket.d and modules/clx/mit-clx/doc.lisp are HPND
# - src/xthread.d and modules/asdf/asdf.lisp are X11
License:	GPL-2.0-or-later AND (GPL-2.0-or-later OR GFDL-1.2-or-later) AND LGPL-2.1-or-later AND HPND AND X11
Release:	7%{?dist}
URL:		http://www.clisp.org/
VCS:		git:%{forgeurl}.git
Source0:	%{forgesource}
# Upstream dropped this file from the distribution
Source1:	https://gitlab.com/sam-s/clhs/-/raw/master/clhs.el
# Updated translations
Source2:	http://translationproject.org/latest/clisp/sv.po
Source3:	http://translationproject.org/latest/clisp/de.po
# https://sourceforge.net/p/clisp/patches/32/
Patch0:		%{name}-format.patch
# The combination of register and volatile is nonsensical
Patch1:		%{name}-register-volatile.patch
# A test that writes to /dev/pts/0 succeeds or fails apparently at random.
# I can only guess that /dev/pts/0 may or may not be what the test expects.
# Perhaps we are racing with something else that allocates a pty.  Disable
# the test for now.
Patch2:		%{name}-pts-access.patch
# Do not call the deprecated siginterrupt function
Patch3:		%{name}-siginterrupt.patch
# Fix an iconv leak in stream.d
Patch4:		%{name}-iconv-close.patch
# Fix a memory leak in encoding.d
# https://gitlab.com/gnu-clisp/clisp/-/merge_requests/11
Patch5:		%{name}-encoding-leak.patch
# Fix undefined behavior in SORT
Patch6:		%{name}-undefined-behavior-sort.patch
# Fix undefined behavior in interpret_bytecode_
Patch7:		%{name}-undefined-behavior-eval.patch
# Fix undefined behavior in pr_array
Patch8:		%{name}-undefined-behavior-io.patch
# Fix misaligned memory accesses on ppc64le
Patch9:		%{name}-ppc64le-alignment.patch
# Fix some mismatched readline function declarations
# https://gitlab.com/gnu-clisp/clisp/-/merge_requests/13
Patch10:	%{name}-readline.patch

# Work around a problem inlining a function on ppc64le
# See https://bugzilla.redhat.com/show_bug.cgi?id=2049371
Patch100:	%{name}-no-inline.patch

BuildRequires:	dbus-devel
BuildRequires:	diffutils
BuildRequires:	emacs
BuildRequires:	fcgi-devel
BuildRequires:	ffcall-devel
BuildRequires:	gcc
BuildRequires:	gdbm-devel
BuildRequires:	gettext-devel
BuildRequires:	ghostscript
BuildRequires:	glibc-langpack-en
BuildRequires:	glibc-langpack-fr
BuildRequires:	glibc-langpack-ja
BuildRequires:	glibc-langpack-zh
BuildRequires:	groff
%if %{with gtk2}
BuildRequires:	gtk2-devel
BuildRequires:	libglade2-devel
%endif
BuildRequires:	libXaw-devel
BuildRequires:	libXft-devel
BuildRequires:	libdb-devel
BuildRequires:	libsigsegv-devel
BuildRequires:	libsvm-devel
BuildRequires:	libunistring-devel
BuildRequires:	libxcrypt-devel
BuildRequires:	make
BuildRequires:	pari-devel
BuildRequires:	pari-gp
BuildRequires:	libpq-devel
BuildRequires:	readline-devel
BuildRequires:	vim-filesystem
BuildRequires:	zlib-devel

Requires:	emacs-filesystem
Requires:	vim-filesystem

# clisp contains a copy of gnulib, which has been granted a bundling exception:
# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides:	bundled(gnulib)

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
# Do not need to specify base modules: i18n, readline, regexp, syscalls.
# The dirkey module currently can only be built on Windows/Cygwin/MinGW.
# The editor module is not in good enough shape to use.
# The matlab, netica, and oracle modules require proprietary code to build.
# The queens module is intended as an example only, not for actual use.
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
# Workaround libtool reordering -Wl,--as-needed after all the libraries.
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

# Compile the Emacs interface
pushd %{buildroot}%{_emacs_sitelispdir}
%{_emacs_bytecompile} *.el
popd

# Put back the original config.rpath
cp -p config.rpath.orig %{buildroot}%{_libdir}/%{instdir}/build-aux/config.rpath

# Fix a missing executable bit
chmod a+x %{buildroot}%{_libdir}/%{instdir}/build-aux/depcomp

# Fix paths in the Makefiles
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

# Install config.h, which is needed in some cases
for dir in %{buildroot}%{_libdir}/%{instdir}/*; do
  cp -p build/$(basename $dir)/config.h $dir || :
done
cp -p build/config.h %{buildroot}%{_libdir}/%{instdir}
cp -p build/clx/new-clx/config.h \
   %{buildroot}%{_libdir}/%{instdir}/clx/new-clx

# Fix broken symlinks in the full set
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

# Help the debuginfo generator
ln -s ../../src/modules.c build/base/modules.c
ln -s ../../src/modules.c build/full/modules.c

%check
make -C build check
make -C build extracheck
make -C build base-mod-check

%files -f %{name}.lang
%license COPYRIGHT GNU-GPL
%{_bindir}/clisp
%{_mandir}/man1/clisp.1*
%{_pkgdocdir}/
%dir %{_libdir}/%{instdir}/
%dir %{_libdir}/%{instdir}/asdf/
%{_libdir}/%{instdir}/asdf/asdf.fas
%dir %{_libdir}/%{instdir}/base/
%{_libdir}/%{instdir}/base/lispinit.mem
%{_libdir}/%{instdir}/base/lisp.run
%dir %{_libdir}/%{instdir}/berkeley-db/
%{_libdir}/%{instdir}/berkeley-db/*.fas
%{_libdir}/%{instdir}/berkeley-db/preload.lisp
%dir %{_libdir}/%{instdir}/bindings/
%dir %{_libdir}/%{instdir}/bindings/glibc/
%{_libdir}/%{instdir}/bindings/glibc/*.fas
%dir %{_libdir}/%{instdir}/clx/
%dir %{_libdir}/%{instdir}/clx/new-clx/
%{_libdir}/%{instdir}/clx/new-clx/*.fas
%{_libdir}/%{instdir}/clx/new-clx/clx-preload.lisp
%{_libdir}/%{instdir}/data/
%dir %{_libdir}/%{instdir}/dbus/
%{_libdir}/%{instdir}/dbus/*.fas
%{_libdir}/%{instdir}/dynmod/
%dir %{_libdir}/%{instdir}/fastcgi/
%{_libdir}/%{instdir}/fastcgi/*.fas
%dir %{_libdir}/%{instdir}/full/
%{_libdir}/%{instdir}/full/lispinit.mem
%{_libdir}/%{instdir}/full/lisp.run
%dir %{_libdir}/%{instdir}/gdbm/
%{_libdir}/%{instdir}/gdbm/*.fas
%{_libdir}/%{instdir}/gdbm/preload.lisp
%if %{with gtk2}
%dir %{_libdir}/%{instdir}/gtk2/
%{_libdir}/%{instdir}/gtk2/*.fas
%{_libdir}/%{instdir}/gtk2/preload.lisp
%endif
%dir %{_libdir}/%{instdir}/libsvm/
%{_libdir}/%{instdir}/libsvm/*.fas
%{_libdir}/%{instdir}/libsvm/preload.lisp
%dir %{_libdir}/%{instdir}/pari/
%{_libdir}/%{instdir}/pari/*.fas
%{_libdir}/%{instdir}/pari/preload.lisp
%dir %{_libdir}/%{instdir}/postgresql/
%{_libdir}/%{instdir}/postgresql/*.fas
%dir %{_libdir}/%{instdir}/rawsock/
%{_libdir}/%{instdir}/rawsock/*.fas
%{_libdir}/%{instdir}/rawsock/preload.lisp
%dir %{_libdir}/%{instdir}/zlib/
%{_libdir}/%{instdir}/zlib/*.fas
%{_emacs_sitelispdir}/*
%{vimfiles_root}/after/syntax/*

%files devel
%doc modules/clx/clx-manual
%{_bindir}/clisp-link
%{_mandir}/man1/clisp-link.1*
%{_libdir}/%{instdir}/asdf/Makefile
%{_libdir}/%{instdir}/asdf/*.lisp
%{_libdir}/%{instdir}/asdf/*.sh
%{_libdir}/%{instdir}/base/*.a
%{_libdir}/%{instdir}/base/*.h
%{_libdir}/%{instdir}/base/*.o
%{_libdir}/%{instdir}/base/makevars
%{_libdir}/%{instdir}/berkeley-db/Makefile
%{_libdir}/%{instdir}/berkeley-db/*.h
%{_libdir}/%{instdir}/berkeley-db/dbi.lisp
%{_libdir}/%{instdir}/berkeley-db/*.o
%{_libdir}/%{instdir}/berkeley-db/*.sh
%{_libdir}/%{instdir}/bindings/glibc/Makefile
%{_libdir}/%{instdir}/bindings/glibc/*.lisp
%{_libdir}/%{instdir}/bindings/glibc/*.o
%{_libdir}/%{instdir}/bindings/glibc/*.sh
%{_libdir}/%{instdir}/build-aux/
%{_libdir}/%{instdir}/clx/new-clx/demos/
%{_libdir}/%{instdir}/clx/new-clx/README
%{_libdir}/%{instdir}/clx/new-clx/Makefile
%{_libdir}/%{instdir}/clx/new-clx/*.h
%{_libdir}/%{instdir}/clx/new-clx/clx.lisp
%{_libdir}/%{instdir}/clx/new-clx/image.lisp
%{_libdir}/%{instdir}/clx/new-clx/resource.lisp
%{_libdir}/%{instdir}/clx/new-clx/*.o
%{_libdir}/%{instdir}/clx/new-clx/*.sh
%{_libdir}/%{instdir}/config.h
%{_libdir}/%{instdir}/dbus/Makefile
%{_libdir}/%{instdir}/dbus/*.h
%{_libdir}/%{instdir}/dbus/*.lisp
%{_libdir}/%{instdir}/dbus/*.o
%{_libdir}/%{instdir}/dbus/*.sh
%{_libdir}/%{instdir}/fastcgi/README
%{_libdir}/%{instdir}/fastcgi/Makefile
%{_libdir}/%{instdir}/fastcgi/*.h
%{_libdir}/%{instdir}/fastcgi/*.lisp
%{_libdir}/%{instdir}/fastcgi/*.o
%{_libdir}/%{instdir}/fastcgi/*.sh
%{_libdir}/%{instdir}/full/*.a
%{_libdir}/%{instdir}/full/*.h
%{_libdir}/%{instdir}/full/*.o
%{_libdir}/%{instdir}/full/makevars
%{_libdir}/%{instdir}/gdbm/Makefile
%{_libdir}/%{instdir}/gdbm/*.h
%{_libdir}/%{instdir}/gdbm/gdbm.lisp
%{_libdir}/%{instdir}/gdbm/*.o
%{_libdir}/%{instdir}/gdbm/*.sh
%if %{with gtk2}
%{_libdir}/%{instdir}/gtk2/Makefile
%{_libdir}/%{instdir}/gtk2/*.cfg
%{_libdir}/%{instdir}/gtk2/*.glade
%{_libdir}/%{instdir}/gtk2/*.h
%{_libdir}/%{instdir}/gtk2/gtk.lisp
%{_libdir}/%{instdir}/gtk2/*.o
%{_libdir}/%{instdir}/gtk2/*.sh
%endif
%{_libdir}/%{instdir}/libsvm/README
%{_libdir}/%{instdir}/libsvm/Makefile
%{_libdir}/%{instdir}/libsvm/*.h
%{_libdir}/%{instdir}/libsvm/libsvm.lisp
%{_libdir}/%{instdir}/libsvm/*.o
%{_libdir}/%{instdir}/libsvm/*.sh
%{_libdir}/%{instdir}/linkkit/
%{_libdir}/%{instdir}/pari/README
%{_libdir}/%{instdir}/pari/Makefile
%{_libdir}/%{instdir}/pari/*.h
%{_libdir}/%{instdir}/pari/desc2lisp.lisp
%{_libdir}/%{instdir}/pari/pari.lisp
%{_libdir}/%{instdir}/pari/*.o
%{_libdir}/%{instdir}/pari/*.sh
%{_libdir}/%{instdir}/postgresql/README
%{_libdir}/%{instdir}/postgresql/Makefile
%{_libdir}/%{instdir}/postgresql/*.h
%{_libdir}/%{instdir}/postgresql/*.lisp
%{_libdir}/%{instdir}/postgresql/*.o
%{_libdir}/%{instdir}/postgresql/*.sh
%{_libdir}/%{instdir}/rawsock/demos/
%{_libdir}/%{instdir}/rawsock/Makefile
%{_libdir}/%{instdir}/rawsock/*.h
%{_libdir}/%{instdir}/rawsock/sock.lisp
%{_libdir}/%{instdir}/rawsock/*.o
%{_libdir}/%{instdir}/rawsock/*.sh
%{_libdir}/%{instdir}/zlib/Makefile
%{_libdir}/%{instdir}/zlib/*.h
%{_libdir}/%{instdir}/zlib/*.lisp
%{_libdir}/%{instdir}/zlib/*.o
%{_libdir}/%{instdir}/zlib/*.sh
%{_datadir}/aclocal/clisp.m4

%changelog
%autochangelog
