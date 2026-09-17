%global source0_hash 9336f02ea99cfad359c78c50fdd9c3061aac7b31966abdc3223f56b3ed7cc377

%global srcname esip

%global fast_tls_ver 1.1.21
%global p1_utils_ver 1.0.26
%global stun_ver 1.2.14

Name: erlang-%{srcname}
Version: 1.0.54
Release: %autorelease
License: Apache-2.0
Summary: ProcessOne SIP server component in Erlang
URL: https://github.com/processone/%{srcname}
VCS: git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1: erlang-esip-0001-Disable-Rebar3-plugins.patch
BuildRequires: erlang-fast_tls >= %{fast_tls_ver}
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3
BuildRequires: erlang-stun >= %{stun_ver}
BuildRequires: gcc
Obsoletes: erlang-p1_sip < 1.0.2
Provides: erlang-p1_sip = %{version}-%{release}
Requires: erlang-fast_tls >= %{fast_tls_ver}
Requires: erlang-p1_utils >= %{p1_utils_ver}
Requires: erlang-stun >= %{stun_ver}

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/lib
gcc c_src/esip_codec.c $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/esip_codec.o
gcc c_src/esip_codec.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -o priv/lib/esip_drv.so

%install
%{erlang3_install}

install -d $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/include
install -d $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/priv/lib

install -pm644 include/* $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/include/
install -pm755 priv/lib/*.so $RPM_BUILD_ROOT%{_erllibdir}/esip-%{version}/priv/lib/

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{erlang_appdir}

%changelog
%autochangelog
