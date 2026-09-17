%global source0_hash 06ede9ce22239403f285741973ca54d78f73d6a2c82587165354aa21d76f599c

%global srcname fast_yaml
%global p1_utils_ver 1.0.28

Name: erlang-%{srcname}
Version: 1.0.39
Release: %autorelease
License: Apache-2.0
Summary: An Erlang wrapper for libyaml "C" library
URL:     https://github.com/processone/%{srcname}/
VCS:     git:%{url}.git
Source0: %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1:  erlang-fast_yaml-0001-Disable-port-compiler-until-we-package-it.patch
Provides:  erlang-p1_yaml = %{version}-%{release}
Obsoletes: erlang-p1_yaml < 1.0.2
BuildRequires: gcc
BuildRequires: erlang-rebar3
BuildRequires: erlang-p1_utils >= %{p1_utils_ver}
BuildRequires: libyaml-devel
Requires: erlang-p1_utils >= %{p1_utils_ver}

%description
P1 YAML is an Erlang wrapper for libyaml "C" library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%{erlang3_compile}

# FIXME we don't have a port compiler plugin for rebar3 yet
mkdir -p priv/lib
gcc c_src/fast_yaml.c $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/fast_yaml.o
gcc c_src/fast_yaml.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -lyaml -o priv/lib/fast_yaml.so

%install
%{erlang3_install}
install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib

%check
%{erlang3_test}

%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
