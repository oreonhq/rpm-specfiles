%global source0_hash 5f20c57d8d7db6d3b86154206ae5d8fba62dd39573114de97c2cb0578251f8e1
%bcond check 0
%global debug_package %{nil}
%global crate webpki-roots
Name:           rust-webpki-roots
Version:        0.25.4
Release:        1%{?dist}
Summary:        Mozilla's CA root certificates for use with webpki
License:        MPL-2.0
URL:            https://crates.io/crates/webpki-roots
Source0:        https://static.crates.io/crates/webpki-roots/webpki-roots-%{version}.crate
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
Summary:        Mozilla's CA root certificates for use with webpki
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
%files -n rust-webpki-roots-devel -f %{oreon_filedir}/rust-webpki-roots-devel.list

%changelog

%autochangelog
