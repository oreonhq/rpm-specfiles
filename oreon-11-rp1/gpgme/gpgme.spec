%global source0_hash 821ab0695c842eab51752a81980c92b0410c7eadd04103f791d5d2a526784966
%global source2_hash 7d06690e613cf84f325ba8e9d03070b4426cbc2c0fa73033fda81a57efc5a8ed
%global source4_hash none
%global source5_hash d4796049c06708a26f3096f748ef095347e1a3c1e570561701fe952c3f565382
%global source6_hash 07e1265648ff51da238c9af7a18b3f1dc7b0c66b4f21a72f27c74b396cd3336d

%bcond check 1
# No Qt5 on RHEL 10 and higher
%bcond qt5 %[ 0%{?rhel} < 10 ]
%bcond qt6 1

%global gnupg2_min_ver 2.2.24
%global libgpg_error_min_ver 1.36

# we are doing out of source build
%global _configure ../configure

Name:           gpgme
Summary:        GnuPG Made Easy - high level crypto API
Version:        2.0.1
%global spversion 2.0.0
Release:        4%{?dist}

# MIT: src/cJSON.{c,h} (used by gpgme-json)
License:        LGPL-2.1-or-later AND MIT
URL:            https://gnupg.org/related_software/gpgme/
Source0:        https://gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2.sig
Source2:        gpgme-multilib.h
Source3:        https://gnupg.org/signature_key.asc
Source4:        https://www.gnupg.org/ftp/gcrypt/qgpgme/qgpgme-%{spversion}.tar.xz
Source5:        https://gnupg.org/ftp/gcrypt/gpgmepp/gpgmepp-%{spversion}.tar.xz
Source6:        https://gnupg.org/ftp/gcrypt/gpgmepy/gpgmepy-%{spversion}.tar.bz2
Source7:        https://www.gnupg.org/ftp/gcrypt/qgpgme/qgpgme-%{spversion}.tar.xz.sig
Source8:        https://gnupg.org/ftp/gcrypt/gpgmepp/gpgmepp-%{spversion}.tar.xz.sig
Source9:        https://gnupg.org/ftp/gcrypt/gpgmepy/gpgmepy-%{spversion}.tar.bz2.sig

## downstream patches
# Don't add extra libs/cflags in gpgme-config/cmake equivalent
Patch1001:        0001-don-t-add-extra-libraries-for-linking.patch
# add -D_FILE_OFFSET_BITS... to gpgme-config, upstreamable
Patch1002:        gpgme-1.3.2-largefile.patch
# Allow extra options to be passed to setup.py during installation
#Patch1004:      0002-setup_py_extra_opts.patch

## temporary downstream fixes
# Skip lang/qt/tests/t-remarks on gnupg 2.4+
Patch3001:        1001-qt-skip-test-remarks-for-gnupg2-2.4.patch

# prevent soname .so.15 conflict for qgpgme with compat-qgpgme124-qt{5,6}
Patch3002:        gpgme-2.0.1-soname2.patch

# for qgpgme <= 2.0.0, rhbz#2464335
# https://github.com/gpg/gpgmeqt/commit/150b23c105f3ea7034e6f106e60686aea4e4a13e
Patch3003:        qgpgme-2.0-fixdnparsing.patch

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gawk
BuildRequires:  texinfo
BuildRequires:  gnupg2 >= %{gnupg2_min_ver}
BuildRequires:  gnupg2-smime
BuildRequires:  libgpg-error-devel >= %{libgpg_error_min_ver}
BuildRequires:  libassuan-devel >= 2.4.2

# to remove RPATH
BuildRequires:  chrpath

# For AutoReq cmake-filesystem
BuildRequires:  cmake

Requires:       gnupg2 >= %{gnupg2_min_ver}

# On the following architectures workaround multiarch conflict of -devel packages:
%define multilib_arches %{ix86} x86_64 ia64 ppc ppc64 s390 s390x %{sparc}

%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libgpg-error-devel%{?_isa} >= %{libgpg_error_min_ver}

%description devel
%{summary}.

