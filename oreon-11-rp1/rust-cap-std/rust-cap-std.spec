%global source0_hash b6dc3090992a735d23219de5c204927163d922f42f575a0189b005c62d37549a
%bcond check 0
%global debug_package %{nil}
%global crate cap-std
Name:           rust-cap-std
Version:        3.4.5
Release:        1%{?dist}
Summary:        Capability-based version of the Rust standard library
License:        Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/cap-std
Source0:        https://static.crates.io/crates/cap-std/cap-std-%{version}.crate
Patch:          cap-std-fix-metadata-auto.diff
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
Summary:        Capability-based version of the Rust standard library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arf-strings-devel
Summary:        Capability-based version of the Rust standard library
BuildArch:      noarch
%description -n %{name}+arf-strings-devel

This package contains library source intended for building other packages which
use the "arf-strings" feature of the "%{crate}" crate.

%package     -n %{name}+arf_strings-devel
Summary:        Capability-based version of the Rust standard library
BuildArch:      noarch
%description -n %{name}+arf_strings-devel

This package contains library source intended for building other packages which
use the "arf_strings" feature of the "%{crate}" crate.

%package     -n %{name}+camino-devel
Summary:        Capability-based version of the Rust standard library
BuildArch:      noarch
%description -n %{name}+camino-devel

This package contains library source intended for building other packages which
use the "camino" feature of the "%{crate}" crate.

%package     -n %{name}+fs_utf8-devel
Summary:        Capability-based version of the Rust standard library
BuildArch:      noarch
%description -n %{name}+fs_utf8-devel

This package contains library source intended for building other packages which
use the "fs_utf8" feature of the "%{crate}" crate.

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
%files -n rust-cap-std-devel -f %{oreon_filedir}/rust-cap-std-devel.list

%changelog

%autochangelog
