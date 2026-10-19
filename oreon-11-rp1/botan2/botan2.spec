%global source0_hash 12f5a8358890bbee82edfe9d2e7769b0a610b6dd0e0698aea13d20a675d84620
%global major_version 2
Name:           botan2
Version:        3.13.0
Release:        1%{?dist}
Summary:        Crypto and TLS for C++11
License:        BSD-2-Clause
URL:            https://botan.randombit.net/
Source0:        https://botan.randombit.net/releases/Botan-%{version}.tar.xz
Patch0:         37fec38ff97604f964122cd2d33f5d503f319b10.patch
Patch1:         f765f0b312f2998498f629d93369babfb2c975b4.patch
Patch2:         0001-fix-make-additions-be-constant-time.patch
Patch3:         0001-fix-use-fedora-new-pem-cert-location.patch
Patch4:         0001-backport-security-fix-for-compiler-induced-side-chan.patch
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  zlib-devel
# /oreon:deps
%description
Botan is a BSD-licensed crypto library written in C++. It provides a
wide variety of basic cryptographic algorithms, X.509 certificates and
CRLs, PKCS \#10 certificate requests, a filter/pipe message processing
system, and a wide variety of other features, all written in portable
C++. The API reference, tutorial, and examples may help impart the
flavor of the library. This is the current stable release branch 2.x
of Botan.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
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
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}
%{summary}

This package contains the Python3 binding for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Botan-%{version}
%oreon_prep
%build

export CXXFLAGS="${CXXFLAGS:-%{optflags}}"
%global enable_modules bzip2,zlib
%{__python3} ./configure.py \
        --prefix=%{_prefix} \
        --libdir=%{_lib} \
        --docdir=%{_docdir} \
        --cc=gcc \
        --os=linux \
        --cpu=%{_arch} \
        --enable-modules=%{enable_modules} \
        --with-python-version=%{python3_version} \
        --with-sphinx \
        --with-rst2man \
        --distribution-info="$(source /etc/os-release ; echo "$NAME")" \
        --disable-static-library \
        --with-debug-info
%make_build PYTHON_EXE=%{__python3}
%install
make install PYTHON_EXE=%{__python3} DESTDIR=%{buildroot}
sed -e '1{/^#!/d}' -i %{buildroot}%{python3_sitearch}/botan2.py
%if "%{python3_sitelib}" != "%{python3_sitearch}"
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}%{python3_sitearch}/botan2.py %{buildroot}%{python3_sitelib}/botan2.py
%endif
mv %{buildroot}%{_docdir}/botan-%{version} %{buildroot}%{_pkgdocdir}
rm -r %{buildroot}%{_pkgdocdir}/handbook/{.doctrees,.buildinfo}
%ldconfig_scriptlets
%oreon_autofiles botan2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles botan2-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-botan2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./botan-test
%files -f %{oreon_filedir}/main.list
%files -n botan2-devel -f %{oreon_filedir}/botan2-devel.list
%files -n botan2-doc -f %{oreon_filedir}/botan2-doc.list
%files -n python3-botan2 -f %{oreon_filedir}/python3-botan2.list

%changelog

%autochangelog
