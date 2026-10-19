%global source3_hash f9c375a1be4a41f7b70301dd83c91cb89e41567478859b77eef375a52d782505
%global source2_hash c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
%global source0_hash 16c2f82143577edb4921b71ede051dac62ca3c16084e918bf7b40c96ae10eb33
%bcond check 1
%global debug_package %{nil}
%global crate self_cell
Name:           rust-self_cell
Version:        1.2.1
Release:        1%{?dist}
Summary:        Safe-to-use proc-macro-free self-referential structs in stable Rust
License:        Apache-2.0 OR GPL-2.0-only
URL:            https://crates.io/crates/self_cell
Source0:        https://static.crates.io/crates/self_cell/self_cell-%{version}.crate
Source2:        https://raw.githubusercontent.com/Voultapher/self_cell/refs/tags/v%{version}/LICENSE-APACHE
Source3:        https://raw.githubusercontent.com/Voultapher/self_cell/refs/tags/v%{version}/LICENSE-GPLv2
Patch:          self_cell-fix-metadata.diff
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
Summary:        Safe-to-use proc-macro-free self-referential structs in stable Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+old_rust-devel
Summary:        Safe-to-use proc-macro-free self-referential structs in stable Rust
BuildArch:      noarch
%description -n %{name}+old_rust-devel

This package contains library source intended for building other packages which
use the "old_rust" feature of the "%{crate}" crate.

%package     -n %{name}+rustversion-devel
Summary:        Safe-to-use proc-macro-free self-referential structs in stable Rust
BuildArch:      noarch
%description -n %{name}+rustversion-devel

This package contains library source intended for building other packages which
use the "rustversion" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{SOURCE2} %{SOURCE3} .
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
cp -p LICENSE-* %{buildroot}%{crate_instdir}/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-self_cell-devel -f %{oreon_filedir}/rust-self_cell-devel.list

%changelog

%autochangelog
