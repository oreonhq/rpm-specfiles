%global source0_hash 52e5938870db620c26a8f329f5735aa3450cedd30f4a4bb98475b1b076d8edae
%bcond check 1
%global debug_package %{nil}
%global crate bitvec_helpers
Name:           rust-bitvec_helpers
Version:        4.0.2
Release:        1%{?dist}
Summary:        BitVec based bitstream reader and writer
License:        MIT
URL:            https://crates.io/crates/bitvec_helpers
Source0:        https://static.crates.io/crates/bitvec_helpers/bitvec_helpers-%{version}.crate
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
Summary:        BitVec based bitstream reader and writer
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bitstream-io-devel
Summary:        BitVec based bitstream reader and writer
BuildArch:      noarch
%description -n %{name}+bitstream-io-devel

This package contains library source intended for building other packages which
use the "bitstream-io" feature of the "%{crate}" crate.

%package     -n %{name}+bitvec-devel
Summary:        BitVec based bitstream reader and writer
BuildArch:      noarch
%description -n %{name}+bitvec-devel

This package contains library source intended for building other packages which
use the "bitvec" feature of the "%{crate}" crate.

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
%files -n rust-bitvec_helpers-devel -f %{oreon_filedir}/rust-bitvec_helpers-devel.list

%changelog

%autochangelog
