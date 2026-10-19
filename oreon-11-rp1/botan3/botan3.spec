%global source2_hash 07862f27687739a7ac201759779d361fa6282f0d6f1cb7973c68ebe1f36f54af
%global source1_hash 0eb228c90cb1ac5ae3d6d367ea50742b017f5f6870362bb5d452561e9c5332dd
%global source0_hash 12f5a8358890bbee82edfe9d2e7769b0a610b6dd0e0698aea13d20a675d84620
%global major_version 3
Name:           botan3
Version:        3.13.0
Release:        1%{?dist}
Summary:        Crypto and TLS for C++
License:        BSD-2-Clause
URL:            https://botan.randombit.net/
Source0:        https://botan.randombit.net/releases/Botan-%{version}.tar.xz
Source1:        https://botan.randombit.net/releases/Botan-%{version}.tar.xz.asc
Source2:        https://botan.randombit.net/pgpkey.txt
Patch1:         pyproject.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-botan3 = %{version}-%{release}
# /oreon:deps
%description
Botan is a BSD-licensed crypto library written in C++. It provides a
wide variety of basic cryptographic algorithms, X.509 certificates and
CRLs, PKCS \#11 certificate requests, a filter/pipe message processing
system, and a wide variety of other features, all written in portable
C++. The API reference, tutorial, and examples may help impart the
flavor of the library. This is the current stable release branch 3.x
of Botan.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       python3-libs
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}
%{summary}

This package contains the Python3 binding for %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
%{summary}

This package contains HTML documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=%{SOURCE0}
%autosetup -n Botan-%{version} -p1

%build

export CXXFLAGS="${CXXFLAGS:-%{optflags}}"
%global enable_modules bzip2,zlib,jitter_rng
%{__python3} ./configure.py \
        --prefix=%{_prefix} \
        --libdir=%{_lib} \
        --docdir=%{_docdir} \
        --cc=gcc \
        --os=linux \
        --cpu=%{_arch} \
        --enable-modules=%{enable_modules} \
        --no-install-python-module \
        --with-sphinx \
        --with-doxygen \
        --with-rst2man \
        --with-cmake-config \
        --distribution-info="$(source /etc/os-release ; echo "$NAME") %{version}-%{release}" \
        --disable-static-library \
        --enable-stack-scrubbing \
        --with-tpm2 \
        --with-sqlite3 \
        --system-cert-bundle=/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem \
        --with-debug-info
%make_build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel
%install
%make_install
%pyproject_install
mv %{buildroot}%{_docdir}/botan-%{version} %{buildroot}%{_pkgdocdir}
rm -rf %{buildroot}%{_pkgdocdir}/handbook/{.doctrees,.buildinfo}
mv %{buildroot}%{_bindir}/botan %{buildroot}%{_bindir}/botan%{major_version}
mv %{buildroot}%{_mandir}/man1/botan.1 %{buildroot}%{_mandir}/man1/botan%{major_version}.1
%oreon_autofiles botan3-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles python3-botan3 usr/lib/python3*/site-packages/botan3* usr/lib64/python3*/site-packages/botan3* usr/bin/*
%oreon_autofiles botan3-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/lib/python3*/site-packages/botan3* usr/lib64/python3*/site-packages/botan3* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./botan-test
rm src/scripts/test_python_packaging.py
LD_LIBRARY_PATH=%{buildroot}%{_libdir} PYTHONPATH=src/python %{python3} src/scripts/test_python.py
%files
%files -n botan3-devel -f %{oreon_filedir}/botan3-devel.list
%files -n python3-botan3 -f %{oreon_filedir}/python3-botan3.list
%files -n botan3-doc -f %{oreon_filedir}/botan3-doc.list

%changelog

%autochangelog
