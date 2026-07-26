%global source0_hash ea40b6679309bef1e589ea341adc04fb9aa5b588e0ec25ff4f072692e67d7f2e

%global srcname mqtree
%global p1_utils_ver 1.0.28

Name:       erlang-%{srcname}
Version:    1.0.19
Release:    %autorelease
License:    Apache-2.0
Summary:    Index tree for MQTT topic filters
URL:        https://github.com/processone/%{srcname}/
VCS:        git:%{url}.git
Source0:    %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1:     erlang-mqtree-0001-Remove-bundled-uthash.patch
Patch2:     erlang-mqtree-0002-FIXME-disable-Rebar3-plugins.patch
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: erlang-rebar3
BuildRequires: erlang-rebar3-pc
BuildRequires: gcc
BuildRequires: openssl-devel
BuildRequires: uthash-devel
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
An Erlang NIF implementation of N-ary tree to keep MQTT topic filters for
efficient matching.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/lib
gcc c_src/mqtree.c $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/mqtree.o
gcc c_src/mqtree.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -o priv/lib/mqtree.so

%install
%{erlang3_install}

install -d %{buildroot}%{_erllibdir}/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/* %{buildroot}%{_erllibdir}/%{srcname}-%{version}/priv/lib/

%check
%{erlang3_test}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
