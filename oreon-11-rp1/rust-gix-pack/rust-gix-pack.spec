%global source0_hash 3d199d515cbdcf05f531f3859be9771fc12acac7b7fe0f5b581b2c1ab1c3a61e
%bcond check 0
%global debug_package %{nil}
%global crate gix-pack
Name:           rust-gix-pack
Version:        0.74.2
Release:        1%{?dist}
Summary:        Implements git packs and related data structures
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-pack
Source0:        https://static.crates.io/crates/gix-pack/gix-pack-%{version}.crate
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
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+generate-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+generate-devel

This package contains library source intended for building other packages which
use the "generate" feature of the "%{crate}" crate.

%package     -n %{name}+object-cache-dynamic-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+object-cache-dynamic-devel

This package contains library source intended for building other packages which
use the "object-cache-dynamic" feature of the "%{crate}" crate.

%package     -n %{name}+pack-cache-lru-dynamic-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+pack-cache-lru-dynamic-devel

This package contains library source intended for building other packages which
use the "pack-cache-lru-dynamic" feature of the "%{crate}" crate.

%package     -n %{name}+pack-cache-lru-static-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+pack-cache-lru-static-devel

This package contains library source intended for building other packages which
use the "pack-cache-lru-static" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha256-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+sha256-devel

This package contains library source intended for building other packages which
use the "sha256" feature of the "%{crate}" crate.

%package     -n %{name}+streaming-input-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+streaming-input-devel

This package contains library source intended for building other packages which
use the "streaming-input" feature of the "%{crate}" crate.

%package     -n %{name}+testing-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+testing-devel

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+wasm-devel

This package contains library source intended for building other packages which
use the "wasm" feature of the "%{crate}" crate.

%prep
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
%files -n rust-gix-pack-devel -f %{oreon_filedir}/rust-gix-pack-devel.list

%changelog

%autochangelog
