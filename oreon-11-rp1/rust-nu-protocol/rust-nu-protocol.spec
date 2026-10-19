%global source0_hash 9fdd6c9896962f3d36601668e590ccc078bfb34ea97ee3c0e3b1261d2f4dc229
%bcond check 1
%global debug_package %{nil}
%global crate nu-protocol
Name:           rust-nu-protocol
Version:        0.99.1
Release:        1%{?dist}
Summary:        Nushell's internal protocols, including its abstract syntax tree
License:        MIT
URL:            https://crates.io/crates/nu-protocol
Source0:        https://static.crates.io/crates/nu-protocol/nu-protocol-%{version}.crate
Patch:          nu-protocol-fix-metadata-auto.diff
Patch:          nu-protocol-fix-metadata.diff
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
Summary:        Nushell's internal protocols, including its abstract syntax tree
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+brotli-devel
Summary:        Nushell's internal protocols, including its abstract syntax tree
BuildArch:      noarch
%description -n %{name}+brotli-devel

This package contains library source intended for building other packages which
use the "brotli" feature of the "%{crate}" crate.

%package     -n %{name}+plugin-devel
Summary:        Nushell's internal protocols, including its abstract syntax tree
BuildArch:      noarch
%description -n %{name}+plugin-devel

This package contains library source intended for building other packages which
use the "plugin" feature of the "%{crate}" crate.

%package     -n %{name}+rmp-serde-devel
Summary:        Nushell's internal protocols, including its abstract syntax tree
BuildArch:      noarch
%description -n %{name}+rmp-serde-devel

This package contains library source intended for building other packages which
use the "rmp-serde" feature of the "%{crate}" crate.

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

%{cargo_test -- -- %{shrink:
    --skip config_
    --skip fancy_default_errors
    --skip filesize_format_auto_metric_
    --skip filesize_metric_
    --skip narratable_errors
    --skip plugins
    --skip test_signature_same_name
    --skip test_signature_same_short
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-nu-protocol-devel -f %{oreon_filedir}/rust-nu-protocol-devel.list

%changelog

%autochangelog
