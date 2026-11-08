# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2c1bacd2110f4799f74de6ebb714b94cf6f80fb112316b1219480fd22562148c

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:           xcb-proto
Version:        1.17.0
Release:        1%{?dist}
Summary:        XCB protocol descriptions

License:        X11-distribute-modifications-variant
URL:            https://xcb.freedesktop.org/
Source0:        https://xorg.freedesktop.org/archive/individual/proto/xcb-proto-%{version}.tar.xz

BuildArch:      noarch
%{!?python3_sitelib:%global python3_sitelib %(python3 -c "import sysconfig; print(sysconfig.get_path('purelib'))")}

BuildRequires:  autoconf automake
BuildRequires:  libxml2
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  oreon-rpm-macros

%description
XCB is a project to enable efficient language bindings to the X11 protocol.
This package contains the protocol descriptions themselves.  Language
bindings use these protocol descriptions to generate code for marshalling
the protocol.


%prep
%oreon_sha256

%autosetup -p1
autoreconf -fiv


%build
# Bit of a hack to get the pc file in /usr/share, so we can be noarch.
%configure --libdir=%{_datadir}
%make_build


%install
%make_install


%check
%make_build check


%files
%license COPYING
%doc NEWS README.md TODO doc/xml-xcb.txt
%{_datadir}/pkgconfig/xcb-proto.pc
%dir %{_datadir}/xcb/
%{_datadir}/xcb/*.xsd
%{_datadir}/xcb/*.xml
%{python3_sitelib}/xcbgen


