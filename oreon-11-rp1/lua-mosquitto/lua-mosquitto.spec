%global source0_hash 5511ab80481dc8b192424a5d0ffa51a998307d36e9c7e0ca230373048de13a9f
%global the_so_name mosquitto.so
Name:           lua-mosquitto
Version:        0.4.1
Release:        1%{?dist}
License:        MIT
Summary:        Lua bindings to libmosquitto
Url:            https://github.com/flukso/%{name}/
Source0:        https://github.com/flukso/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       lua(abi) = %{lua_version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lua
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  mosquitto-devel
BuildRequires:  pkgconfig
# /oreon:deps
%description
%{name} is a Lua library that provides complete bindings to the
Eclipse Mosquitto message broker (https://mosquitto.org) API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

export CFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags}"
export OPT=
%make_build %{the_so_name}
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
