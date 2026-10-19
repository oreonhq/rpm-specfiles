%global source0_hash df51e72c150781d2c7d4cbcb0b803277caaa80476786994a62961a8f1010dafb
%bcond check 1
%global debug_package %{nil}
%global crate config-file
Name:           rust-config-file
Version:        0.2.3
Release:        1%{?dist}
Summary:        Read and parse configuration file automatically
License:        BSD-2-Clause
URL:            https://crates.io/crates/config-file
Source0:        https://static.crates.io/crates/config-file/config-file-%{version}.crate
Source1:	LICENSE
Patch:          config-file-fix-metadata.diff
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
Summary:        Read and parse configuration file automatically
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Read and parse configuration file automatically
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+serde-xml-rs-devel
Summary:        Read and parse configuration file automatically
BuildArch:      noarch
%description -n %{name}+serde-xml-rs-devel

This package contains library source intended for building other packages which
use the "serde-xml-rs" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Read and parse configuration file automatically
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+serde_yaml-devel
Summary:        Read and parse configuration file automatically
BuildArch:      noarch
%description -n %{name}+serde_yaml-devel

This package contains library source intended for building other packages which
use the "serde_yaml" feature of the "%{crate}" crate.

%package     -n %{name}+toml-devel
Summary:        Read and parse configuration file automatically
BuildArch:      noarch
%description -n %{name}+toml-devel

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%package     -n %{name}+toml-crate-devel
Summary:        Read and parse configuration file automatically
BuildArch:      noarch
%description -n %{name}+toml-crate-devel

This package contains library source intended for building other packages which
use the "toml-crate" feature of the "%{crate}" crate.

%package     -n %{name}+xml-devel
Summary:        Read and parse configuration file automatically
BuildArch:      noarch
%description -n %{name}+xml-devel

This package contains library source intended for building other packages which
use the "xml" feature of the "%{crate}" crate.

%package     -n %{name}+yaml-devel
Summary:        Read and parse configuration file automatically
BuildArch:      noarch
%description -n %{name}+yaml-devel

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp %{SOURCE1} LICENSE   #we have to add the LICENSE file manually since upstream doesn't include it
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
%files -n rust-config-file-devel -f %{oreon_filedir}/rust-config-file-devel.list

%changelog

%autochangelog
