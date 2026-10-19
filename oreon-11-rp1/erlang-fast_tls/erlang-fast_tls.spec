%global source0_hash fbffef294f4c8695cd7000084bed89e9e206c58a6a4a097d50560ed6d0b0dd0c
%global srcname fast_tls
%global p1_utils_ver 1.0.28
Name: erlang-%{srcname}
Version: 1.1.26
Release:        1%{?dist}
License: Apache-2.0
Summary:        TLS / SSL native driver for Erlang / Elixir
URL: https://github.com/processone/%{srcname}/
VCS: git:%{url}.git
Source0:        https://github.com/processone/%{srcname}//archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1: erlang-fast_tls-0001-Use-the-system-ciphers-by-default.patch
Patch2: erlang-fast_tls-0002-Disable-Rebar3-plugins.patch
Provides:  erlang-p1_tls = %{version}-%{release}
Obsoletes: erlang-p1_tls < 1.0.1
Requires: erlang-p1_utils >= %{p1_utils_ver}
# oreon:deps
BuildRequires:  erlang-p1_utils
BuildRequires:  erlang-rebar3
BuildRequires:  gcc
BuildRequires:  openssl-devel
# /oreon:deps
%description
TLS / SSL native driver for Erlang / Elixir. This is used by ejabberd.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build

%{erlang3_compile}
mkdir -p priv/lib
gcc c_src/fast_tls.c	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/fast_tls.o
gcc c_src/ioqueue.c	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/ioqueue.o
gcc c_src/p1_sha.c	$CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/p1_sha.o
gcc c_src/fast_tls.o c_src/ioqueue.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lssl -lcrypto -o priv/lib/fast_tls.so
gcc c_src/p1_sha.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -L%{_libdir} -lssl -lcrypto -o priv/lib/p1_sha.so
%install
%{erlang3_install}
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
