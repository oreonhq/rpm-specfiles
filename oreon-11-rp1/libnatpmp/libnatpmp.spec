%global source0_hash 0684ed2c8406437e7519a1bd20ea83780db871b3a3a5d752311ba3e889dbfc70
Name:           libnatpmp
Version:        20230423
Release:        9%{?dist}
Summary:        Library of The NAT Port Mapping Protocol (NAT-PMP)
License:        LGPL-2.0-or-later
URL:            http://miniupnp.free.fr/libnatpmp.html
Source0:        http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
libnatpmp is an attempt to make a portable and fully compliant implementation
of the protocol for the client side. It is based on non blocking sockets and
all calls of the API are asynchronous. It is therefore very easy to integrate
the NAT-PMP code to any event driven code.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%make_build CFLAGS="-fPIC -Wall -DENABLE_STRNATPMPERR %{optflags}" EXTRA_LD="%{?__global_ldflags}"
%install
make install INSTALL="install -p" PREFIX=%{buildroot} \
     INSTALLDIRLIB="%{buildroot}%{_libdir}" \
     INSTALLDIRINC="%{buildroot}%{_includedir}" \
     INSTALLDIRBIN="%{buildroot}%{_bindir}"
install -m 0644 -p natpmp_declspec.h %{buildroot}%{_includedir}/
find %{buildroot} -name '*.a' -delete -print
find %{buildroot} -name '*.so' -exec chmod 755 {} ";" -print
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make testgetgateway
./testgetgateway
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libnatpmp-devel -f %{oreon_filedir}/libnatpmp-devel.list

%changelog

%autochangelog
