%global source0_hash 578bf2c9ed4614820fb87cba5275a8d009e09b9748ef4e6c8921febb4dcedeff

%global major_version 1.10

Name:           botan
Version:        %{major_version}.17
Release:        53%{?dist}
Summary:        Crypto library written in C++

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://botan.randombit.net/
# tarfile is stripped using repack.sh. original tarfile to be found
# here: http://botan.randombit.net/releases/Botan-%%{version}.tgz
Source0:        Botan-%{version}.stripped.tar.gz
Source1:        README.fedora
# Enable only cleared ECC algorithms
Patch0:         botan-1.10.5-ecc-fix.patch
# Make boost_python selectable
Patch1:         botan-boost_python.patch
# Fix wrong path
Patch2:         botan-1.10.13-python-init.patch
# 2to3 doc/conf.py
Patch3:         botan-1.10.17-doc-conf-2to3.patch
# Fix FTBFS
Patch4:         botan-1.10.17-u64bit.patch
# Add RISC-V (riscv64)
# Upstream in later versions:
# https://github.com/randombit/botan/blob/master/src/build-data/arch/riscv64.txt
Patch9:         Botan-1.10.17-add-riscv64.patch

BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  make

# do not check .so files in the python_sitelib directories
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

%description
Botan is a BSD-licensed crypto library written in C++. It provides a
wide variety of basic cryptographic algorithms, X.509 certificates and
CRLs, PKCS \#10 certificate requests, a filter/pipe message processing
system, and a wide variety of other features, all written in portable
C++. The API reference, tutorial, and examples may help impart the
flavor of the library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       bzip2-devel
Requires:       zlib-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
%{summary}

This package contains HTML documentation for %{name}.

%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%{summary}

This package contains the Python3 binding for %{name}.

Note: The Python binding should be considered alpha software, and the
interfaces may change in the future.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Botan-%{version}
%autosetup -p1 -n Botan-%{version}

# These tests will fail.
rm -rf checks/ec_tests.cpp

%build

# we have the necessary prerequisites, so enable optional modules
%global enable_modules bzip2,zlib

# fixme: maybe disable unix_procs, very slow.
%global disable_modules gnump

%{__python3} ./configure.py \
        --prefix=%{_prefix} \
        --libdir=%{_lib} \
        --cc=gcc \
        --os=linux \
        --cpu=%{_arch} \
        --enable-modules=%{enable_modules} \
        --disable-modules=%{disable_modules} \
        --with-boost-python \
        --with-python-version=dummy.dummy \
        --with-sphinx

# (ab)using CXX as an easy way to inject our CXXFLAGS
make CXX="g++ -std=c++11 ${CXXFLAGS:-%{optflags}}" %{?_smp_mflags}

make -f Makefile.python \
     CXX="g++ -std=c++11 ${CXXFLAGS:-%{optflags}}" %{?_smp_mflags} \
     PYTHON_INC="$(python3-config --includes)" \
     PYTHON_ROOT=. \
     BOOST_PYTHON=boost_python%{python3_version_nodots}

%install
make install \
     DESTDIR=%{buildroot}%{_prefix} \
     DOCDIR=%{buildroot}%{_pkgdocdir} \
     INSTALL_CMD_EXEC="install -p -m 755" \
     INSTALL_CMD_DATA="install -p -m 644"

make -f Makefile.python install \
     PYTHON_SITE_PACKAGE_DIR=%{buildroot}%{python3_sitearch}

# fixups
find doc/examples -type f -exec chmod -x {} \;
mv doc/examples/python doc/python2-examples
cp -a doc/{examples,python2-examples,license.txt} \
   %{buildroot}%{_pkgdocdir}
cp -a %{SOURCE1} %{buildroot}%{_pkgdocdir}
rm -r %{buildroot}%{_pkgdocdir}/manual/{.doctrees,.buildinfo}

%ldconfig_post

%ldconfig_postun

%files
%dir %{_pkgdocdir}
%{_pkgdocdir}/readme.txt
%{_pkgdocdir}/README.fedora
%if 0%{?_licensedir:1}
%exclude %{_pkgdocdir}/license.txt
%license doc/license.txt
%else
%{_pkgdocdir}/license.txt
%endif # licensedir
%{_libdir}/libbotan-%{major_version}.so.*

%files devel
%{_pkgdocdir}/examples
%{_bindir}/botan-config-%{major_version}
%{_includedir}/*
%exclude %{_libdir}/libbotan-%{major_version}.a
%{_libdir}/libbotan-%{major_version}.so
%{_libdir}/pkgconfig/botan-%{major_version}.pc

%files doc
%dir %{_pkgdocdir}
%{_pkgdocdir}/manual
# next files duplicated on purpose, because -doc doesn't depend on the
# main package
%{_pkgdocdir}/readme.txt
%{_pkgdocdir}/README.fedora
%if 0%{?_licensedir:1}
%exclude %{_pkgdocdir}/license.txt
%license doc/license.txt
%else
%{_pkgdocdir}/license.txt
%endif # licensedir
%{_pkgdocdir}/python2-examples

%files -n python3-%{name}
%{python3_sitearch}/%{name}

%check
make CXX="g++ -std=c++11 ${CXXFLAGS:-%{optflags}}" %{?_smp_mflags} check

# these checks would fail
mv checks/validate.dat{,.orig}
awk '/\[.*\]/{f=0} /\[(RC5.*|RC6)\]/{f=1} (f && !/^#/){sub(/^/,"#")} {print}' \
    checks/validate.dat.orig > checks/validate.dat
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./check --validate

%changelog
%autochangelog
