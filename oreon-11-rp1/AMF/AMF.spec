# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c4b26b2c58295ad6f43176607d07a345f05d9770d53e7234299701b6956b3761
%global source1_hash ea39044e69f843d4fff7617e9a98875a9e950f18b7233bfaac731ffc9ec48184
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           AMF
Epoch:          1
Version:        1.5.3
Release:        %{autorelease}
Summary:        Advanced Media Framework (AMF) SDK
License:        MIT
URL:            https://gpuopen.com/advanced-media-framework/
BuildArch:      noarch

Source0:        %{name}-cleaned-%{version}.tar.gz
Source1:        %{name}-tarball.sh

%description
A light-weight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed source AMD
Pro driver and OpenMax on the open source AMD Mesa driver.

%package        devel
Summary:        Development files for %{name}

%description    devel
A light-weight, portable multimedia framework that abstracts away most of the
platform and API-specific details. %{name} is supported on the closed source AMD
Pro driver and OpenMax on the open source AMD Mesa driver.

The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        samples
Summary:        Sample files for %{name}

%description    samples
The %{name}-samples package contains sample programs and source for applications
that use %{name}.

%package        docs
Summary:        PDF documentation for %{name}

%description    docs
The %{name}-docs package contains the development documentation in PDF format
that is available in the main %{name}-devel package in Markdown format.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1

%install
mkdir -p %{buildroot}%{_includedir}/%{name}
cp -fr amf/public/include/* %{buildroot}%{_includedir}/%{name}/

mkdir -p %{buildroot}%{_usrsrc}/%{name}
cp -fr amf/public/* %{buildroot}%{_usrsrc}/%{name}/
rm -fr %{buildroot}%{_usrsrc}/%{name}/include
ln -sf ../../include/AMF %{buildroot}%{_usrsrc}/%{name}/include

mkdir pdf
mv amf/doc/*pdf pdf/

%files devel
%license LICENSE.txt
%doc amf/doc/*
%{_includedir}/%{name}/

%files samples
%license LICENSE.txt
%{_usrsrc}/%{name}

%files docs
%license LICENSE.txt
%doc pdf/*

%changelog
%autochangelog
