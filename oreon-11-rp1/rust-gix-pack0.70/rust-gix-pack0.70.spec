%global source0_hash daf02e6f5c8f07a069c9ea5245f40d9b14856ada4086091dc99941b49002b4fa
%bcond check 0
%global debug_package %{nil}
%global crate gix-pack
Name:           rust-gix-pack0.70
Version:        0.70.0
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

%package     -n %{name}+clru-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+clru-devel

This package contains library source intended for building other packages which
use the "clru" feature of the "%{crate}" crate.

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

%package     -n %{name}+gix-diff-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+gix-diff-devel

This package contains library source intended for building other packages which
use the "gix-diff" feature of the "%{crate}" crate.

%package     -n %{name}+gix-hashtable-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+gix-hashtable-devel

This package contains library source intended for building other packages which
use the "gix-hashtable" feature of the "%{crate}" crate.

%package     -n %{name}+gix-traverse-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+gix-traverse-devel

This package contains library source intended for building other packages which
use the "gix-traverse" feature of the "%{crate}" crate.

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

%package     -n %{name}+parking_lot-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

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

%package     -n %{name}+streaming-input-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+streaming-input-devel

This package contains library source intended for building other packages which
use the "streaming-input" feature of the "%{crate}" crate.

%package     -n %{name}+uluru-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+uluru-devel

This package contains library source intended for building other packages which
use the "uluru" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-devel
Summary:        Implements git packs and related data structures
BuildArch:      noarch
%description -n %{name}+wasm-devel

This package contains library source intended for building other packages which
use the "wasm" feature of the "%{crate}" crate.

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
%files -n rust-gix-pack0.70-devel -f %{oreon_filedir}/rust-gix-pack0.70-devel.list

%changelog

%autochangelog
