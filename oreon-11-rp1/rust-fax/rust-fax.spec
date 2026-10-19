%global source0_hash 70ed8646f3993cad0585c6669ffba6f7e5440a0bfb0a1f16600cae33ce7cf307
%bcond check 0
%global debug_package %{nil}
%global crate fax
Name:           rust-fax
Version:        0.3.0
Release:        1%{?dist}
Summary:        Decoder and Encoder for CCITT Group 3 and 4 bi-level image encodings...
License:        MIT
URL:            https://crates.io/crates/fax
Source0:        https://static.crates.io/crates/fax/fax-%{version}.crate
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

%package     -n %{name}+debug-devel
Summary:        Decoder and Encoder for CCITT Group 3 and 4 bi-level image encodings...
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+fax_derive-devel
Summary:        Decoder and Encoder for CCITT Group 3 and 4 bi-level image encodings...
BuildArch:      noarch
%description -n %{name}+fax_derive-devel

This package contains library source intended for building other packages which
use the "fax_derive" feature of the "%{crate}" crate.

%package     -n %{name}+generate_bitmaps-devel
Summary:        Decoder and Encoder for CCITT Group 3 and 4 bi-level image encodings...
BuildArch:      noarch
%description -n %{name}+generate_bitmaps-devel

This package contains library source intended for building other packages which
use the "generate_bitmaps" feature of the "%{crate}" crate.

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
%files -n rust-fax-devel -f %{oreon_filedir}/rust-fax-devel.list

%changelog

%autochangelog
