%global source0_hash f75363874b771be265f4ffe307ca705ef6f3baa19011c149da8674a87f1b75c4
%bcond check 1
%global debug_package %{nil}
%global crate askama
Name:           rust-askama
Version:        0.14.0
Release:        1%{?dist}
Summary:        Type-safe, compiled Jinja-like templates for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/askama
Source0:        https://static.crates.io/crates/askama/askama-%{version}.crate
Patch:          askama-fix-metadata.diff
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
Summary:        Type-safe, compiled Jinja-like templates for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Type-safe, compiled Jinja-like templates for Rust
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+blocks-devel
Summary:        Type-safe, compiled Jinja-like templates for Rust
BuildArch:      noarch
%description -n %{name}+blocks-devel

This package contains library source intended for building other packages which
use the "blocks" feature of the "%{crate}" crate.

%package     -n %{name}+code-in-doc-devel
Summary:        Type-safe, compiled Jinja-like templates for Rust
BuildArch:      noarch
%description -n %{name}+code-in-doc-devel

This package contains library source intended for building other packages which
use the "code-in-doc" feature of the "%{crate}" crate.

%package     -n %{name}+config-devel
Summary:        Type-safe, compiled Jinja-like templates for Rust
BuildArch:      noarch
%description -n %{name}+config-devel

This package contains library source intended for building other packages which
use the "config" feature of the "%{crate}" crate.

%package     -n %{name}+derive-devel
Summary:        Type-safe, compiled Jinja-like templates for Rust
BuildArch:      noarch
%description -n %{name}+derive-devel

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%package     -n %{name}+full-devel
Summary:        Type-safe, compiled Jinja-like templates for Rust
BuildArch:      noarch
%description -n %{name}+full-devel

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Type-safe, compiled Jinja-like templates for Rust
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Type-safe, compiled Jinja-like templates for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+urlencode-devel
Summary:        Type-safe, compiled Jinja-like templates for Rust
BuildArch:      noarch
%description -n %{name}+urlencode-devel

This package contains library source intended for building other packages which
use the "urlencode" feature of the "%{crate}" crate.

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
%files -n rust-askama-devel -f %{oreon_filedir}/rust-askama-devel.list

%changelog

%autochangelog
