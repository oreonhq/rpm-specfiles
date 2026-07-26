%global source0_hash b54af487fb6278fa7832be3cf5e7f88cd65900e635f85e47cc1286bc1920f7ed

# Upstream version is 2.0.0 but has no release
%global snapdate 20240426
%global commit d725c816bb26483ac397ce0d19de5ad2972955f1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           libxeddsa
Version:        2.0.0^%{snapdate}git%{shortcommit}
Release:        9%{?dist}
Summary:        Toolkit around Curve25519 and Ed25519 key pairs

# ref10 library is Public Domain (under ref10/ subdirectory)
License:        MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libsodium-devel
BuildRequires:  libsodium-static
# For docs:
BuildRequires:  doxygen
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-breathe

%description
An implementation of XEdDSA, based on ref10 by Daniel J. Bernstein.

XEdDSA is a signature scheme that utilizes the birational maps between
Curve25519 and Ed25519 (defined in RFC 7748 on page 5) to create and
verify digital signatures with Curve25519 keys.

XEdDSA is also specified for Curve448/Ed448, which is not covered by
this library.

This library has a set of functions surrounding Curve25519 and Ed25519
key pairs, to make this library a toolset around both curves instead
of just an implementation of XEdDSA.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
The %{name}-doc package contains HTML documentation for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir}
# results are in redhat-linux-build/
%cmake_build
# Build HTML documentation
pushd docs/
make html  # results are in docs/_build/html/
popd

%install
%cmake_install
# INCLUDE_INSTALL_DIR=/usr/include is not used by the project
install -D -p -m 0644 include/xeddsa.h %{buildroot}%{_includedir}/xeddsa.h
# Install html docs
mkdir -p %{buildroot}%{_pkgdocdir}/
cp -pr docs/_build/html %{buildroot}%{_pkgdocdir}/
# Remove buildinfo sphinx documentation
rm -rf %{buildroot}%{_pkgdocdir}/html/.buildinfo
# Remove static library
rm -f %{buildroot}/%{_libdir}/*.a

%check
%ctest -C Debug

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/%{name}.so.2
%{_libdir}/%{name}.so.2.*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/xeddsa.h

%files doc
%{_pkgdocdir}/html/

%changelog
%autochangelog
