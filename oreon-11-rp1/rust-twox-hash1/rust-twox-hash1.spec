%global source0_hash 97fee6b57c6a41524a810daee9286c02d7752c4253064d0b05472833a438f675
%bcond check 1
%global debug_package %{nil}
%global crate twox-hash
Name:           rust-twox-hash1
Version:        1.6.3
Release:        1%{?dist}
Summary:        Rust implementation of the XXHash and XXH3 algorithms
License:        MIT
URL:            https://crates.io/crates/twox-hash
Source0:        https://static.crates.io/crates/twox-hash/twox-hash-%{version}.crate
Patch:          twox-hash-fix-metadata.diff
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
Summary:        Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+digest_0_10-devel
Summary:        Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+digest_0_10-devel

This package contains library source intended for building other packages which
use the "digest_0_10" feature of the "%{crate}" crate.

%package     -n %{name}+digest_0_9-devel
Summary:        Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+digest_0_9-devel

This package contains library source intended for building other packages which
use the "digest_0_9" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-twox-hash1-devel -f %{oreon_filedir}/rust-twox-hash1-devel.list

%changelog

%autochangelog
