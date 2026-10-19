%global source0_hash a38c5e5bbaa10cc256774ea394ad62968c31c0e3c3265f65221e02c87dd1a914
%bcond check 0
%global debug_package %{nil}
%global crate serde-sarif
Name:           rust-serde-sarif
Version:        0.5.0
Release:        1%{?dist}
Summary:        Serde serialization for SARIF files
License:        MIT
URL:            https://crates.io/crates/serde-sarif
Source0:        https://static.crates.io/crates/serde-sarif/serde-sarif-%{version}.crate
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
Summary:        Serde serialization for SARIF files
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cargo_metadata-devel
Summary:        Serde serialization for SARIF files
BuildArch:      noarch
%description -n %{name}+cargo_metadata-devel

This package contains library source intended for building other packages which
use the "cargo_metadata" feature of the "%{crate}" crate.

%package     -n %{name}+clang-tidy-converters-devel
Summary:        Serde serialization for SARIF files
BuildArch:      noarch
%description -n %{name}+clang-tidy-converters-devel

This package contains library source intended for building other packages which
use the "clang-tidy-converters" feature of the "%{crate}" crate.

%package     -n %{name}+clippy-converters-devel
Summary:        Serde serialization for SARIF files
BuildArch:      noarch
%description -n %{name}+clippy-converters-devel

This package contains library source intended for building other packages which
use the "clippy-converters" feature of the "%{crate}" crate.

%package     -n %{name}+hadolint-converters-devel
Summary:        Serde serialization for SARIF files
BuildArch:      noarch
%description -n %{name}+hadolint-converters-devel

This package contains library source intended for building other packages which
use the "hadolint-converters" feature of the "%{crate}" crate.

%package     -n %{name}+regex-devel
Summary:        Serde serialization for SARIF files
BuildArch:      noarch
%description -n %{name}+regex-devel

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%package     -n %{name}+shellcheck-converters-devel
Summary:        Serde serialization for SARIF files
BuildArch:      noarch
%description -n %{name}+shellcheck-converters-devel

This package contains library source intended for building other packages which
use the "shellcheck-converters" feature of the "%{crate}" crate.

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
%files -n rust-serde-sarif-devel -f %{oreon_filedir}/rust-serde-sarif-devel.list

%changelog

%autochangelog
