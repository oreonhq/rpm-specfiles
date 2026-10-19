%global source0_hash 8464ec13c3691491391d9fce00f6416c9a48e46972f72d7865688be2080192c9
%bcond check 0
%global debug_package %{nil}
%global crate twox-hash
Name:           rust-twox-hash
Version:        2.1.3
Release:        2%{?dist}
Summary:        A Rust implementation of the XXHash and XXH3 algorithms
License:        MIT
URL:            https://crates.io/crates/twox-hash
Source0:        https://static.crates.io/crates/twox-hash/twox-hash-%{version}.crate
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
Summary:        A Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+random-devel
Summary:        A Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+random-devel

This package contains library source intended for building other packages which
use the "random" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        A Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+xxhash32-devel
Summary:        A Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+xxhash32-devel

This package contains library source intended for building other packages which
use the "xxhash32" feature of the "%{crate}" crate.

%package     -n %{name}+xxhash3_128-devel
Summary:        A Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+xxhash3_128-devel

This package contains library source intended for building other packages which
use the "xxhash3_128" feature of the "%{crate}" crate.

%package     -n %{name}+xxhash3_64-devel
Summary:        A Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+xxhash3_64-devel

This package contains library source intended for building other packages which
use the "xxhash3_64" feature of the "%{crate}" crate.

%package     -n %{name}+xxhash64-devel
Summary:        A Rust implementation of the XXHash and XXH3 algorithms
BuildArch:      noarch
%description -n %{name}+xxhash64-devel

This package contains library source intended for building other packages which
use the "xxhash64" feature of the "%{crate}" crate.

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
%files -n rust-twox-hash-devel -f %{oreon_filedir}/rust-twox-hash-devel.list

%changelog

%autochangelog
