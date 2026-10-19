%global source0_hash 578bf2c9ed4614820fb87cba5275a8d009e09b9748ef4e6c8921febb4dcedeff
%global major_version 1.10
Name:           botan
Version:        %{major_version}.17
Release:        53%{?dist}
Summary:        Crypto library written in C++
License:        LicenseRef-Callaway-BSD
URL:            http://botan.randombit.net/
Source0:        Botan-%{version}.stripped.tar.gz
Source1:        README.fedora
Patch0:         botan-1.10.5-ecc-fix.patch
Patch1:         botan-boost_python.patch
Patch2:         botan-1.10.13-python-init.patch
Patch3:         botan-1.10.17-doc-conf-2to3.patch
Patch4:         botan-1.10.17-u64bit.patch
Patch9:         Botan-1.10.17-add-riscv64.patch
%global __provides_exclude_from ^(%{python3_sitearch}/.*\\.so)$
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  zlib-devel
# /oreon:deps
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

%global enable_modules bzip2,zlib
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
find doc/examples -type f -exec chmod -x {} \;
mv doc/examples/python doc/python2-examples
cp -a doc/{examples,python2-examples,license.txt} \
   %{buildroot}%{_pkgdocdir}
cp -a %{SOURCE1} %{buildroot}%{_pkgdocdir}
rm -r %{buildroot}%{_pkgdocdir}/manual/{.doctrees,.buildinfo}
%ldconfig_post
%ldconfig_postun
%oreon_autofiles botan-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles botan-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-botan usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make CXX="g++ -std=c++11 ${CXXFLAGS:-%{optflags}}" %{?_smp_mflags} check
mv checks/validate.dat{,.orig}
awk '/\[.*\]/{f=0} /\[(RC5.*|RC6)\]/{f=1} (f && !/^#/){sub(/^/,"#")} {print}' \
    checks/validate.dat.orig > checks/validate.dat
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./check --validate
%files -f %{oreon_filedir}/main.list
%files -n botan-devel -f %{oreon_filedir}/botan-devel.list
%files -n botan-doc -f %{oreon_filedir}/botan-doc.list
%files -n python3-botan -f %{oreon_filedir}/python3-botan.list

%changelog

%autochangelog
