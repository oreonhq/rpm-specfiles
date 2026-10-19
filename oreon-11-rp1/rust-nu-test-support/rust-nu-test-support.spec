%global source0_hash 2ae36af2be5338110bfea1316051a2825a464447b01f9547f689fcaeb5f918f5
%bcond check 1
%global debug_package %{nil}
%global crate nu-test-support
Name:           rust-nu-test-support
Version:        0.99.1
Release:        1%{?dist}
Summary:        Support for writing Nushell tests
License:        MIT
URL:            https://crates.io/crates/nu-test-support
Source0:        https://static.crates.io/crates/nu-test-support/nu-test-support-%{version}.crate
Patch:          nu-test-support-fix-metadata.diff
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
Summary:        Support for writing Nushell tests
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

%{cargo_test -- -- --exact %{shrink:
    --skip playground::tests::current_working_directory_back_to_root_from_anywhere
    --skip playground::tests::current_working_directory_in_sandbox_directory_created
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-nu-test-support-devel -f %{oreon_filedir}/rust-nu-test-support-devel.list

%changelog

%autochangelog
