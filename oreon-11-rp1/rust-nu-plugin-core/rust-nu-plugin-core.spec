%global source0_hash 3b6de4cbecdc9568acb9e81a6e769813f3decb97802e26fc5c66dc360f18e332
%bcond check 0
%global debug_package %{nil}
%global crate nu-plugin-core
Name:           rust-nu-plugin-core
Version:        0.99.1
Release:        1%{?dist}
Summary:        Shared internal functionality to support Nushell plugins
License:        MIT
URL:            https://crates.io/crates/nu-plugin-core
Source0:        https://static.crates.io/crates/nu-plugin-core/nu-plugin-core-%{version}.crate
Patch:          nu-plugin-core-fix-metadata-auto.diff
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
Summary:        Shared internal functionality to support Nushell plugins
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+interprocess-devel
Summary:        Shared internal functionality to support Nushell plugins
BuildArch:      noarch
%description -n %{name}+interprocess-devel

This package contains library source intended for building other packages which
use the "interprocess" feature of the "%{crate}" crate.

%package     -n %{name}+local-socket-devel
Summary:        Shared internal functionality to support Nushell plugins
BuildArch:      noarch
%description -n %{name}+local-socket-devel

This package contains library source intended for building other packages which
use the "local-socket" feature of the "%{crate}" crate.

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

%ifnarch %{ix86}
%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-nu-plugin-core-devel -f %{oreon_filedir}/rust-nu-plugin-core-devel.list

%changelog

%autochangelog
