%global source0_hash c440fee6771453beb31bfa9b2bd84f7cca9e2091081239b655a226137cb8ec1d
%global srcname ezlib
%global p1_utils_ver 1.0.26
Name:       erlang-%{srcname}
Version:    1.0.16
Release:        1%{?dist}
License:    Apache-2.0
Summary:        Native zlib driver for Erlang
URL:        https://github.com/processone/%{srcname}
VCS:        git:%{url}.git
Source0:        https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1:     erlang-ezlib-0001-Disable-Rebar3-plugins.patch
Provides:   erlang-p1_zlib = %{version}-%{release}
Obsoletes:  erlang-p1_zlib <= 1.0.1-2
Requires: erlang-p1_utils >= %{p1_utils_ver}
# oreon:deps
BuildRequires:  erlang-p1_utils
BuildRequires:  erlang-rebar3
BuildRequires:  gcc
BuildRequires:  zlib-devel
# /oreon:deps
%description
A native zlib driver for Erlang / Elixir, used by ejabberd.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

%{erlang3_compile}
mkdir -p priv/lib
gcc c_src/ezlib.c $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/ezlib.o
gcc c_src/ezlib.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -lz -o priv/lib/ezlib.so
%install
%{erlang3_install}
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/ezlib.so \
    $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
