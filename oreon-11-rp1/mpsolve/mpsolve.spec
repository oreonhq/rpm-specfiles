%global source0_hash none
%global my_octave_pkg_install \
mkdir -p %{buildroot}%{octprefix} \
mkdir -p %{buildroot}%{octarchprefix} \
%octave_cmd pkg("prefix","%{buildroot}%{octprefix}","%{buildroot}%{octarchprefix}");pkg("global_list",fullfile("%{buildroot}%{octshareprefix}","octave_packages"));pkg("install","-nodeps","-verbose",glob("%{_builddir}/%{buildsubdir}/examples/matlab/%{octpkg}-%{version}-*.tar.gz"){1,1});unlink(pkg("global_list")); \
if [ -e %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m ] \
then \
  mv %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m.orig \
fi \
echo "function on_uninstall (desc)" > %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m \
echo "  error ('Can not uninstall %s installed by the redhat package manager', desc.name);" >> %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m \
echo "endfunction" >> %{buildroot}%{octpkgdir}/packinfo/on_uninstall.m \
if [ -e %{_builddir}/%{buildsubdir}/examples/matlab/%{octpkg}-%{version}/*.metainfo.xml ] \
then \
  echo "Found .metainfo.xml appdata file" \
  mkdir -p %{buildroot}/%{_metainfodir} \
  cp -p %{_builddir}/%{buildsubdir}/examples/matlab/%{octpkg}-%{version}/*.metainfo.xml %{buildroot}/%{_metainfodir}/ \
  appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/*.metainfo.xml \
else \
  echo "Did not find a .metainfo.xml appdata file" \
fi \
%{nil}
%global giturl  https://github.com/robol/MPSolve
%global commit  8450a4da8f02be0aefb3b0abaf084584a615e41d
Name:           mpsolve
Version:        3.2.3~beta
Release:        1%{?dist}
Summary:        Multiprecision polynomial solver
License:        GPL-3.0-or-later
URL:            https://numpi.dm.unipi.it/software/mpsolve
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{commit}/%{name}-8450a4d.tar.gz
Patch:          %{name}-lto.patch
ExcludeArch:    %{ix86}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%global _desc %{expand:MPSolve stands for Multiprecision Polynomial SOLVEr.  It aims to provide an
easy to use universal blackbox for solving polynomials and secular equations.
Its features include:
- Arbitrary precision approximation.
- Guaranteed inclusion radii for the results.
- Exploiting of polynomial structures: it can take advantage of sparsity as
  well as coefficients in a particular domain (i.e. integers or rationals).
- It can be specialized for specific classes of polynomials.  As an   example,
  the roots of the Mandelbrot polynomial of degree 2,097,151 were computed in
  about 10 days on a dual Xeon server.}
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  bison
BuildRequires:  doxygen-latex
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gmp-devel
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(octave)
BuildRequires:  python3-devel
BuildRequires:  tex(dvips)
# /oreon:deps
%description
%_desc

This package contains command-line interfaces to %{name}.

%package        libs
Summary:        Multiprecision polynomial solver library
%description    libs
%_desc

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch
%description    doc
%_desc

This package contains developer documentation for %{name}.

%package        devel
Summary:        Headers and library links for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
%description    devel
This package contains header and library links for developing
applications that use %{name}.

%package     -n xmpsolve
Summary:        Qt GUI for mpsolve
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       shared-mime-info%{?_isa}
%description -n xmpsolve
%_desc

This package contains a Qt-based graphical interface to mpsolve.

%package     -n python3-mpsolve
Summary:        Python 3 interface to mpsolve
BuildArch:      noarch
Requires:       %{name}-libs = %{version}-%{release}
%description -n python3-mpsolve
%_desc

This package contains a python 3 interface to mpsolve.

%global octpkg  %{name}

%package     -n octave-mpsolve
Summary:        Octave interface to mpsolve
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       octave(api) = %{?octave_api}%{!?octave_api:0}
Requires(post): octave
Requires(postun): octave
%description -n octave-mpsolve
%_desc

This package contains an octave interface to mpsolve.

%prep

%autosetup -n MPSolve-%{commit} -p1

%conf
# Fix the version number in the octave interface
sed -i 's/3\.1\.7/%{version}/' examples/octave/DESCRIPTION
cp -p examples/octave/DESCRIPTION examples/matlab

# Octave wants the COPYING file
cp -p COPYING examples/matlab

# We do not need both HTML and PDF documentation
sed -i '/GENERATE_LATEX/s/YES/NO/' doc/Doxyfile.in

# Doxygen wants the CSS file up one level
cp -p doc/doxygen/doxygen.css doc

# Do not force use of -fomit-frame-pointer
sed -i '/-fomit-frame-pointer/d' configure.ac

# Generate the configure script
autoreconf -fi .

%build

%configure --disable-static --disable-debug --enable-qml-ui LIBS=-lpthread
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
export GS_OPTIONS=-dNOSAFER
%make_build
cd examples/matlab
mkdir -p MPSolve-%{version}/src
mkoctfile -I../../include -c -o mps_interp.o mps_interp.c
mkoctfile -I../../include -c -o mps_kostlan.o mps_kostlan.c
mkoctfile -I../../include -c -o mps_option_parser.o mps_option_parser.c
mkoctfile -I../../include -c -o mps_roots_double.o mps_roots_double.c
mkoctfile -I../../include -c -o mps_roots_string.o mps_roots_string.c
mkoctfile -o MPSolve-%{version}/src/mps_interp.oct -L../../src/libmps/.libs mps_interp.o -lmps -lmpfr
mkoctfile -o MPSolve-%{version}/src/mps_kostlan.oct -L../../src/libmps/.libs mps_kostlan.o -lmps
mkoctfile -o MPSolve-%{version}/src/mps_option_parser.oct -L../../src/libmps/.libs mps_option_parser.o -lmps
mkoctfile -o MPSolve-%{version}/src/mps_roots_double.oct -L../../src/libmps/.libs mps_roots_double.o -lmps
mkoctfile -o MPSolve-%{version}/src/mps_roots_string.oct -L../../src/libmps/.libs mps_roots_string.o -lmps
cp -p *.m MPSolve-%{version}/src
cp -p COPYING DESCRIPTION MPSolve-%{version}
tar cf mpsolve-%{version}-any-none.tar MPSolve-%{version}
gzip -9v mpsolve-%{version}-any-none.tar
cd -
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/192x192/apps
mv %{buildroot}%{_datadir}/icons/xmpsolve.png \
   %{buildroot}%{_datadir}/icons/hicolor/192x192/apps
for sz in 16 22 24 32 36 48 64 72 96 128 256; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps
  magick src/xmpsolve/xmpsolve.png -resize ${sz}x${sz} \
    %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/xmpsolve.png
done
%my_octave_pkg_install
%oreon_autofiles xmpsolve usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-mpsolve usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles octave-mpsolve usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%post        -n octave-mpsolve

%octave_cmd pkg rebuild
%preun       -n octave-mpsolve

%octave_pkg_preun
%postun      -n octave-mpsolve

%octave_cmd pkg rebuild
%files -f %{oreon_filedir}/main.list
%files -n mpsolve-libs -f %{oreon_filedir}/mpsolve-libs.list
%files -n mpsolve-doc -f %{oreon_filedir}/mpsolve-doc.list
%files -n mpsolve-devel -f %{oreon_filedir}/mpsolve-devel.list
%files -n xmpsolve -f %{oreon_filedir}/xmpsolve.list
%files -n python3-mpsolve -f %{oreon_filedir}/python3-mpsolve.list
%files -n octave-mpsolve -f %{oreon_filedir}/octave-mpsolve.list

%changelog

%autochangelog
