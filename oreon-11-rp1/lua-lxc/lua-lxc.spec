%global source0_hash 5faf1c87db7e0ade5635c72cfed9e0434d26477721a791dbe56c0a99350ce448
%global luaver 5.1
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}
Name:           lua-lxc
Version:        3.0.2
Release:        1%{?dist}
Summary:        Lua binding for LXC
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://linuxcontainers.org/lxc
Source0:        https://linuxcontainers.org/downloads/lxc/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  lxc-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lua)
# /oreon:deps
%description
Linux Resource Containers provide process and resource isolation
without the overhead of full virtualization.

The lua-lxc package contains the Lua binding for LXC.

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}core\\.so\\.0

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