%package -n %{name}pp
Summary:        C++ bindings/wrapper for GPGME
Obsoletes:      gpgme-pp < 1.8.0-7
Provides:       gpgme-pp = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       gpgme-pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n %{name}pp
%{summary}.

%package -n %{name}pp-devel
Summary:        Development libraries and header files for %{name}-pp
Obsoletes:      gpgme-pp-devel < 1.8.0-7
Provides:       gpgme-pp-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       gpgme-pp-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-devel%{?_isa}

%description -n %{name}pp-devel
%{summary}

%if %{with qt5}
%package -n q%{name}-qt5
Summary:        Qt5 API bindings/wrapper for GPGME
Requires:       %{name}pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
Obsoletes:      q%{name} < 1.20.0
Provides:       q%{name}

%description -n q%{name}-qt5
%{summary}.
%endif

%if %{with qt6}
%package -n q%{name}-qt6
Summary:        Qt6 API bindings/wrapper for GPGME
Requires:       %{name}pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Test)

%description -n q%{name}-qt6
%{summary}.
%endif

%if %{with qt5} || %{with qt6}
%package -n q%{name}-common-devel
Summary:        Common development header files for %{name}-qt5 and %{name}-qt6
Requires:       %{name}pp-devel%{?_isa}

%description -n q%{name}-common-devel
%{summary}.
%endif

