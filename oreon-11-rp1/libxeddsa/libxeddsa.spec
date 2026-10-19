%global source0_hash b54af487fb6278fa7832be3cf5e7f88cd65900e635f85e47cc1286bc1920f7ed
%global snapdate 20240426
%global commit d725c816bb26483ac397ce0d19de5ad2972955f1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           libxeddsa
Version:        2.0.0^%{snapdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        Toolkit around Curve25519 and Ed25519 key pairs
License:        MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/Syndace/%{name}
Source0:        https://github.com/Syndace/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libsodium-devel
BuildRequires:  libsodium-static
BuildRequires:  make
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
# /oreon:deps
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
%cmake_build
pushd docs/
make html  # results are in docs/_build/html/
popd
%install
%cmake_install
install -D -p -m 0644 include/xeddsa.h %{buildroot}%{_includedir}/xeddsa.h
mkdir -p %{buildroot}%{_pkgdocdir}/
cp -pr docs/_build/html %{buildroot}%{_pkgdocdir}/
rm -rf %{buildroot}%{_pkgdocdir}/html/.buildinfo
rm -f %{buildroot}/%{_libdir}/*.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%ctest -C Debug
%files -f %{oreon_filedir}/main.list
%files -n libxeddsa-devel -f %{oreon_filedir}/libxeddsa-devel.list
%files -n libxeddsa-doc -f %{oreon_filedir}/libxeddsa-doc.list

%changelog

%autochangelog
