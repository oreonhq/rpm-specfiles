%global source0_hash c1348164456f72ca0116e4538bdaabb0ddb622c7d9f16387c725af3e96d6001c
%bcond check 0
%global debug_package %{nil}
%global crate simplelog
Name:           rust-simplelog0.11
Version:        0.11.2
Release:        1%{?dist}
Summary:        Simple and easy-to-use logging facility for Rust's log crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/simplelog
Source0:        https://static.crates.io/crates/simplelog/simplelog-%{version}.crate
Patch:          simplelog-fix-metadata.diff
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
Summary:        Simple and easy-to-use logging facility for Rust's log crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ansi_term-devel
Summary:        Simple and easy-to-use logging facility for Rust's log crate
BuildArch:      noarch
%description -n %{name}+ansi_term-devel

This package contains library source intended for building other packages which
use the "ansi_term" feature of the "%{crate}" crate.

%package     -n %{name}+paris-devel
Summary:        Simple and easy-to-use logging facility for Rust's log crate
BuildArch:      noarch
%description -n %{name}+paris-devel

This package contains library source intended for building other packages which
use the "paris" feature of the "%{crate}" crate.

%package     -n %{name}+termcolor-devel
Summary:        Simple and easy-to-use logging facility for Rust's log crate
BuildArch:      noarch
%description -n %{name}+termcolor-devel

This package contains library source intended for building other packages which
use the "termcolor" feature of the "%{crate}" crate.

%package     -n %{name}+test-devel
Summary:        Simple and easy-to-use logging facility for Rust's log crate
BuildArch:      noarch
%description -n %{name}+test-devel

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

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
%files -n rust-simplelog0.11-devel -f %{oreon_filedir}/rust-simplelog0.11-devel.list

%changelog

%autochangelog
