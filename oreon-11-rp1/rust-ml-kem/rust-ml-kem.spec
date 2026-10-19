%global source0_hash 5e15f3e5b957493873e396a66914e83e616b6afe335cdef7efe5c6e1216aba66
%bcond check 0
%global debug_package %{nil}
%global crate ml-kem
Name:           rust-ml-kem
Version:        0.3.2
Release:        1%{?dist}
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulatio...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ml-kem
Source0:        https://static.crates.io/crates/ml-kem/ml-kem-%{version}.crate
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
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulatio...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulatio...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+const-oid-devel
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulatio...
BuildArch:      noarch
%description -n %{name}+const-oid-devel

This package contains library source intended for building other packages which
use the "const-oid" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulatio...
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+hazmat-devel
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulatio...
BuildArch:      noarch
%description -n %{name}+hazmat-devel

This package contains library source intended for building other packages which
use the "hazmat" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulatio...
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs8-devel
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulatio...
BuildArch:      noarch
%description -n %{name}+pkcs8-devel

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Pure Rust implementation of the Module-Lattice-Based Key-Encapsulatio...
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-ml-kem-devel -f %{oreon_filedir}/rust-ml-kem-devel.list

%changelog

%autochangelog
