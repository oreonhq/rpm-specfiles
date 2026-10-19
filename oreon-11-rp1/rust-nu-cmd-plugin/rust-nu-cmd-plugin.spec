%global source0_hash 8845ca79dd71a3a6ca5c903e46fa857597793ea96839561cb4cd41f104ff7ea7
%bcond check 0
%global debug_package %{nil}
%global crate nu-cmd-plugin
Name:           rust-nu-cmd-plugin
Version:        0.99.1
Release:        1%{?dist}
Summary:        Commands for managing Nushell plugins
License:        MIT
URL:            https://crates.io/crates/nu-cmd-plugin
Source0:        https://static.crates.io/crates/nu-cmd-plugin/nu-cmd-plugin-%{version}.crate
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
Summary:        Commands for managing Nushell plugins
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
%files -n rust-nu-cmd-plugin-devel -f %{oreon_filedir}/rust-nu-cmd-plugin-devel.list

%changelog

%autochangelog
