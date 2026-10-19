%global source0_hash 6764c3b5dd454e283a30e6dfe78e9b31096d9e32036b5d1eaac7a6119ccb9a24
%bcond check 0
%global debug_package %{nil}
%global crate postcard
Name:           rust-postcard
Version:        1.1.3
Release:        1%{?dist}
Summary:        A no_std + serde compatible message library for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/postcard
Source0:        https://static.crates.io/crates/postcard/postcard-%{version}.crate
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
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+core-num-saturating-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+core-num-saturating-devel

This package contains library source intended for building other packages which
use the "core-num-saturating" feature of the "%{crate}" crate.

%package     -n %{name}+crc-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+crc-devel

This package contains library source intended for building other packages which
use the "crc" feature of the "%{crate}" crate.

%package     -n %{name}+defmt-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+defmt-devel

This package contains library source intended for building other packages which
use the "defmt" feature of the "%{crate}" crate.

%package     -n %{name}+embedded-io-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+embedded-io-devel

This package contains library source intended for building other packages which
use the "embedded-io" feature of the "%{crate}" crate.

%package     -n %{name}+embedded-io-04-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+embedded-io-04-devel

This package contains library source intended for building other packages which
use the "embedded-io-04" feature of the "%{crate}" crate.

%package     -n %{name}+embedded-io-06-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+embedded-io-06-devel

This package contains library source intended for building other packages which
use the "embedded-io-06" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-derive-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+experimental-derive-devel

This package contains library source intended for building other packages which
use the "experimental-derive" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-cas-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+heapless-cas-devel

This package contains library source intended for building other packages which
use the "heapless-cas" feature of the "%{crate}" crate.

%package     -n %{name}+nalgebra-v0_33-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+nalgebra-v0_33-devel

This package contains library source intended for building other packages which
use the "nalgebra-v0_33" feature of the "%{crate}" crate.

%package     -n %{name}+nalgebra_v0_33-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+nalgebra_v0_33-devel

This package contains library source intended for building other packages which
use the "nalgebra_v0_33" feature of the "%{crate}" crate.

%package     -n %{name}+paste-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+paste-devel

This package contains library source intended for building other packages which
use the "paste" feature of the "%{crate}" crate.

%package     -n %{name}+postcard-derive-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+postcard-derive-devel

This package contains library source intended for building other packages which
use the "postcard-derive" feature of the "%{crate}" crate.

%package     -n %{name}+use-crc-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+use-crc-devel

This package contains library source intended for building other packages which
use the "use-crc" feature of the "%{crate}" crate.

%package     -n %{name}+use-defmt-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+use-defmt-devel

This package contains library source intended for building other packages which
use the "use-defmt" feature of the "%{crate}" crate.

%package     -n %{name}+use-std-devel
Summary:        A no_std + serde compatible message library for Rust
BuildArch:      noarch
%description -n %{name}+use-std-devel

This package contains library source intended for building other packages which
use the "use-std" feature of the "%{crate}" crate.

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
%files -n rust-postcard-devel -f %{oreon_filedir}/rust-postcard-devel.list

%changelog

%autochangelog
