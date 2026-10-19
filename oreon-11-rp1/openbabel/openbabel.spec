%global source0_hash e140c25480fe1678d00b9a52462368fa4e7805fba67b12ee496784437f3e239e
%{!?perl_vendorarch:%global perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)}
%global __provides_exclude_from ^(%{perl_vendorarch}/auto|%{python3_sitearch})/.*\\.so$
Name: openbabel
Version: 3.2.1
Release:        1%{?dist}
Summary:        Chemistry software file format converter
License: GPL-2.0-only
URL: https://openbabel.org/
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/%{name}-3-2-1.tar.gz
Source1: obgui.desktop
Source2: openbabel-inchi-license-lgpl-2.1.txt
Patch0: %{name}-perl.patch
Patch1: %{name}-plugindir.patch
Patch2: %{name}-noswig-rubymethod.patch
Patch3: %{name}-ruby19-vendorarch.patch
Patch4: %{name}-disable-tests.patch
Patch5: %{name}-fix-libdir-in-pkgconfig.patch
Patch6: %{name}-disable-tests-s390x.patch
Patch7: %{name}-3.1.1-fix_bug2223.patch
Patch8: %{name}-3.1.1-fix_bug2217.patch
Patch9: %{name}-3.1.1-bug2378.patch
Patch10: %{name}-3.1.1-bug2493.patch
Patch11: %{name}-disable-tests-riscv64.patch
Patch12: 2784.patch
Patch13: %{name}-find_eigen3_5.0.patch
Patch14: %{name}-set_cxx17_standard.patch
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  rapidjson-devel
BuildRequires:  ruby-devel
BuildRequires:  swig
BuildRequires:  wxGTK3-devel
# /oreon:deps
%description
Open Babel is a free, open-source version of the Babel chemistry file
translation program. Open Babel is a project designed to pick up where
Babel left off, as a cross-platform program and library designed to
interconvert between many file formats used in molecular modeling,
computational chemistry, and many related areas.

This package contains the command-line utility, which is intended to
be used as a replacement for the original babel program, to translate
between various chemical file formats as well as a wide variety of
utilities to foster development of other open source scientific
software.

%package devel
Summary: Development tools for programs which will use the Open Babel library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package includes the header files and libraries
necessary for developing programs using the Open Babel library.

%package doc
Summary: Additional documentation for the Open Babel library
BuildArch: noarch
%description doc
This package contains additional documentation for Open Babel.

%package gui
Summary: Chemistry software file format converter - GUI version
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description gui
Open Babel is a free, open-source version of the Babel chemistry file
translation program. Open Babel is a project designed to pick up where
Babel left off, as a cross-platform program and library designed to
interconvert between many file formats used in molecular modeling,
computational chemistry, and many related areas.

This package contains the graphical interface.

%package libs
Summary: Chemistry software file format converter - libraries
%description libs
Open Babel is a free, open-source version of the Babel chemistry file
translation program. Open Babel is a project designed to pick up where
Babel left off, as a cross-platform program and library designed to
interconvert between many file formats used in molecular modeling,
computational chemistry, and many related areas.

This package contains the C++ library, which includes all of the
file-translation code.

%package -n perl-%{name}
Summary: Perl wrapper for the Open Babel library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: perl-devel
BuildRequires: perl-generators
%description -n perl-%{name}
Perl wrapper for the Open Babel library.

%package -n python3-%{name}
Summary: Python wrapper for the Open Babel library
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
%{?python_provide:%python_provide python3-%{name}}
Obsoletes: python2-%{name} < 0:%{version}-%{release}
%description -n python3-%{name}
Python3 wrapper for the Open Babel library.

%package -n ruby-%{name}
Summary: Ruby wrapper for the Open Babel library
Requires: ruby(release)
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
BuildRequires: ruby-devel
%description -n ruby-%{name}
Ruby wrapper for the Open Babel library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%(echo %{version} | tr '.' '-')
%patch -P 0 -p1 -b .perl_path
%patch -P 1 -p1 -b .plugindir
%patch -P 2 -p1 -b .noswig_ruby
%patch -P 3 -p1 -b .ruby_vendor
%ifarch aarch64 %{arm} %{power64} s390x
%patch -P 4 -p1 -b .tests
%endif
%patch -P 5 -p1 -b .s390x
%ifarch s390x
%patch -P 6 -p1 -b .backup
%endif
%patch -P 7 -p1 -b .backup
%patch -P 8 -p1 -b .backup
%patch -P 9 -p1 -b .backup
%patch -P 10 -p1 -b .backup
%ifarch riscv64
%patch -P 11 -p1 -b .riscv64
%endif
%patch -P 12 -p1 -b .backup

