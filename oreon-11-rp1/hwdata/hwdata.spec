%global source0_hash 13605519e72e46aa13d5eede1901a07a6c83cd25ef866a86e7458047b5c81ce5

Name: hwdata
Summary: Hardware identification and configuration data
Version: 0.405
Release: 1%{?dist}
License: GPL-2.0-or-later
Source:        https://github.com/vcrhonek/hwdata/archive/refs/tags/v%{version}.tar.gz#/hwdata-0.405.tar.gz

URL:    https://github.com/vcrhonek/hwdata
BuildArch: noarch
BuildRequires: make

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids and usb.ids databases.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains files for developing applications that use
%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build
%configure

# nothing to build

%install
%make_install libdir=%{_prefix}/lib

%files
%license COPYING
%doc LICENSE
%dir %{_datadir}/%{name}
%{_prefix}/lib/modprobe.d/dist-blacklist.conf
%{_datadir}/%{name}/*

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.405-1
- Prepare for Oreon 11 (RP1)
