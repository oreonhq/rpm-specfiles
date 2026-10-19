%global source0_hash 04113cb9355a377d83f06ef1f0a45b8ab8cd7d8b1288160717d66df5c7988d27
%bcond check 1
%global debug_package %{nil}
%global crate rust-embed
Name:           rust-rust-embed
Version:        8.11.0
Release:        1%{?dist}
Summary:        Custom Derive Macro which loads files into the rust binary
License:        MIT
URL:            https://crates.io/crates/rust-embed
Source0:        https://static.crates.io/crates/rust-embed/rust-embed-%{version}.crate
Patch:          rust-embed-fix-metadata.diff
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
Summary:        Custom Derive Macro which loads files into the rust binary
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-embed-devel
Summary:        Custom Derive Macro which loads files into the rust binary
BuildArch:      noarch
%description -n %{name}+debug-embed-devel

This package contains library source intended for building other packages which
use the "debug-embed" feature of the "%{crate}" crate.

%package     -n %{name}+deterministic-timestamps-devel
Summary:        Custom Derive Macro which loads files into the rust binary
BuildArch:      noarch
%description -n %{name}+deterministic-timestamps-devel

This package contains library source intended for building other packages which
use the "deterministic-timestamps" feature of the "%{crate}" crate.

%package     -n %{name}+hex-devel
Summary:        Custom Derive Macro which loads files into the rust binary
BuildArch:      noarch
%description -n %{name}+hex-devel

This package contains library source intended for building other packages which
use the "hex" feature of the "%{crate}" crate.

%package     -n %{name}+include-exclude-devel
Summary:        Custom Derive Macro which loads files into the rust binary
BuildArch:      noarch
%description -n %{name}+include-exclude-devel

This package contains library source intended for building other packages which
use the "include-exclude" feature of the "%{crate}" crate.

%package     -n %{name}+interpolate-folder-path-devel
Summary:        Custom Derive Macro which loads files into the rust binary
BuildArch:      noarch
%description -n %{name}+interpolate-folder-path-devel

This package contains library source intended for building other packages which
use the "interpolate-folder-path" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -r examples/
rm tests/mime_guess.rs
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rust-embed-devel -f %{oreon_filedir}/rust-rust-embed-devel.list

%changelog

%autochangelog