cp -p %{SOURCE2} ./inchi-license-lgpl-2.1.txt

# convert to Unix line endings
dos2unix -k \
  data/chemdrawcdx.h \
  include/openbabel/{tautomer.h,math/align.h} \
  src/math/align.cpp \
  test/testsmartssym.py \

magick src/GUI/babel.xpm -transparent white babel.png

# Remove duplicate html files
pushd doc
for man in *.1; do
 html=`basename $man .1`.html
 if [ -f $html ]; then
   rm $html
 fi
done
popd

%build

%cmake \
%if "%{?_lib}" == "lib64"
 %{?_cmake_lib_suffix64} \
%endif
 -Wno-dev \
 -DCMAKE_SKIP_RPATH:BOOL=ON \
 -DBUILD_GUI:BOOL=ON \
 -DPYTHON_BINDINGS:BOOL=ON \
 -DPYTHON_EXECUTABLE=%{__python3} \
 -DPERL_BINDINGS:BOOL=ON \
 -DRUBY_BINDINGS:BOOL=ON \
 -DWITH_MAEPARSER:BOOL=OFF \
 -DWITH_COORDGEN:BOOL=OFF \
 -DOB_PLUGIN_INSTALL_DIR:PATH=%{_lib}/openbabel3 \
 -DOPENBABEL_USE_SYSTEM_INCHI=true \
 -DINCHI_INCLUDE_DIR:PATH=%{_includedir}/inchi \
 -DINCHI_LIBRARY:FILEPATH=%{_libdir}/libinchi.so \
 -DENABLE_VERSIONED_FORMATS=false \
 -DRUN_SWIG=true \
 -DENABLE_TESTS:BOOL=ON \
 -DOPTIMIZE_NATIVE=OFF \
 -DGLIBC_24_COMPATIBLE:BOOL=OFF \
 -DEIGEN3_INCLUDE_DIR:PATH=%(pkgconf --variable=prefix eigen3)/include/eigen3 \
 -DEIGEN3_VERSION:STRING=%(pkgconf --modversion eigen3)
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_libdir}/cmake/openbabel2/*.cmake
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -Dpm644 babel.png %{buildroot}%{_datadir}/pixmaps/babel.png
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/openbabel3.sh <<EOF
BABEL_LIBDIR=%{_libdir}/%{name}3
export BABEL_LIBDIR
BABEL_DATADIR=%{_datadir}/%{name}
export BABEL_DATADIR
EOF
cat > %{buildroot}%{_sysconfdir}/profile.d/openbabel3.csh <<EOF
setenv BABEL_LIBDIR %{_libdir}/%{name}3
setenv BABEL_DATADIR %{_datadir}/%{name}
EOF
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rm -f %{_vpath_builddir}/%{_lib}/openbabel.so
export CTEST_OUTPUT_ON_FAILURE=1
export PYTHONPATH=%{buildroot}%{python3_sitearch}
%ctest -E 'pybindtest_bindings|pybindtest_obconv_writers|test_align_4|test_align_5'
%files -f %{oreon_filedir}/main.list
%files -n openbabel-devel -f %{oreon_filedir}/openbabel-devel.list
%files -n openbabel-doc -f %{oreon_filedir}/openbabel-doc.list
%files -n openbabel-gui -f %{oreon_filedir}/openbabel-gui.list
%files -n openbabel-libs -f %{oreon_filedir}/openbabel-libs.list
%files -n perl-openbabel -f %{oreon_filedir}/perl-openbabel.list
%files -n python3-openbabel -f %{oreon_filedir}/python3-openbabel.list
%files -n ruby-openbabel -f %{oreon_filedir}/ruby-openbabel.list

%changelog

%autochangelog

