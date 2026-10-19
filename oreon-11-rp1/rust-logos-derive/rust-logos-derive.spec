%global source0_hash 52d3a9855747c17eaf4383823f135220716ab49bea5fbea7dd42cc9a92f8aa31
%bcond check 1
%global debug_package %{nil}
%global crate logos-derive
Name:           rust-logos-derive
Version:        0.16.1
Release:        1%{?dist}
Summary:        Create ridiculously fast Lexers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/logos-derive
Source0:        https://static.crates.io/crates/logos-derive/logos-derive-%{version}.crate
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
Summary:        Create ridiculously fast Lexers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Create ridiculously fast Lexers
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+forbid_unsafe-devel
Summary:        Create ridiculously fast Lexers
BuildArch:      noarch
%description -n %{name}+forbid_unsafe-devel

This package contains library source intended for building other packages which
use the "forbid_unsafe" feature of the "%{crate}" crate.

%package     -n %{name}+state_machine_codegen-devel
Summary:        Create ridiculously fast Lexers
BuildArch:      noarch
%description -n %{name}+state_machine_codegen-devel

This package contains library source intended for building other packages which
use the "state_machine_codegen" feature of the "%{crate}" crate.

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
%files -n rust-logos-derive-devel -f %{oreon_filedir}/rust-logos-derive-devel.list

%changelog

%autochangelog
