%global source0_hash b36c5bae69f304b5f448177d08dfb485dac81742d22e460ddbdfcf408fa38b97
%bcond check 1
%global debug_package %{nil}
%global crate fat-macho
Name:           rust-fat-macho0.4
Version:        0.4.12
Release:        1%{?dist}
Summary:        Mach-O Fat Binary Reader and Writer
License:        MIT
URL:            https://crates.io/crates/fat-macho
Source0:        https://static.crates.io/crates/fat-macho/fat-macho-%{version}.crate
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
Summary:        Mach-O Fat Binary Reader and Writer
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bitcode-devel
Summary:        Mach-O Fat Binary Reader and Writer
BuildArch:      noarch
%description -n %{name}+bitcode-devel

This package contains library source intended for building other packages which
use the "bitcode" feature of the "%{crate}" crate.

%package     -n %{name}+llvm-bitcode-devel
Summary:        Mach-O Fat Binary Reader and Writer
BuildArch:      noarch
%description -n %{name}+llvm-bitcode-devel

This package contains library source intended for building other packages which
use the "llvm-bitcode" feature of the "%{crate}" crate.

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
%files -n rust-fat-macho0.4-devel -f %{oreon_filedir}/rust-fat-macho0.4-devel.list

%changelog

%autochangelog
