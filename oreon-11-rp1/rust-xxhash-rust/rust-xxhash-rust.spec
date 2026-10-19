%global source0_hash aee1b19627c7c60102ab80d3a9cbe18de90bfe03bfa6c3715447681f0e8c8af6
%bcond check 0
%global debug_package %{nil}
%global crate xxhash-rust
Name:           rust-xxhash-rust
Version:        0.8.18
Release:        1%{?dist}
Summary:        Implementation of xxhash
License:        BSL-1.0
URL:            https://crates.io/crates/xxhash-rust
Source0:        https://static.crates.io/crates/xxhash-rust/xxhash-rust-%{version}.crate
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

%package     -n %{name}+const_xxh3-devel
Summary:        Implementation of xxhash
BuildArch:      noarch
%description -n %{name}+const_xxh3-devel

This package contains library source intended for building other packages which
use the "const_xxh3" feature of the "%{crate}" crate.

%package     -n %{name}+const_xxh32-devel
Summary:        Implementation of xxhash
BuildArch:      noarch
%description -n %{name}+const_xxh32-devel

This package contains library source intended for building other packages which
use the "const_xxh32" feature of the "%{crate}" crate.

%package     -n %{name}+const_xxh64-devel
Summary:        Implementation of xxhash
BuildArch:      noarch
%description -n %{name}+const_xxh64-devel

This package contains library source intended for building other packages which
use the "const_xxh64" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Implementation of xxhash
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+xxh3-devel
Summary:        Implementation of xxhash
BuildArch:      noarch
%description -n %{name}+xxh3-devel

This package contains library source intended for building other packages which
use the "xxh3" feature of the "%{crate}" crate.

%package     -n %{name}+xxh32-devel
Summary:        Implementation of xxhash
BuildArch:      noarch
%description -n %{name}+xxh32-devel

This package contains library source intended for building other packages which
use the "xxh32" feature of the "%{crate}" crate.

%package     -n %{name}+xxh64-devel
Summary:        Implementation of xxhash
BuildArch:      noarch
%description -n %{name}+xxh64-devel

This package contains library source intended for building other packages which
use the "xxh64" feature of the "%{crate}" crate.

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
%files -n rust-xxhash-rust-devel -f %{oreon_filedir}/rust-xxhash-rust-devel.list

%changelog

%autochangelog
