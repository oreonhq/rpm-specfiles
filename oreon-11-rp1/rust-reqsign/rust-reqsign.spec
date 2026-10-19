%global source0_hash 2f343280e2e5ce07f97f32ead07a68824cb9cea60093ad78f22664011f90ae47
%bcond check 1
%global debug_package %{nil}
%global crate reqsign
Name:           rust-reqsign
Version:        0.20.0
Release:        1%{?dist}
Summary:        Signing HTTP requests for popular cloud services
License:        Apache-2.0
URL:            https://crates.io/crates/reqsign
Source0:        https://static.crates.io/crates/reqsign/reqsign-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Signing HTTP requests for popular cloud services
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aliyun-devel
Summary:        Signing HTTP requests for popular cloud services
BuildArch:      noarch
%description -n %{name}+aliyun-devel

This package contains library source intended for building other packages which
use the "aliyun" feature of the "%{crate}" crate.

%package     -n %{name}+aws-devel
Summary:        Signing HTTP requests for popular cloud services
BuildArch:      noarch
%description -n %{name}+aws-devel

This package contains library source intended for building other packages which
use the "aws" feature of the "%{crate}" crate.

%package     -n %{name}+azure-devel
Summary:        Signing HTTP requests for popular cloud services
BuildArch:      noarch
%description -n %{name}+azure-devel

This package contains library source intended for building other packages which
use the "azure" feature of the "%{crate}" crate.

%package     -n %{name}+default-context-devel
Summary:        Signing HTTP requests for popular cloud services
BuildArch:      noarch
%description -n %{name}+default-context-devel

This package contains library source intended for building other packages which
use the "default-context" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Signing HTTP requests for popular cloud services
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+google-devel
Summary:        Signing HTTP requests for popular cloud services
BuildArch:      noarch
%description -n %{name}+google-devel

This package contains library source intended for building other packages which
use the "google" feature of the "%{crate}" crate.

%package     -n %{name}+huaweicloud-devel
Summary:        Signing HTTP requests for popular cloud services
BuildArch:      noarch
%description -n %{name}+huaweicloud-devel

This package contains library source intended for building other packages which
use the "huaweicloud" feature of the "%{crate}" crate.

%package     -n %{name}+oracle-devel
Summary:        Signing HTTP requests for popular cloud services
BuildArch:      noarch
%description -n %{name}+oracle-devel

This package contains library source intended for building other packages which
use the "oracle" feature of the "%{crate}" crate.

%package     -n %{name}+tencent-devel
Summary:        Signing HTTP requests for popular cloud services
BuildArch:      noarch
%description -n %{name}+tencent-devel

This package contains library source intended for building other packages which
use the "tencent" feature of the "%{crate}" crate.

%package     -n %{name}+volcengine-devel
Summary:        Signing HTTP requests for popular cloud services
BuildArch:      noarch
%description -n %{name}+volcengine-devel

This package contains library source intended for building other packages which
use the "volcengine" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-reqsign-devel -f %{oreon_filedir}/rust-reqsign-devel.list

%changelog

%autochangelog
