%global source0_hash a7507d819769d01a365ab707794a4084392c824f54a7a6a7862f8c3d0892b283
%bcond check 0
%global debug_package %{nil}
%global crate sha2
Name:           rust-sha2
Version:        0.10.9
Release:        1%{?dist}
Summary:        Pure Rust implementation of the SHA-2 hash function family
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sha2
Source0:        https://static.crates.io/crates/sha2/sha2-%{version}.crate
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
Summary:        Pure Rust implementation of the SHA-2 hash function family
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+asm-devel
Summary:        Pure Rust implementation of the SHA-2 hash function family
BuildArch:      noarch
%description -n %{name}+asm-devel

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

%package     -n %{name}+asm-aarch64-devel
Summary:        Pure Rust implementation of the SHA-2 hash function family
BuildArch:      noarch
%description -n %{name}+asm-aarch64-devel

This package contains library source intended for building other packages which
use the "asm-aarch64" feature of the "%{crate}" crate.

%package     -n %{name}+compress-devel
Summary:        Pure Rust implementation of the SHA-2 hash function family
BuildArch:      noarch
%description -n %{name}+compress-devel

This package contains library source intended for building other packages which
use the "compress" feature of the "%{crate}" crate.

%package     -n %{name}+force-soft-devel
Summary:        Pure Rust implementation of the SHA-2 hash function family
BuildArch:      noarch
%description -n %{name}+force-soft-devel

This package contains library source intended for building other packages which
use the "force-soft" feature of the "%{crate}" crate.

%package     -n %{name}+force-soft-compact-devel
Summary:        Pure Rust implementation of the SHA-2 hash function family
BuildArch:      noarch
%description -n %{name}+force-soft-compact-devel

This package contains library source intended for building other packages which
use the "force-soft-compact" feature of the "%{crate}" crate.

%package     -n %{name}+loongarch64_asm-devel
Summary:        Pure Rust implementation of the SHA-2 hash function family
BuildArch:      noarch
%description -n %{name}+loongarch64_asm-devel

This package contains library source intended for building other packages which
use the "loongarch64_asm" feature of the "%{crate}" crate.

%package     -n %{name}+oid-devel
Summary:        Pure Rust implementation of the SHA-2 hash function family
BuildArch:      noarch
%description -n %{name}+oid-devel

This package contains library source intended for building other packages which
use the "oid" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of the SHA-2 hash function family
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
%files -n rust-sha2-devel -f %{oreon_filedir}/rust-sha2-devel.list

%changelog

%autochangelog
