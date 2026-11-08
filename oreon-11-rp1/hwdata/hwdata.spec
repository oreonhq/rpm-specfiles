# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5a71ab7a48c668ef912fcfdbec046949087019f8dd7fb967445d36fbeb778350

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name: hwdata
Summary: Hardware identification and configuration data
Version:        0.413
Release:        1%{?dist}
License: GPL-2.0-or-later
Source0:        https://github.com/vcrhonek/hwdata/archive/v%{version}.tar.gz
URL:    https://github.com/vcrhonek/hwdata
BuildArch: noarch
BuildRequires: make
BuildRequires:  oreon-rpm-macros

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
%oreon_sha256

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

