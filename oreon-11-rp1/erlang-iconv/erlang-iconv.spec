%global source0_hash d781325fa991e4c0d6d207025f52c7761685323b0e61c498f172590eca0d9276
%global srcname iconv
%global p1_utils_ver 1.0.19
Name:       erlang-%{srcname}
Version:    1.0.14
Release:        1%{?dist}
Summary:        Fast encoding conversion library for Erlang / Elixir
License:    Apache-2.0
URL:        https://github.com/processone/%{srcname}
VCS:        scm:git:%{url}.git
Source0:        https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1:     erlang-iconv-0001-Disable-port-compiler-until-we-package-it.patch
Provides:   erlang-p1_iconv = %{version}-%{release}
Obsoletes:  erlang-p1_iconv <= 1.0.0-2
Requires: erlang-p1_utils >= %{p1_utils_ver}
# oreon:deps
BuildRequires:  erlang-p1_utils
BuildRequires:  erlang-rebar3
BuildRequires:  gcc
# /oreon:deps
%description
Erlang bindings for libiconv. This is used by ejabberd.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

%configure --enable-nif
%{erlang3_compile}
mkdir -p priv/lib
gcc c_src/iconv.c $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/iconv.o
gcc c_src/iconv.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -o priv/lib/iconv.so
%install
%{erlang3_install}
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/iconv.so $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
