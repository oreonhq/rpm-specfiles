%global source0_hash eedd8c64460676101062f9f2ecdeb52d8f43e622da6a6c5bf5158f4ef08b0906
%bcond check 1
%global debug_package %{nil}
%global crate igvm_defs
Name:           rust-igvm_defs
Version:        0.4.0
Release:        1%{?dist}
Summary:        Igvm_defs crate is the specification for the Independent Guest Virtual Machine
License:        MIT
URL:            https://crates.io/crates/igvm_defs
Source0:        https://static.crates.io/crates/igvm_defs/igvm_defs-%{version}.crate
Patch:          igvm_defs-fix-metadata.diff
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
Summary:        Igvm_defs crate is the specification for the Independent Guest Virtual Machine
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Igvm_defs crate is the specification for the Independent Guest Virtual Machine
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-igvm_defs-devel -f %{oreon_filedir}/rust-igvm_defs-devel.list

%changelog

%autochangelog
