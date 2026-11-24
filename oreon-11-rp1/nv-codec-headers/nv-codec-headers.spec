# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2255bc74d038b95aa4be30f5f66322c2176acbdb90ada1851db6993536fbeaf7
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           nv-codec-headers
Version:        13.1.15.0
Release:        %{autorelease}
Summary:        FFmpeg version of Nvidia Codec SDK headers
License:        MIT
URL:            https://github.com/FFmpeg/nv-codec-headers
Source0:        %{url}/archive/n%{version}/nv-codec-headers-n%{version}.tar.gz

BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  make

%description
FFmpeg version of headers required to interface with Nvidias codec APIs.

%prep
%oreon_sha256
%autosetup -n nv-codec-headers-n%{version}
sed -i -e 's@/include@/include/ffnvcodec@g' ffnvcodec.pc.in

sed -n '4,25p' include/ffnvcodec/nvEncodeAPI.h > LICENSE
sed -i '1,22s/^.\{,3\}//' LICENSE

%build
%make_build PREFIX=%{_prefix} LIBDIR=/share

%install
%make_install PREFIX=%{_prefix} LIBDIR=/share

%files
%doc README
%license LICENSE
%{_includedir}/ffnvcodec/
%{_datadir}/pkgconfig/ffnvcodec.pc

%changelog
%autochangelog
