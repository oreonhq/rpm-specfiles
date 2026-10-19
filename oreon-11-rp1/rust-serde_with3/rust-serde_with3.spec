%global source0_hash 8e28bdad6db2b8340e449f7108f020b3b092e8583a9e3fb82713e1d4e71fe817
%bcond check 0
%global debug_package %{nil}
%global crate serde_with
Name:           rust-serde_with3
Version:        3.11.0
Release:        1%{?dist}
Summary:        Custom de/serialization functions for Rust's serde
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_with
Source0:        https://static.crates.io/crates/serde_with/serde_with-%{version}.crate
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
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+chrono_0_4-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+chrono_0_4-devel

This package contains library source intended for building other packages which
use the "chrono_0_4" feature of the "%{crate}" crate.

%package     -n %{name}+doc-comment-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+doc-comment-devel

This package contains library source intended for building other packages which
use the "doc-comment" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+guide-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+guide-devel

This package contains library source intended for building other packages which
use the "guide" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown_0_14-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+hashbrown_0_14-devel

This package contains library source intended for building other packages which
use the "hashbrown_0_14" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown_0_15-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+hashbrown_0_15-devel

This package contains library source intended for building other packages which
use the "hashbrown_0_15" feature of the "%{crate}" crate.

%package     -n %{name}+hex-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+hex-devel

This package contains library source intended for building other packages which
use the "hex" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap_1-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+indexmap_1-devel

This package contains library source intended for building other packages which
use the "indexmap_1" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap_2-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+indexmap_2-devel

This package contains library source intended for building other packages which
use the "indexmap_2" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+schemars_0_8-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+schemars_0_8-devel

This package contains library source intended for building other packages which
use the "schemars_0_8" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+serde_with_macros-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+serde_with_macros-devel

This package contains library source intended for building other packages which
use the "serde_with_macros" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+time_0_3-devel
Summary:        Custom de/serialization functions for Rust's serde
BuildArch:      noarch
%description -n %{name}+time_0_3-devel

This package contains library source intended for building other packages which
use the "time_0_3" feature of the "%{crate}" crate.

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
%files -n rust-serde_with3-devel -f %{oreon_filedir}/rust-serde_with3-devel.list

%changelog

%autochangelog