%if %{with qt5}
%package -n q%{name}-qt5-devel
Summary:        Development libraries and header files for %{name}-qt5
# before libqgpgme.so symlink was moved to avoid conflict
Conflicts:      kdepimlibs-devel < 4.14.10-17
Requires:       q%{name}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       q%{name}-common-devel%{?_isa}
Obsoletes:      q%{name}-devel < 1.20.0
Provides:       q%{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       q%{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n q%{name}-qt5-devel
%{summary}.
%endif

%if %{with qt6}
%package -n q%{name}-qt6-devel
Summary:        Development libraries and header files for %{name}-qt6
Requires:       q%{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       q%{name}-common-devel%{?_isa}

%description -n q%{name}-qt6-devel
%{summary}.
%endif

%package -n python3-gpg
Summary:        %{name} bindings for Python 3
BuildRequires:  python3-devel
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      platform-python-gpg < %{version}-%{release}

%description -n python3-gpg
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
test "%{source5_hash}" = "none" || { f="%{SOURCE5}"; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source5_hash}" || { echo "oreon: Source5 hash mismatch" >&2; exit 1; }; }
test "%{source6_hash}" = "none" || { f="%{SOURCE6}"; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source6_hash}" || { echo "oreon: Source6 hash mismatch" >&2; exit 1; }; }
%autosetup -N -p1 -S gendiff -n gpgme-2.0.1
# verify sources
gpg2 --import --import-options import-export,import-minimal %{SOURCE3} > ./gpg-keyring.gpg
gpgv2 --keyring ./gpg-keyring.gpg %{SOURCE1} %{SOURCE0}
gpgv2 --keyring ./gpg-keyring.gpg %{SOURCE7} %{SOURCE4}
gpgv2 --keyring ./gpg-keyring.gpg %{SOURCE8} %{SOURCE5}
# pub key of gpgmepy signature not published yet
# gpgv2 --keyring ./gpg-keyring.gpg %%{SOURCE9} %%{SOURCE6}

# constant and predictable names for scripts and patches
mkdir gpgmepp qgpgme gpgmepy
tar --xz -xf %{SOURCE4} --directory=qgpgme --strip-components=1
tar --xz -xf %{SOURCE5} --directory=gpgmepp --strip-components=1
tar --bzip2 -xf %{SOURCE6} --directory=gpgmepy --strip-components=1

%autopatch -p1 

## HACK ALERT
# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g' src/gpgme-config.in

# The build machinery does not support the newest Pythons
sed -i 's/3.13/%{python3_version}/g' configure

%generate_buildrequires
cd gpgmepy
%pyproject_buildrequires

%build
# People neeed to learn that you can't run autogen.sh anymore
#./autogen.sh

# Since 1.16.0, we need to explicitly pass -D_LARGEFILE_SOURCE and
# -D_FILE_OFFSET_BITS=64 for the QT binding to build successfully on 32-bit
# platforms.
export CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I$(pwd)/src -L$(pwd)/build/src/.libs/"
export CXXFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -I$(pwd)/src -L$(pwd)/build/src/.libs/"
# Explicit new lines in C(XX)FLAGS can break naive build scripts
export CFLAGS="$(echo ${CFLAGS} | tr '\n\\' '  ')"
export CXXFLAGS="$(echo ${CXXFLAGS} | tr '\n\\' '  ')"
export SETUPTOOLS_USE_DISTUTILS=local
#export PYTHON=%%{python3}
#export PYTHON_VERSION=%%{python3_version}

GPGME_TOPDIR=$(pwd)
mkdir build
cd build
%configure --disable-static --disable-silent-rules --enable-languages=
%make_build


# for bindings to find this build while not yet installed
export CMAKE_INCLUDE_PATH=$GPGME_TOPDIR/src/
export CMAKE_LIBRARY_PATH=$GPGME_TOPDIR/build/src/.libs/
export PKG_CONFIG_PATH=$GPGME_TOPDIR/build/src/
GPGME_INC_DIR=$GPGME_TOPDIR/src/
GPGME_LIB_DIR=$GPGME_TOPDIR/build/src/.libs/

# build python bindings gpgmepy
cd $GPGME_TOPDIR/gpgmepy
ln -s ../build/src/gpgme.h gpgme.h
cp ../build/src/gpgme-config .
echo "libs=\"-L$GPGME_TOPDIR/build/src/.libs/ $(./gpgme-config --libs)\"" | sed -i '/^libs="/r /dev/stdin' gpgme-config
GPGME_CONFIG=$GPGME_TOPDIR/gpgmepy ./configure
mv src gpg
%pyproject_wheel


# build c++ bindings gpgmepp
cd $GPGME_TOPDIR/gpgmepp
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DENALE_SHARED=yes -DENABLE_STATIC=no -DGpgme_INCLUDE_DIR=$GPGME_TOPDIR/build/src -DGpgme_LIBRARIES='-L$(GPGME_LIB_DIR) -lgpgme' -DGpgme_VERSION=%{version}
%cmake_build
#temp install for qgpgme
DESTDIR=$GPGME_TOPDIR/gpgmepp/buildroot/ cmake --install redhat-linux-build/

# build qt5/6 bindings qgpgme
cd $GPGME_TOPDIR/qgpgme
export CMAKE_APPBUNDLE_PATH=$GPGME_TOPDIR/gpgmepp/buildroot%{_libdir}/cmake/

%if %{with qt5}
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DENALE_SHARED=yes -DENABLE_STATIC=no -DGpgme_INCLUDE_DIR=$GPGME_TOPDIR/build/src -DGpgme_LIBRARIES='-L$(GPGME_LIB_DIR) -lgpgme' -DGpgme_VERSION=%{version}  -DBUILD_WITH_QT5=ON -DBUILD_WITH_QT6=OFF
%cmake_build
mv redhat-linux-build build-qt5
%endif

%if %{with qt6}
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DENALE_SHARED=yes -DENABLE_STATIC=no -DGpgme_INCLUDE_DIR=$GPGME_TOPDIR/build/src -DGpgme_LIBRARIES='-L$(GPGME_LIB_DIR) -lgpgme' -DGpgme_VERSION=%{version}  -DBUILD_WITH_QT5=OFF -DBUILD_WITH_QT6=ON
%cmake_build
mv redhat-linux-build build-qt6
%endif


%install
GPGME_TOPDIR=$(pwd)

# When using distutils from setuptools 60+, ./setup.py install use
# the .egg format. This forces setuptools to use .egg-info format.
# SETUP_PY_EXTRA_OPTS is introduced by the Patch1004 above.
export SETUPTOOLS_USE_DISTUTILS=local
export SETUP_PY_EXTRA_OPTS="--single-version-externally-managed --root=/"
# Also install either qt5 or qt6
cd build
%make_install

# install gpgmepy
cd $GPGME_TOPDIR/gpgmepy
%pyproject_install

# install gpgmepp
cd $GPGME_TOPDIR/gpgmepp
%cmake_install


# install qgpgme for qt5 and qt6
%if %{with qt5}
cd $GPGME_TOPDIR/qgpgme
rm -f redhat-linux-build
ln -s build-qt5 redhat-linux-build
%cmake_install
%endif 

%if %{with qt6}
cd $GPGME_TOPDIR/qgpgme
rm -f redhat-linux-build
ln -s build-qt6 redhat-linux-build
%cmake_install
%endif 

# unpackaged files
rm -fv %{buildroot}%{_infodir}/dir
rm -fv %{buildroot}%{_libdir}/lib*.la

# Hack to resolve multiarch conflict (#341351)
%ifarch %{multilib_arches}
mv %{buildroot}%{_bindir}/gpgme-config{,.%{_target_cpu}}
cat > gpgme-config-multilib.sh <<__END__
#!/bin/sh
exec %{_bindir}/gpgme-config.\$(arch) \$@
__END__
install -D -p gpgme-config-multilib.sh %{buildroot}%{_bindir}/gpgme-config
mv %{buildroot}%{_includedir}/gpgme.h \
   %{buildroot}%{_includedir}/gpgme-%{__isa_bits}.h
install -m644 -p -D %{SOURCE2} %{buildroot}%{_includedir}/gpgme.h
%endif
chrpath -d %{buildroot}%{_bindir}/%{name}-tool
chrpath -d %{buildroot}%{_bindir}/%{name}-json
chrpath -d %{buildroot}%{_bindir}/gnupg-key-manage
chrpath -d %{buildroot}%{_libdir}/lib%{name}pp.so*
# qt5
%if %{with qt5}
chrpath -d %{buildroot}%{_libdir}/libq%{name}.so*
%endif
# qt6
%if %{with qt6}
chrpath -d %{buildroot}%{_libdir}/libq%{name}qt6.so*
%endif

# autofoo installs useless stuff for uninstall
rm -vf %{buildroot}%{python2_sitelib}/gpg/install_files.txt
rm -vf %{buildroot}%{python3_sitelib}/gpg/install_files.txt

%if %{with check}
%check
pushd build
make check
popd
%endif

%files
%license COPYING* LICENSES
%doc AUTHORS NEWS README*
%{_bindir}/%{name}-json
%{_bindir}/gnupg-key-manage
%{_libdir}/lib%{name}.so.45*
%{_mandir}/man1/%{name}-json.*

%files devel
%{_bindir}/%{name}-config
%{_bindir}/%{name}-tool
%ifarch %{multilib_arches}
%{_bindir}/%{name}-config.%{_target_cpu}
%{_includedir}/%{name}-%{__isa_bits}.h
%endif
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_datadir}/aclocal/%{name}.m4
%{_infodir}/%{name}.info*
%{_libdir}/pkgconfig/%{name}*.pc

%files -n %{name}pp
%doc gpgmepp/README
%{_libdir}/lib%{name}pp.so.7*

%files -n %{name}pp-devel
%{_includedir}/%{name}++/
%{_libdir}/lib%{name}pp.so
%{_libdir}/cmake/Gpgmepp/

%if %{with qt5}
%files -n q%{name}-qt5
%doc qgpgme/README
%{_libdir}/libq%{name}.so.15*
%endif

%if %{with qt6}
%files -n q%{name}-qt6
%{_libdir}/libq%{name}qt6.so.15*
%endif

%if %{with qt5} || %{with qt6}
%files -n q%{name}-common-devel
%endif

%if %{with qt5}
%files -n q%{name}-qt5-devel
%{_includedir}/q%{name}-qt5/
%{_libdir}/libq%{name}.so
%{_libdir}/cmake/QGpgme/
%endif

%if %{with qt6}
%files -n q%{name}-qt6-devel
%{_includedir}/q%{name}-qt6/
%{_libdir}/libq%{name}qt6.so
%{_libdir}/cmake/QGpgmeQt6/
%endif

%files -n python3-gpg
%doc gpgmepy/README
%{python3_sitearch}/gpg-*.dist-info/
%{python3_sitearch}/gpg/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.1-4
- Import
