%global source0_hash da8e198c052315686d36371e8a3c5778b7852fc75cc313e4e11eeb7a644a1b62
%bcond check 0
%global debug_package %{nil}
%global crate clap_complete_command
Name:           rust-clap_complete_command
Version:        0.6.1
Release:        1%{?dist}
Summary:        Reduces boilerplate for adding a shell completion command to Clap
License:        MIT
URL:            https://crates.io/crates/clap_complete_command
Source0:        https://static.crates.io/crates/clap_complete_command/clap_complete_command-%{version}.crate
Patch:          clap_complete_command-fix-metadata.diff
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
Summary:        Reduces boilerplate for adding a shell completion command to Clap
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+fig-devel
Summary:        Reduces boilerplate for adding a shell completion command to Clap
BuildArch:      noarch
%description -n %{name}+fig-devel

This package contains library source intended for building other packages which
use the "fig" feature of the "%{crate}" crate.

%package     -n %{name}+nushell-devel
Summary:        Reduces boilerplate for adding a shell completion command to Clap
BuildArch:      noarch
%description -n %{name}+nushell-devel

This package contains library source intended for building other packages which
use the "nushell" feature of the "%{crate}" crate.

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
%files -n rust-clap_complete_command-devel -f %{oreon_filedir}/rust-clap_complete_command-devel.list

%changelog

%autochangelog
