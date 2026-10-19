%global source0_hash a52d3a8bfc85f250440e4424db7d857e241a3aebbbe301f3eb606ab15c39acbf
%bcond check 0
%global debug_package %{nil}
%global crate libflate_lz77
Name:           rust-libflate_lz77_1
Version:        1.2.0
Release:        1%{?dist}
Summary:        LZ77 encoder for libflate crate
License:        MIT
URL:            https://crates.io/crates/libflate_lz77
Source0:        https://static.crates.io/crates/libflate_lz77/libflate_lz77-%{version}.crate
Patch:          libflate_lz77-fix-metadata.diff
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
Summary:        LZ77 encoder for libflate crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-libflate_lz77_1-devel -f %{oreon_filedir}/rust-libflate_lz77_1-devel.list

%changelog

%autochangelog
