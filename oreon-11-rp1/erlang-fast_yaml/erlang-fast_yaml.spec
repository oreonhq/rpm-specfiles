%global source0_hash ec798397a676a0c3f8f0930324fd108ae465eeafd4d56d3ed722395b2f609110
%global srcname fast_yaml
%global p1_utils_ver 1.0.28
Name: erlang-%{srcname}
Version: 1.0.40
Release:        1%{?dist}
License: Apache-2.0
Summary:        An Erlang wrapper for libyaml "C" library
URL:     https://github.com/processone/%{srcname}/
VCS:     git:%{url}.git
Source0:        https://github.com/processone/%{srcname}//archive/%{version}/%{srcname}-%{version}.tar.gz
Patch1:  erlang-fast_yaml-0001-Disable-port-compiler-until-we-package-it.patch
Provides:  erlang-p1_yaml = %{version}-%{release}
Obsoletes: erlang-p1_yaml < 1.0.2
Requires: erlang-p1_utils >= %{p1_utils_ver}
# oreon:deps
BuildRequires:  erlang-p1_utils
BuildRequires:  erlang-rebar3
BuildRequires:  gcc
BuildRequires:  libyaml-devel
# /oreon:deps
%description
P1 YAML is an Erlang wrapper for libyaml "C" library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build

%{erlang3_compile}
mkdir -p priv/lib
gcc c_src/fast_yaml.c $CFLAGS -fPIC -c -I%{_libdir}/erlang/usr/include -o c_src/fast_yaml.o
gcc c_src/fast_yaml.o $LDFLAGS -shared -L%{_libdir}/erlang/usr/lib -lei -lyaml -o priv/lib/fast_yaml.so
%install
%{erlang3_install}
install -d $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib
install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{srcname}-%{version}/priv/lib
%oreon_autofiles main

%check

%{erlang3_test}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
