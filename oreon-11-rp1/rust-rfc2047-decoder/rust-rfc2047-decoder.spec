%global source0_hash bc36545d1021456a751b573517cb52e8c339b2f662e6b2778ef629282678de29
%bcond check 0
%global debug_package %{nil}
%global crate rfc2047-decoder
Name:           rust-rfc2047-decoder
Version:        1.0.6
Release:        1%{?dist}
Summary:        Rust library for decoding RFC 2047 MIME Message Headers
License:        MIT
URL:            https://crates.io/crates/rfc2047-decoder
Source0:        https://static.crates.io/crates/rfc2047-decoder/rfc2047-decoder-%{version}.crate
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
Summary:        Rust library for decoding RFC 2047 MIME Message Headers
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
%files -n rust-rfc2047-decoder-devel -f %{oreon_filedir}/rust-rfc2047-decoder-devel.list

%changelog

%autochangelog
