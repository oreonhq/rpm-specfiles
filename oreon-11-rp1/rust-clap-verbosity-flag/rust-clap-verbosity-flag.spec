%global source0_hash 9d92b1fab272fe943881b77cc6e920d6543e5b1bfadbd5ed81c7c5a755742394
%bcond check 1
%global debug_package %{nil}
%global crate clap-verbosity-flag
Name:           rust-clap-verbosity-flag
Version:        3.0.4
Release:        1%{?dist}
Summary:        Easily add a --verbose flag to CLIs using Clap
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/clap-verbosity-flag
Source0:        https://static.crates.io/crates/clap-verbosity-flag/clap-verbosity-flag-%{version}.crate
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
Summary:        Easily add a --verbose flag to CLIs using Clap
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
%files -n rust-clap-verbosity-flag-devel -f %{oreon_filedir}/rust-clap-verbosity-flag-devel.list

%changelog

%autochangelog
