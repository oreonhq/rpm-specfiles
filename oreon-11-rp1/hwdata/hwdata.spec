Name: hwdata
Summary: Hardware identification and configuration data
Version: 0.405
Release: 1%{?dist}
License: GPL-2.0-or-later
Source: https://github.com/vcrhonek/hwdata/archive/v%{version}.tar.gz
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
