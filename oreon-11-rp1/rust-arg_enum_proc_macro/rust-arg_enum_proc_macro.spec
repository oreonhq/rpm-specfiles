%global source0_hash 0ae92a5119aa49cdbcf6b9f893fe4e1d98b04ccbf82ee0584ad948a44a734dea
%bcond check 0
%global debug_package %{nil}
%global crate arg_enum_proc_macro
Name:           rust-arg_enum_proc_macro
Version:        0.3.4
Release:        1%{?dist}
Summary:        A procedural macro compatible with clap arg_enum
License:        MIT
URL:            https://crates.io/crates/arg_enum_proc_macro
Source0:        https://static.crates.io/crates/arg_enum_proc_macro/arg_enum_proc_macro-%{version}.crate
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
Summary:        A procedural macro compatible with clap arg_enum
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
%files -n rust-arg_enum_proc_macro-devel -f %{oreon_filedir}/rust-arg_enum_proc_macro-devel.list

%changelog

%autochangelog
