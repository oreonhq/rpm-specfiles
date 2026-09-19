%global source0_hash 207e8624382e815f58bc5c3d4aad725d94588a6cc465d34634e6533dcaae2e0d

%global ver_maj 0
%global ver_min 13
%global ver_patch 1
Name:		tomsfastmath
Version:	%{ver_maj}.%{ver_min}.%{ver_patch}
Release:	18%{?dist}
Summary:	Fast large integer arithmetic library

# Automatically converted from old format: Public Domain or WTFPL - needs further work
License:	LicenseRef-Callaway-Public-Domain OR WTFPL
URL:		http://www.libtom.net/
Source0:	https://github.com/libtom/tomsfastmath/archive/v%{ver_maj}.%{ver_min}.%{ver_patch}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:	libtool
BuildRequires:	gcc

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
# Add tomsfastmath.pc in next release
# sed -e 's,^Version:.*,Version: %%{version},' tomsfastmath.pc.in > tomsfastmath.pc
# mkdir -p %%{buildroot}%%{_libdir}/pkgconfig
# install -p -m 0644 -D tomsfastmath.pc %%{buildroot}%%{_libdir}/pkgconfig/

%ldconfig_scriptlets

%files
%doc doc/tfm.pdf
%license LICENSE
%{_libdir}/libtfm.so.*

%files devel
%{_includedir}/tfm.h
%{_libdir}/libtfm.so

%changelog
%autochangelog
