%global source3_hash 6f57d0e17fefd2238bd037aebf03efa960641629dd61dd9d47f122a829f6e375
%global source1_hash 5dd1e3c2e2f9d0e6fca672ddeaf55738d99593e8d9662dba9de6155f48ba9c24
%global source0_hash 7160e80e84dafd00d956c84891c533bb7ab16a6a54fbe1574b2f3acf0496977b
%bcond check 1
%bcond qt5 %[ 0%{?rhel} < 10 ]
%bcond qt6 1
%bcond devel 0
%global gnupg2_min_ver 2.2.24
%global libgpg_error_min_ver 1.36
%global _configure ../configure
%global sname gpgme
Name:           compat-gpgme124
Summary:        GnuPG Made Easy - high level crypto API
Version:        2.2.0
Release:        1%{?dist}
License:        LGPL-2.1-or-later AND MIT
URL:            https://gnupg.org/related_software/gpgme/
Source0:        https://gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/gpgme/gpgme-%{version}.tar.bz2.sig
Source3:        https://gnupg.org/signature_key.asc
Source2:        gpgme-multilib.h
Patch1001:      0001-don-t-add-extra-libraries-for-linking.patch
Patch1002:      gpgme-1.3.2-largefile.patch
Patch1004:      0002-setup_py_extra_opts.patch
Patch3001:      1001-qt-skip-test-remarks-for-gnupg2-2.4.patch
Requires:       gnupg2 >= %{gnupg2_min_ver}
%global multilib_arches %{ix86} x86_64 ia64 ppc ppc64 s390 s390x %{sparc}
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  gnupg2-smime
BuildRequires:  gpgverify
BuildRequires:  libassuan-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  texinfo
# /oreon:deps
%description
GnuPG Made Easy (GPGME) is a library designed to make access to GnuPG
easier for applications.  It provides a high-level crypto API for
encryption, decryption, signing, signature verification and key
management.

%package -n compat-gpgmepp124
Summary:        C++ bindings/wrapper for GPGME
Provides:       gpgme-pp = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       gpgme-pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n compat-gpgmepp124
%{summary}.

%if %{with devel}
%package devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libgpg-error-devel%{?_isa} >= %{libgpg_error_min_ver}
%description devel
%{summary}.

%package -n compat-%{sname}pp124-devel
Summary:        Development libraries and header files for %{name}-pp
Provides:       gpgme-pp-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       gpgme-pp-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}pp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-devel%{?_isa}
%description -n compat-%{sname}pp-devel
%{summary}
%endif

%if %{with qt5}
%package -n compat-q%{sname}124-qt5
Summary:        Qt5 API bindings/wrapper for GPGME
Requires:       compat-%{sname}pp124%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Test)
Obsoletes:      q%{name} < 1.20.0
Provides:       q%{name}
%description -n compat-q%{sname}124-qt5
%{summary}.
%endif

%if %{with qt6}
%package -n compat-q%{sname}124-qt6
Summary:        Qt6 API bindings/wrapper for GPGME
Requires:       compat-%{sname}pp124%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Test)
%description -n compat-q%{sname}124-qt6
%{summary}.
%endif

%if %{with devel}
%if %{with qt5} || %{with qt6}
%package -n compat-q%{sname}124-common-devel
Summary:        Common development header files for %{name}-qt5 and %{name}-qt6
Requires:       compat-%{sname}pp124-devel%{?_isa}
%description -n compat-q%{sname}-common-devel
%{summary}.
%endif

%if %{with qt5}
%package -n q%{name}-qt5-devel
Summary:        Development libraries and header files for %{name}-qt5
Conflicts:      kdepimlibs-devel < 4.14.10-17
Requires:       q%{sname}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       q%{sname}-common-devel%{?_isa}
Obsoletes:      q%{sname}-devel < 1.20.0
Provides:       q%{sname}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       q%{sname}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n compat-q%{sname}124-qt5-devel
%{summary}.
%endif

