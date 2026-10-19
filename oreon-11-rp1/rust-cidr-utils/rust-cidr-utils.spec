%global source0_hash 1f59aae4103f56b79b449c67bde6d1e96aa9f617d95af57ed1d72d6f948fe597
%bcond check 1
%global debug_package %{nil}
%global crate cidr-utils
Name:           rust-cidr-utils
Version:        0.7.1
Release:        1%{?dist}
Summary:        Functions for working with IPv4 CIDRs and IPv6 CIDRs
License:        MIT
URL:            https://crates.io/crates/cidr-utils
Source0:        https://static.crates.io/crates/cidr-utils/cidr-utils-%{version}.crate
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
Summary:        Functions for working with IPv4 CIDRs and IPv6 CIDRs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+combiner-devel
Summary:        Functions for working with IPv4 CIDRs and IPv6 CIDRs
BuildArch:      noarch
%description -n %{name}+combiner-devel

This package contains library source intended for building other packages which
use the "combiner" feature of the "%{crate}" crate.

%package     -n %{name}+iterator-devel
Summary:        Functions for working with IPv4 CIDRs and IPv6 CIDRs
BuildArch:      noarch
%description -n %{name}+iterator-devel

This package contains library source intended for building other packages which
use the "iterator" feature of the "%{crate}" crate.

%package     -n %{name}+separator-devel
Summary:        Functions for working with IPv4 CIDRs and IPv6 CIDRs
BuildArch:      noarch
%description -n %{name}+separator-devel

This package contains library source intended for building other packages which
use the "separator" feature of the "%{crate}" crate.

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
%files -n rust-cidr-utils-devel -f %{oreon_filedir}/rust-cidr-utils-devel.list

%changelog

%autochangelog
