%global source0_hash none
%undefine _hardened_build
%global pkg     %{name}
%global pkgname Bigloo
%bcond customgc 1
%global         bundledgc 8.2.2
%bcond customlbt 1
%global         bundlelbt 1.0.20210529
Name:           bigloo
Version:        4.6a%{?patch_ver:.%{patch_ver}}
Release:        1%{?dist}
Summary:        A compiler for the Scheme programming language
License:        GPL-2.0-or-later
URL:            https://www-sop.inria.fr/mimosa/fp/Bigloo
VCS:            git:https://github.com/manuel-serrano/bigloo.git
Source0:        ftp://ftp-sop.inria.fr/indes/fp/%{pkgname}/%{name}-%{version}.tar.gz
Patch:          %{name}-emacs.patch
Patch:          %{name}-stat64.patch
Patch:          %{name}-noreturn.patch
Patch:          %{name}-memread.patch
Patch:          %{name}-lto-type.patch
Patch:          %{name}-test.patch
Patch:          %{name}-callcc.patch
Patch:          %{name}-javac.patch
Patch:          %{name}-java-signum.patch
Patch:          %{name}-gcc15.patch
ExcludeArch:    %{ix86}
%ifarch %{java_arches}
%endif
%if %{with customgc}
%endif
%if %{without customlbt}
%endif
%if %{without customgc}
%endif
Requires:       bigloo-libs%{?_isa} = %{version}-%{release}
Requires:       emacs-filesystem >= %{?_emacs_version}%{!?_emacs_version:0}
%ifarch %{java_arches}
Requires:       javapackages-filesystem
%endif
Requires:       indent
Requires:       gmp-devel%{?_isa}
%if %{without customgc}
Requires:       gc-devel%{?_isa}
%endif
Requires:       gcc
Requires:       glibc-devel%{?_isa}
Requires:       libgcc%{?_isa}
Requires:       libunistring-devel%{?_isa}
Requires:       libuv-devel%{?_isa}
%if %{with customgc}
Provides:       bundled(gc) = %{bundledgc}
%endif
%if %{with customlbt}
Provides:       bundled(libbacktrace) = %{bundlelbt}
%global __provides_exclude libbacktrace.*
%global __requires_exclude libbacktrace.*
%endif
# oreon:deps
BuildRequires:  emacs
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  indent
BuildRequires:  libatomic
BuildRequires:  libtool
BuildRequires:  libunistring-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  texi2html
BuildRequires:  texinfo-tex
BuildRequires:  zip
# /oreon:deps
%description
Bigloo is a Scheme implementation devoted to one goal: enabling a Scheme based
programming style where C(++) is usually required.  Bigloo attempts to make
Scheme practical by offering features usually presented by traditional
programming languages but not offered by Scheme and functional programming.
Bigloo compiles Scheme modules.  It delivers small and fast standalone binary
executables.  Bigloo enables full connections between Scheme and C programs.

%package libs
Summary:        Bigloo runtime libraries
License:        LGPL-2.0-or-later AND LGPL-3.0-or-later AND BSD-3-Clause AND MIT
%description libs
Runtime libraries for Bigloo compiled programs.

%package doc
Summary:        Bigloo documentation
BuildArch:      noarch
%description doc
Documentation for the Bigloo compiler and integrated development environment.

%prep

%autosetup -p0 -n %{name}-%{version}%{?patch_suffix}

%conf
# Remove an example with a dubious license
rm -fr examples/Socket

# encoding fixes
for f in README.md; do
  iconv -f ISO8859-1 -t UTF8 $f | sed 's/=ISO-8859-1/=UTF-8/' > $f.utf8
  touch -r $f $f.utf8
  mv -f $f.utf8 $f
done

# correct examples Makefiles for installation
find examples -name Makefile -exec \
  sed -i 's|include.*Makefile.config|include %{_libdir}/bigloo/%{version}/Makefile.config|g' {} +

# fix missing linkage
%if %{without customgc}
sed -i 's/^extralibs="-lm -lc"/extralibs="-lgc -lm -lc"/' configure
sed -i 's/LDOPTS=\"/&-Wl,--as-needed -lgc /' Makefile.misc
%endif

# Keep generated files for debuginfo
sed -i 's/fcfa-arithmetic/& -rm/' configure
sed -i 's/no-hello/& -rm/' bdb/bdb/Makefile
sed -i 's/-O2/& -rm/' cigloo/Makefile

# Remove warning flags not recognized by gcc
sed -i 's/ -Wno-parentheses-equality//;s/ -Wno-invalid-source-encoding//' \
    autoconf/ccwarning

%build

%define inplace $PWD/inplace
ulimit -s unlimited
export LOCALE="C.utf8"
export CFLAGS="%{build_cflags} -std=gnu17 -D_GNU_SOURCE=1 -fwrapv -fno-strict-aliasing -Wno-unused"
sed -i 's/TLS=thread_local/TLS=_Thread_local/;s/"thread_local"/"_Thread_local"/' autoconf/pthreadlocalstorage
sed -i "s|^CFLAGS.*|& $CFLAGS|" bdb/blib/Makefile
export LDFLAGS="-Wl,-z,relro -Wl,--as-needed"
./configure \
        --prefix=%{_prefix} \
        --bindir=%{_bindir} \
        --libdir=%{_libdir} \
        --mandir=%{_mandir}/man1 \
        --infodir=%{_infodir} \
        --docdir=%{_docdir} \
        --lispdir=%{_emacs_sitelispdir}/bigloo \
