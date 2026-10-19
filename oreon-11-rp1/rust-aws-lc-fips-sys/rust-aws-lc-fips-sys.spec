%global source0_hash 37b00953a69b2cfb471d13d72538d2e66930832340b0f31deadd404b48c573c5
%bcond check 0
%global debug_package %{nil}
%global crate aws-lc-fips-sys
Name:           rust-aws-lc-fips-sys
Version:        0.13.16
Release:        1%{?dist}
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
License:        ISC AND (Apache-2.0 OR ISC) AND OpenSSL
URL:            https://crates.io/crates/aws-lc-fips-sys
Source0:        https://static.crates.io/crates/aws-lc-fips-sys/aws-lc-fips-sys-%{version}.crate
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
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+asan-devel
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+asan-devel

This package contains library source intended for building other packages which
use the "asan" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-devel
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+bindgen-devel

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+fips-devel
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+fips-devel

This package contains library source intended for building other packages which
use the "fips" feature of the "%{crate}" crate.

%package     -n %{name}+ssl-devel
Summary:        AWS-LC is a general-purpose cryptographic library maintained by the A...
BuildArch:      noarch
%description -n %{name}+ssl-devel

This package contains library source intended for building other packages which
use the "ssl" feature of the "%{crate}" crate.

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
%files -n rust-aws-lc-fips-sys-devel -f %{oreon_filedir}/rust-aws-lc-fips-sys-devel.list

%changelog

%autochangelog