%if %{with qt6}
%package -n compt-q%{sname}124-qt6-devel
Summary:        Development libraries and header files for %{name}-qt6
Requires:       q%{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       q%{name}-common-devel%{?_isa}
%description -n compat-q%{sname}124-qt6-devel
%{summary}.
%endif
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring=%{SOURCE3} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -n gpgme-%{version} -p1 -S gendiff

## HACK ALERT
# The config script already suppresses the -L if it's /usr/lib, so cheat and
# set it to a value which we know will be suppressed.
sed -i -e 's|^libdir=@libdir@$|libdir=@exec_prefix@/lib|g' src/gpgme-config.in

%build

export CFLAGS='%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
export CXXFLAGS='%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64'
export CFLAGS="$(echo ${CFLAGS} | tr '\n\\' '  ')"
export CXXFLAGS="$(echo ${CXXFLAGS} | tr '\n\\' '  ')"
export SETUPTOOLS_USE_DISTUTILS=local
export ac_cv_prog_cxx_cxx11=''
mkdir build
pushd build
%configure --disable-static --disable-silent-rules --enable-languages=%{?with_qt5:qt,}%{!?with_qt5:%{?with_qt6:qt6,}}cpp
%make_build
popd
%if %{with qt5} && %{with qt6}
mkdir bqt6
pushd bqt6
%configure --disable-static --disable-silent-rules --enable-languages=cpp,qt6
%make_build
popd
%endif
%install
export SETUPTOOLS_USE_DISTUTILS=local
export SETUP_PY_EXTRA_OPTS="--single-version-externally-managed --root=/"
pushd build
%make_install
popd
%if %{with qt5} && %{with qt6}
pushd bqt6
%make_install
popd
%endif
rm -fv %{buildroot}%{_infodir}/dir
rm -fv %{buildroot}%{_libdir}/lib*.la
%ifarch %{multilib_arches}
mv %{buildroot}%{_bindir}/gpgme-config{,.%{_target_cpu}}
cat > gpgme-config-multilib.sh <<__END__
exec %{_bindir}/gpgme-config.\$(arch) \$@
__END__
install -D -p gpgme-config-multilib.sh %{buildroot}%{_bindir}/gpgme-config
mv %{buildroot}%{_includedir}/gpgme.h \
   %{buildroot}%{_includedir}/gpgme-%{__isa_bits}.h
install -m644 -p -D %{SOURCE2} %{buildroot}%{_includedir}/gpgme.h
%endif
chrpath -d %{buildroot}%{_bindir}/%{sname}-tool
chrpath -d %{buildroot}%{_bindir}/%{sname}-json
chrpath -d %{buildroot}%{_libdir}/lib%{sname}pp.so*
%if %{with qt5}
chrpath -d %{buildroot}%{_libdir}/libq%{sname}.so*
%endif
%if %{with qt6}
chrpath -d %{buildroot}%{_libdir}/libq%{sname}qt6.so*
%endif
%if %{without devel}
rm -rf %{buildroot}%{_includedir}
rm -f %{buildroot}%{_libdir}/*.so
rm -rf %{buildroot}%{_libdir}/cmake
rm -rf %{buildroot}%{_libdir}/pkgconfig
rm -f %{buildroot}%{_bindir}/gpgme-config*
rm -f %{buildroot}%{_bindir}/gpgme-tool
rm -rf %{buildroot}%{_datadir}/aclocal
rm -rf %{buildroot}%{_datadir}/info/gpgme.*
%endif
rm -f %{buildroot}%{_bindir}/%{sname}-json
rm -f %{buildroot}%{_mandir}/man1/%{sname}-json.*
%oreon_autofiles compat-gpgmepp124 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles compat-qgpgme124-qt5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles compat-qgpgme124-qt6 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

pushd build
make check
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n compat-gpgmepp124 -f %{oreon_filedir}/compat-gpgmepp124.list
%files -n compat-qgpgme124-qt5 -f %{oreon_filedir}/compat-qgpgme124-qt5.list
%files -n compat-qgpgme124-qt6 -f %{oreon_filedir}/compat-qgpgme124-qt6.list

%changelog

%autochangelog
