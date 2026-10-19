%global source0_hash 841d1cc9bed7f9236f321df977030373f4a4163ae1a7dbfe1a51a2c1a51d9100
%bcond check 0
%global debug_package %{nil}
%global crate hashbrown
Name:           rust-hashbrown0.16
Version:        0.16.1
Release:        1%{?dist}
Summary:        A Rust port of Google's SwissTable hash map
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hashbrown
Source0:        https://static.crates.io/crates/hashbrown/hashbrown-%{version}.crate
Patch:          hashbrown-fix-metadata-auto.diff
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
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+allocator-api2-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+allocator-api2-devel

This package contains library source intended for building other packages which
use the "allocator-api2" feature of the "%{crate}" crate.

%package     -n %{name}+core-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+core-devel

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%package     -n %{name}+default-hasher-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+default-hasher-devel

This package contains library source intended for building other packages which
use the "default-hasher" feature of the "%{crate}" crate.

%package     -n %{name}+equivalent-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+equivalent-devel

This package contains library source intended for building other packages which
use the "equivalent" feature of the "%{crate}" crate.

%package     -n %{name}+inline-more-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+inline-more-devel

This package contains library source intended for building other packages which
use the "inline-more" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+raw-entry-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+raw-entry-devel

This package contains library source intended for building other packages which
use the "raw-entry" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+rustc-dep-of-std-devel

This package contains library source intended for building other packages which
use the "rustc-dep-of-std" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-internal-api-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+rustc-internal-api-devel

This package contains library source intended for building other packages which
use the "rustc-internal-api" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A Rust port of Google's SwissTable hash map
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-hashbrown0.16-devel -f %{oreon_filedir}/rust-hashbrown0.16-devel.list

%changelog

%autochangelog

