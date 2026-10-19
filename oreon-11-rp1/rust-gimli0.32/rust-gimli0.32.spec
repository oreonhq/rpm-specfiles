%global source0_hash e629b9b98ef3dd8afe6ca2bd0f89306cec16d43d907889945bc5d6687f2f13c7
%bcond check 1
%global debug_package %{nil}
%global crate gimli
Name:           rust-gimli0.32
Version:        0.32.3
Release:        1%{?dist}
Summary:        Library for reading and writing the DWARF debugging format
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gimli
Source0:        https://static.crates.io/crates/gimli/gimli-%{version}.crate
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
Summary:        Library for reading and writing the DWARF debugging format
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+endian-reader-devel
Summary:        Library for reading and writing the DWARF debugging format
BuildArch:      noarch
%description -n %{name}+endian-reader-devel

This package contains library source intended for building other packages which
use the "endian-reader" feature of the "%{crate}" crate.

%package     -n %{name}+fallible-iterator-devel
Summary:        Library for reading and writing the DWARF debugging format
BuildArch:      noarch
%description -n %{name}+fallible-iterator-devel

This package contains library source intended for building other packages which
use the "fallible-iterator" feature of the "%{crate}" crate.

%package     -n %{name}+read-devel
Summary:        Library for reading and writing the DWARF debugging format
BuildArch:      noarch
%description -n %{name}+read-devel

This package contains library source intended for building other packages which
use the "read" feature of the "%{crate}" crate.

%package     -n %{name}+read-all-devel
Summary:        Library for reading and writing the DWARF debugging format
BuildArch:      noarch
%description -n %{name}+read-all-devel

This package contains library source intended for building other packages which
use the "read-all" feature of the "%{crate}" crate.

%package     -n %{name}+read-core-devel
Summary:        Library for reading and writing the DWARF debugging format
BuildArch:      noarch
%description -n %{name}+read-core-devel

This package contains library source intended for building other packages which
use the "read-core" feature of the "%{crate}" crate.

%package     -n %{name}+rustc-dep-of-std-devel
Summary:        Library for reading and writing the DWARF debugging format
BuildArch:      noarch
%description -n %{name}+rustc-dep-of-std-devel

This package contains library source intended for building other packages which
use the "rustc-dep-of-std" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Library for reading and writing the DWARF debugging format
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+write-devel
Summary:        Library for reading and writing the DWARF debugging format
BuildArch:      noarch
%description -n %{name}+write-devel

This package contains library source intended for building other packages which
use the "write" feature of the "%{crate}" crate.

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
%files -n rust-gimli0.32-devel -f %{oreon_filedir}/rust-gimli0.32-devel.list

%changelog

%autochangelog
