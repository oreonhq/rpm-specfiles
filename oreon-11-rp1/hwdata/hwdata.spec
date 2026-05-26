Name: hwdata
Summary: Hardware identification and configuration data
Version: 0.405
Release: 1%{?dist}
License: GPL-2.0-or-later
Source: https://github.com/vcrhonek/hwdata/archive/v%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 13605519e72e46aa13d5eede1901a07a6c83cd25ef866a86e7458047b5c81ce5
%global source0_file v0.405.tar.gz
# oreon url source checksums end
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v0.405.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "13605519e72e46aa13d5eede1901a07a6c83cd25ef866a86e7458047b5c81ce5" || { echo "oreon: Source0 SHA256 mismatch for v0.405.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
