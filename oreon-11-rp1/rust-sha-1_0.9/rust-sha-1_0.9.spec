%global source0_hash 99cd6713db3cf16b6c84e06321e049a9b9f699826e16096d23bbcc44d15d51a6
%bcond check 1
%global debug_package %{nil}
%global crate sha-1
Name:           rust-sha-1_0.9
Version:        0.9.8
Release:        1%{?dist}
Summary:        SHA-1 hash function
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sha-1
Source0:        https://static.crates.io/crates/sha-1/sha-1-%{version}.crate
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
Summary:        SHA-1 hash function
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+asm-devel
Summary:        SHA-1 hash function
BuildArch:      noarch
%description -n %{name}+asm-devel

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

%package     -n %{name}+asm-aarch64-devel
Summary:        SHA-1 hash function
BuildArch:      noarch
%description -n %{name}+asm-aarch64-devel

This package contains library source intended for building other packages which
use the "asm-aarch64" feature of the "%{crate}" crate.

%package     -n %{name}+compress-devel
Summary:        SHA-1 hash function
BuildArch:      noarch
%description -n %{name}+compress-devel

This package contains library source intended for building other packages which
use the "compress" feature of the "%{crate}" crate.

%package     -n %{name}+force-soft-devel
Summary:        SHA-1 hash function
BuildArch:      noarch
%description -n %{name}+force-soft-devel

This package contains library source intended for building other packages which
use the "force-soft" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-asm-devel
Summary:        SHA-1 hash function
BuildArch:      noarch
%description -n %{name}+sha1-asm-devel

This package contains library source intended for building other packages which
use the "sha1-asm" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        SHA-1 hash function
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
%files -n rust-sha-1_0.9-devel -f %{oreon_filedir}/rust-sha-1_0.9-devel.list

%changelog

%autochangelog
