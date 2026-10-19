%global source0_hash 2b80f3149b2de6d1f4f2fcb4fe6515a17eb363b52111bf57b90f37bf6f5e12e1
%global octave_api api-v60
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global builddocs 1
%if %{with flexiblas}
%global blaslib flexiblas
%else
%global blaslib openblas
%endif
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif
%bcond_with blas64
%if 0%{?rcver:1}
%global rctag  -rc%{?rcver}
%global relsuf .rc%{?rcver}
%endif
%global optflags %{optflags}
%global build_ldflags %{build_ldflags} -flto
Name:           octave
Epoch:          6
Version:        11.3.0
Release:        1%{?dist}
Summary:        A high-level language for numerical computations
License:        GPL-3.0-or-later
URL:            http://www.octave.org
Source0:        https://ftp.gnu.org/gnu/octave/octave-%{version}.tar.xz
Source1:        macros.octave
Source2:        xorg.conf
%if !%{builddocs}
Source3:        octave-%{version}-docs.tar.xz
%endif
Patch2:         octave-time.patch
Provides:       octave(api) = %{octave_api}
Provides:       bundled(gnulib)
Provides:       bundled(qterminal)
Provides:       bundled(amos)
Provides:       bundled(blas-xtra)
Provides:       bundled(daspk)
Provides:       bundled(dasrt)
Provides:       bundled(dassl)
Provides:       bundled(faddeeva)
Provides:       bundled(lapack-xtra)
Provides:       bundled(odepack)
Provides:       bundled(ordered-qz)
Provides:       bundled(quadpack)
Provides:       bundled(ranlib)
Provides:       bundled(slatec-err)
Provides:       bundled(slatec-fn)
%if %{with java}
%endif
%if %{with blas64}
%else
%endif
%ifnarch s390 s390x
%endif
Requires:       epstool
Requires:       gnuplot
Requires:       gnuplot-common
Requires:       hdf5 = %{_hdf5_version}
Requires:       hicolor-icon-theme
%if %{with java}
Requires:       java-25-headless
%endif
Requires:       less
%if %{undefined flatpak}
Requires:       info
Requires:       texinfo
Requires:       tex(amssymb.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(listings.sty)
Requires:       tex(lmodern.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(color.sty)
Requires:       tex(epsfig.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
%endif
# oreon:deps
BuildRequires:  GraphicsMagick-c++-devel
BuildRequires:  arpack-devel
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fftw-devel
BuildRequires:  flex
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  ghostscript
BuildRequires:  gl2ps-devel
BuildRequires:  glpk-devel
BuildRequires:  gnuplot
BuildRequires:  gperf
BuildRequires:  hdf5-devel
BuildRequires:  java-25-devel
BuildRequires:  less
BuildRequires:  libX11-devel
BuildRequires:  libappstream-glib
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  llvm-devel
BuildRequires:  lzip
BuildRequires:  make
BuildRequires:  mesa-libGL
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ncurses-devel
BuildRequires:  openblas-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  portaudio-devel
BuildRequires:  qhull-devel
BuildRequires:  qrupdate-devel
BuildRequires:  qscintilla-qt6-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qttools-devel
BuildRequires:  rapidjson-devel
BuildRequires:  readline-devel
BuildRequires:  suitesparse-devel
BuildRequires:  tex(dvips)
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
BuildRequires:  texlive-collection-fontsrecommended
BuildRequires:  xorg-x11-drv-dummy
BuildRequires:  zip
BuildRequires:  zlib-devel
# /oreon:deps
%description
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language. Octave
has extensive tools for solving common numerical linear algebra
problems, finding the roots of nonlinear equations, integrating
ordinary functions, manipulating polynomials, and integrating ordinary
differential and differential-algebraic equations. It is easily
extensible and customizable via user-defined functions written in
Octave's own language, or using dynamically loaded modules written in
C++, C, Fortran, or other languages.

%package devel
Summary:        Development headers and files for Octave
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       gcc-c++
Requires:       gcc-gfortran
Requires:       fftw-devel%{?_isa}
Requires:       hdf5-devel%{?_isa}
Requires:       %{blaslib}-devel%{?_isa}
Requires:       readline-devel%{?_isa}
Requires:       zlib-devel
Requires:       libappstream-glib
%description devel
The octave-devel package contains files needed for developing
applications which use GNU Octave.

%package doc
Summary:        Documentation for Octave
BuildArch:      noarch
%description doc
This package contains documentation for Octave.

%prep

%autosetup -p1 -n %{name}-%{version}%{?rctag}
%if %{with blas64}
sed -i -e 's/OCTAVE_CHECK_LIB(suitesparseconfig,/OCTAVE_CHECK_LIB(suitesparseconfig64,/' configure.ac
%endif

%build

export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export F77=gfortran
%if !%{builddocs}
%global disabledocs --disable-docs
%endif
%if %{with java}
libjvm=$(find %{_jvmdir}/jre/lib -name libjvm.so -printf %h)
export JAVA_HOME=%{java_home}
%endif
export CPPFLAGS=-I%{_includedir}/suitesparse
export CXXFLAGS="$(echo %optflags | sed s/-Wp,-D_GLIBCXX_ASSERTIONS//)"
verstr=$(%{__cxx} --version | head -1)
if [[ "$verstr" == *"GCC"* ]]; then
  CXXFLAGS="$CXXFLAGS -flto=auto"
else
  CXXFLAGS="$CXXFLAGS -flto"
fi
%configure --enable-shared --disable-static \
 --enable-float-truncate \
 %{?disabledocs} \
 --disable-silent-rules \
 --with-blas=%{blaslib}%{?with_blas64:64}  \
%if %{with java}
 --with-java-includedir=%{_jvmdir}/java/include \
 --with-java-libdir=$libjvm \
%endif
 --with-qrupdate \
 --with-amd --with-umfpack --with-colamd --with-ccolamd --with-cholmod \
 --with-cxsparse
make liboctave/version.h
if ! grep -q '^#define OCTAVE_API_VERSION "%{octave_api}"' liboctave/version.h
then
  echo "octave_api variable in spec does not match liboctave/version.h"
  exit 1
fi
%make_build OCTAVE_RELEASE="Fedora %{version}%{?rctag}-%{release}"
%install
%make_install
make install-data install-html install-info install-pdf DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -ar AUTHORS BUGS ChangeLog examples NEWS README %{buildroot}%{_pkgdocdir}/
cp -a doc/refcard/*.pdf %{buildroot}%{_pkgdocdir}/
%if !%{builddocs}
tar xvf %SOURCE3 -C %{buildroot}
%endif
find %{buildroot}%{_libdir} -name \*.la -delete
rm -f %{buildroot}%{_infodir}/dir
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/octave/%{version}%{?rctag}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/octave-%{_arch}.conf
perl -pi -e "s,%{buildroot},," %{buildroot}%{_libdir}/%{name}/ls-R
perl -pi -e "s,%{buildroot},," %{buildroot}%{_datadir}/%{name}/ls-R
touch %{buildroot}%{_datadir}/%{name}/ls-R
desktop-file-validate %{buildroot}%{_datadir}/applications/org.octave.Octave.desktop
%{?el9:sed -i -e '/url type=/d' %{buildroot}/%{_datadir}/metainfo/org.octave.Octave.metainfo.xml}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.octave.Octave.metainfo.xml
HOST_TYPE=`%{buildroot}%{_bindir}/octave-config -p CANONICAL_HOST_TYPE`
mkdir -p %{buildroot}%{_libdir}/%{name}/site/oct/%{octave_api}/$HOST_TYPE
mkdir -p %{buildroot}%{_libdir}/%{name}/site/oct/$HOST_TYPE
mkdir -p %{buildroot}%{_datadir}/%{name}/packages
mkdir -p %{buildroot}%{_libdir}/%{name}/packages
touch %{buildroot}%{_datadir}/%{name}/octave_packages
for include in octave-config defaults
do
   mv %{buildroot}%{_includedir}/%{name}-%{version}%{?rctag}/%{name}/${include}.h \
      %{buildroot}%{_includedir}/%{name}-%{version}%{?rctag}/%{name}/${include}-%{__isa_bits}.h
   cat > %{buildroot}%{_includedir}/%{name}-%{version}%{?rctag}/%{name}/${include}.h <<EOF
EOF
done
for script in octave-config-%{version}%{?rctag} mkoctfile-%{version}%{?rctag}
do
   mv %{buildroot}%{_bindir}/${script} %{buildroot}%{_libdir}/%{name}/%{version}%{?rctag}/${script}
   cat > %{buildroot}%{_bindir}/${script} <<EOF
ARCH=\$(uname -m)
case \$ARCH in
x86_64 | ia64 | s390x | aarch64 | ppc64 | ppc64le | riscv64) LIB_DIR=%{_libdir}
                       SECONDARY_LIB_DIR=%{_prefix}/lib
                       ;;
* )
                       LIB_DIR=%{_prefix}/lib
                       SECONDARY_LIB_DIR=%{_prefix}/lib64
                       ;;
esac
if [ ! -x \$LIB_DIR/%{name}/%{version}%{?rctag}/${script} ] ; then
  if [ ! -x \$SECONDARY_LIB_DIR/%{name}/%{version}%{?rctag}/${script} ] ; then
    echo "Error: \$LIB_DIR/%{name}/%{version}%{?rctag}/${script} not found"
    if [ -d \$SECONDARY_LIB_DIR ] ; then
      echo "   and \$SECONDARY_LIB_DIR/%{name}/%{version}%{?rctag}/${script} not found"
    fi
    exit 1
  fi
  LIB_DIR=\$SECONDARY_LIB_DIR
fi
exec \$LIB_DIR/%{name}/%{version}%{?rctag}/${script} "\$@"
EOF
   chmod +x %{buildroot}%{_bindir}/${script}
done
sed -i -e '/^# Created by Octave/d' %{buildroot}%{_datadir}/%{name}/%{version}%{?rctag}/etc/doc-cache
mkdir -p %{buildroot}%{macrosdir}
cp -p %SOURCE1 %{buildroot}%{macrosdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

cp %SOURCE2 .
if [ -x /usr/libexec/Xorg ]; then
   Xorg=/usr/libexec/Xorg
else
   Xorg=/usr/libexec/Xorg.bin
fi
$Xorg -noreset +extension GLX +extension RANDR +extension RENDER -logfile ./xorg.log -config ./xorg.conf :99 &
sleep 2
export DISPLAY=:99
export FLEXIBLAS=netlib
%ifarch ppc64le riscv64
make check || :
%else
make check
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n octave-devel -f %{oreon_filedir}/octave-devel.list
%files -n octave-doc -f %{oreon_filedir}/octave-doc.list

%changelog

%autochangelog
