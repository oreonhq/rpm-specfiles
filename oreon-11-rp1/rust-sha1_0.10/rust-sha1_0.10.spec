%global source0_hash a978451301f4db1d02937a4ab3ccce137717b81826e79b7d49ffe3244a13c3b8
%bcond check 1
%global debug_package %{nil}
%global crate sha1
Name:           rust-sha1_0.10
Version:        0.10.7
Release:        1%{?dist}
Summary:        SHA-1 hash function
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sha1
Source0:        https://static.crates.io/crates/sha1/sha1-%{version}.crate
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

%package     -n %{name}+loongarch64_asm-devel
Summary:        SHA-1 hash function
BuildArch:      noarch
%description -n %{name}+loongarch64_asm-devel

This package contains library source intended for building other packages which
use the "loongarch64_asm" feature of the "%{crate}" crate.

%package     -n %{name}+oid-devel
Summary:        SHA-1 hash function
BuildArch:      noarch
%description -n %{name}+oid-devel

This package contains library source intended for building other packages which
use the "oid" feature of the "%{crate}" crate.

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
%files -n rust-sha1_0.10-devel -f %{oreon_filedir}/rust-sha1_0.10-devel.list

%changelog

%autochangelog
