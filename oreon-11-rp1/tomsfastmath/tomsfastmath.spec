%global source0_hash 207e8624382e815f58bc5c3d4aad725d94588a6cc465d34634e6533dcaae2e0d
%global ver_maj 0
%global ver_min 13
%global ver_patch 1
Name:		tomsfastmath
Version:	%{ver_maj}.%{ver_min}.%{ver_patch}
Release:        18%{?dist}
Summary:        Fast large integer arithmetic library
License:	LicenseRef-Callaway-Public-Domain OR WTFPL
URL:		http://www.libtom.net/
Source0:        https://github.com/libtom/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
TomsFastMath is meant to be a very fast yet still fairly portable and easy to
port large integer arithmetic library written in ISO C. The goal specifically
is to be able to perform very fast modular exponentiations and other related
functions required for ECC, DH and RSA cryptosystems.

%package devel
Summary:	Development headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%make_build -f makefile.shared CFLAGS="%{build_cflags} -fomit-frame-pointer -Isrc/headers" LDFLAGS="%{build_ldflags}"
%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
install -p -m0755 .libs/libtfm.so.1.0.0 %{buildroot}%{_libdir}
pushd %{buildroot}%{_libdir}
ln -s libtfm.so.1.0.0 libtfm.so.1
ln -s libtfm.so.1.0.0 libtfm.so
popd
install -p -m0644 -D src/headers/tfm.h %{buildroot}%{_includedir}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tomsfastmath-devel -f %{oreon_filedir}/tomsfastmath-devel.list

%changelog

%autochangelog
