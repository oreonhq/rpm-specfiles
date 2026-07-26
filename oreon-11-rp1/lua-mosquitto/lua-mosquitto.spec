%global source0_hash 0e83d498d8c9eb2ca933ce5a9e2ed53194a25eca18c777525000419fc507e725

%global the_so_name mosquitto.so

Name:           lua-mosquitto
Version:        0.3
Release:        16%{?dist}
License:        MIT
Summary:        Lua bindings to libmosquitto
Url:            https://github.com/flukso/%{name}/
Source:         https://github.com/flukso/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  lua >= 5.1
BuildRequires:  lua-devel >= 5.1
BuildRequires:  mosquitto-devel
BuildRequires: make

Requires:       lua(abi) = %{lua_version}

%description
%{name} is a Lua library that provides complete bindings to the
Eclipse Mosquitto message broker (https://mosquitto.org) API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# To make sure we are using proper flags
export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
export OPT=
%make_build %{the_so_name}

%install
%make_install

%files
%license LICENSE
%doc README.md
%{lua_libdir}/%{the_so_name}

%changelog
%autochangelog
