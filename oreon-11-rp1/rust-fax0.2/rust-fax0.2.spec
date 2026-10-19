%global source0_hash caf1079563223d5d59d83c85886a56e586cfd5c1a26292e971a0fa266531ac5a
%bcond check 0
%global debug_package %{nil}
%global crate fax
Name:           rust-fax0.2
Version:        0.2.7
Release:        1%{?dist}
Summary:        Decoder and Encoder for CCITT Group 3 and 4 bi-level image encodings used by fax machines TIFF and PDF
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

%package     -n %{name}+default-devel
Summary:        Decoder and Encoder for CCITT Group 3 and 4 bi-level image encodings used by fax machines TIFF and PDF
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Decoder and Encoder for CCITT Group 3 and 4 bi-level image encodings used by fax machines TIFF and PDF
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+generate_bitmaps-devel
Summary:        Decoder and Encoder for CCITT Group 3 and 4 bi-level image encodings used by fax machines TIFF and PDF
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
%files -n rust-fax0.2-devel -f %{oreon_filedir}/rust-fax0.2-devel.list

%changelog

%autochangelog
