%global source0_hash 5faf1c87db7e0ade5635c72cfed9e0434d26477721a791dbe56c0a99350ce448

%if 0%{?fedora} || 0%{?rhel} >= 8
%global luaver 5.4
%else
%global luaver 5.1
%endif
%global lualibdir %{_libdir}/lua/%{luaver}
%global luapkgdir %{_datadir}/lua/%{luaver}

Name:           lua-lxc
Version:        3.0.2
Release:        21%{?dist}
Summary:        Lua binding for LXC
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://linuxcontainers.org/lxc
Source0:        https://linuxcontainers.org/downloads/lxc/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lua)
BuildRequires:  lxc-devel >= 3.0.0
BuildRequires:  make
BuildRequires:  gcc

%description
Linux Resource Containers provide process and resource isolation
without the overhead of full virtualization.

The lua-lxc package contains the Lua binding for LXC.

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}core\\.so\\.0

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%{lualibdir}/lxc
%{luapkgdir}/lxc.lua

%changelog
%autochangelog