%ifarch %{java_arches}
        --jvm=yes \
        --javaprefix=%{_jvmdir}/java/bin \
%else
        --jvm=no \
%endif
%ifarch %{power64} s390x
        --no-c-musttail \
%endif
        --bee=full \
        --customgc=%{?with_customgc:yes}%{!?with_customgc:no} \
        --customlibbacktrace=%{?with_customlbt:yes}%{!?with_customlbt:no} \
        --coflags="$CFLAGS" \
        --cpicflags="-fPIC" \
        --sharedbde=yes \
        --sharedcompiler=yes \
        --native-default-backend \
        --customgmp=no \
        --customlibuv=no \
        --strip=no \
        --configureinfo=yes
sed -i '/^RPATH=/s,\$(DESTDIR).*:,,' Makefile.config
%if %{with customlbt}
sed -i 's/-llibbacktrace/$(LDBUILDOPTS) -lbacktrace/' Makefile.config
%endif
LD_LIBRARY_PATH=$PWD/lib/bigloo/%{version} make
LD_LIBRARY_PATH=$PWD/lib/bigloo/%{version} \
    BIGLOOLIB=%{inplace}%{_libdir}/bigloo/%{version} \
    make DESTDIR=%{inplace} install
LD_LIBRARY_PATH=$PWD/lib/bigloo/%{version} \
    PATH=$PWD/bin:$PATH \
    BIGLOOLIB=%{inplace}%{_libdir}/bigloo/%{version} \
    make compile-bee
chmod -R o+r .
%install
mkdir -p %{buildroot}%{_emacs_sitelispdir}/bigloo
env LD_LIBRARY_PATH=$PWD/lib/bigloo/%{version} %make_install
env LD_LIBRARY_PATH=$PWD/lib/bigloo/%{version} \
    make DESTDIR=%{buildroot} EMACSDIR=%{_emacs_sitelispdir}/bigloo install-bee
make -C manuals DESTDIR=%{buildroot} install-bee
rmdir %{buildroot}%{_libdir}/pkgconfig
chmod 755 %{buildroot}%{_bindir}/*
find %{buildroot}%{_libdir} -name \*.so -exec chmod 755 {} +
%ifarch %{java_arches}
mkdir %{buildroot}%{_javadir}
mv %{buildroot}%{_bindir}/jigloo.class %{buildroot}%{_javadir}
%endif
sed -e 's|^BOOTDIR=.*|BOOTDIR=%{_prefix}|g' \
    -e 's|^BOOTBINDIR=.*|BOOTBINDIR=%{_bindir}|g' \
    -e 's|^BOOTLIBDIR=.*|BOOTLIBDIR=%{_libdir}/bigloo/%{version}|g' \
    -e 's|^BGLBUILDBINDIR=.*|BGLBUILDBINDIR=%{_bindir}|g' \
    -e 's|^BGLBUILDLIBDIR=.*|BGLBUILDLIBDIR=%{_libdir}/bigloo/%{version}|g' \
    -e 's|^\(BIGLOO=.*\)\.sh|\1|' \
    -e 's|^\(BGL.*=.*\)\.sh|\1|' \
    -i %{buildroot}%{_libdir}/bigloo/%{version}/Makefile.config
sed -i 's|\(LIBRARY_PATH=\).*|\1%{_libdir}/bigloo/%{version}:$LD_LIBRARY_PATH|' \
    %{buildroot}%{_bindir}/*.sh
for link in $(find %{buildroot}%{_libdir} -type l); do
    target=$(readlink $link)
    if [[ "$target" =~ "%{buildroot}" ]]; then
        rm $link
	ln -s $(basename $target) $link
    fi
done
rm -fr %{buildroot}%{_infodir}/dir %{buildroot}%{_datadir}/doc
mkdir -p %{buildroot}%{_emacs_sitestartdir}
cat > %{buildroot}%{_emacs_sitestartdir}/bigloo.el <<EOF
(require 'bmacs)
EOF
pushd %{buildroot}%{_emacs_sitelispdir}/bigloo
rm -f bmacs-xemacs.el xemacs-etags.el
%{_emacs_bytecompile} bmacs.el bmacs-config.el bmacs-gnu-emacs.el
popd
%ifnarch %{power64}
%oreon_autofiles bigloo-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bigloo-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

ulimit -s unlimited
export TZ=$(date +%%Z)
NATIVEBACKEND=$(sed -n 's/NATIVEBACKEND=\(.*\)/\1/p' Makefile.config)
JVMBACKEND=$(sed -n 's/JVMBACKEND=\(.*\)/\1/p' Makefile.config)
cd recette
if [ "$NATIVEBACKEND" = yes ]; then
  make recette-static
  ../bin/bglrun.sh ./recette-static
fi
cd -
if [ "$JVMBACKEND" = yes ]; then
  make jvm-test
fi
%endif
%files -f %{oreon_filedir}/main.list
%files -n bigloo-libs -f %{oreon_filedir}/bigloo-libs.list
%files -n bigloo-doc -f %{oreon_filedir}/bigloo-doc.list

%changelog

%autochangelog
