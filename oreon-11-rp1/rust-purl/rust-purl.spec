%global source10_hash 93dd22d1a0fbb1ccb4e320a7ac1f5f58c7338eb11f8893756b7819cd1b62b5e3
%global source0_hash 60ebe4262ae91ddd28c8721111a0a6e9e58860e211fc92116c4bb85c98fd96ad
%bcond check 1
%global debug_package %{nil}
%global crate purl
Name:           rust-purl
Version:        0.1.6
Release:        1%{?dist}
Summary:        Package URL implementation with customizable package types
License:        MIT
URL:            https://crates.io/crates/purl
Source0:        https://static.crates.io/crates/purl/purl-%{version}.crate
Source10:       https://github.com/phylum-dev/purl/raw/refs/tags/v%{version}/LICENSE
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
Summary:        Package URL implementation with customizable package types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+package-type-devel
Summary:        Package URL implementation with customizable package types
BuildArch:      noarch
%description -n %{name}+package-type-devel

This package contains library source intended for building other packages which
use the "package-type" feature of the "%{crate}" crate.

%package     -n %{name}+phf-devel
Summary:        Package URL implementation with customizable package types
BuildArch:      noarch
%description -n %{name}+phf-devel

This package contains library source intended for building other packages which
use the "phf" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Package URL implementation with customizable package types
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+smartstring-devel
Summary:        Package URL implementation with customizable package types
BuildArch:      noarch
%description -n %{name}+smartstring-devel

This package contains library source intended for building other packages which
use the "smartstring" feature of the "%{crate}" crate.

%package     -n %{name}+unicase-devel
Summary:        Package URL implementation with customizable package types
BuildArch:      noarch
%description -n %{name}+unicase-devel

This package contains library source intended for building other packages which
use the "unicase" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p '%{SOURCE10}' .
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
%files -n rust-purl-devel -f %{oreon_filedir}/rust-purl-devel.list

%changelog

%autochangelog
