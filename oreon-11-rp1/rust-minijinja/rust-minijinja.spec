%global source0_hash 5c54f3bcc034dd74496b5ca929fd0b710186672d5ff0b0f255a9ceb259042ece
%bcond check 1
%global debug_package %{nil}
%global crate minijinja
Name:           rust-minijinja
Version:        2.16.0
Release:        1%{?dist}
Summary:        Powerful template engine for Rust with minimal dependencies
License:        Apache-2.0
URL:            https://crates.io/crates/minijinja
Source0:        https://static.crates.io/crates/minijinja/minijinja-%{version}.crate
Patch:          minijinja-fix-metadata.diff
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
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+adjacent_loop_items-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+adjacent_loop_items-devel

This package contains library source intended for building other packages which
use the "adjacent_loop_items" feature of the "%{crate}" crate.

%package     -n %{name}+builtins-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+builtins-devel

This package contains library source intended for building other packages which
use the "builtins" feature of the "%{crate}" crate.

%package     -n %{name}+custom_syntax-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+custom_syntax-devel

This package contains library source intended for building other packages which
use the "custom_syntax" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+deserialization-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+deserialization-devel

This package contains library source intended for building other packages which
use the "deserialization" feature of the "%{crate}" crate.

%package     -n %{name}+fuel-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+fuel-devel

This package contains library source intended for building other packages which
use the "fuel" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+internal_debug-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+internal_debug-devel

This package contains library source intended for building other packages which
use the "internal_debug" feature of the "%{crate}" crate.

%package     -n %{name}+internal_safe_search-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+internal_safe_search-devel

This package contains library source intended for building other packages which
use the "internal_safe_search" feature of the "%{crate}" crate.

%package     -n %{name}+json-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+json-devel

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%package     -n %{name}+key_interning-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+key_interning-devel

This package contains library source intended for building other packages which
use the "key_interning" feature of the "%{crate}" crate.

%package     -n %{name}+loop_controls-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+loop_controls-devel

This package contains library source intended for building other packages which
use the "loop_controls" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+multi_template-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+multi_template-devel

This package contains library source intended for building other packages which
use the "multi_template" feature of the "%{crate}" crate.

%package     -n %{name}+percent-encoding-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+percent-encoding-devel

This package contains library source intended for building other packages which
use the "percent-encoding" feature of the "%{crate}" crate.

%package     -n %{name}+preserve_order-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+preserve_order-devel

This package contains library source intended for building other packages which
use the "preserve_order" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+speedups-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+speedups-devel

This package contains library source intended for building other packages which
use the "speedups" feature of the "%{crate}" crate.

%package     -n %{name}+stacker-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+stacker-devel

This package contains library source intended for building other packages which
use the "stacker" feature of the "%{crate}" crate.

%package     -n %{name}+std_collections-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+std_collections-devel

This package contains library source intended for building other packages which
use the "std_collections" feature of the "%{crate}" crate.

%package     -n %{name}+unicase-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+unicase-devel

This package contains library source intended for building other packages which
use the "unicase" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+unicode-devel

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-ident-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+unicode-ident-devel

This package contains library source intended for building other packages which
use the "unicode-ident" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_machinery-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+unstable_machinery-devel

This package contains library source intended for building other packages which
use the "unstable_machinery" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_machinery_serde-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+unstable_machinery_serde-devel

This package contains library source intended for building other packages which
use the "unstable_machinery_serde" feature of the "%{crate}" crate.

%package     -n %{name}+urlencode-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+urlencode-devel

This package contains library source intended for building other packages which
use the "urlencode" feature of the "%{crate}" crate.

%package     -n %{name}+v_htmlescape-devel
Summary:        Powerful template engine for Rust with minimal dependencies
BuildArch:      noarch
%description -n %{name}+v_htmlescape-devel

This package contains library source intended for building other packages which
use the "v_htmlescape" feature of the "%{crate}" crate.

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
%files -n rust-minijinja-devel -f %{oreon_filedir}/rust-minijinja-devel.list

%changelog

%autochangelog
