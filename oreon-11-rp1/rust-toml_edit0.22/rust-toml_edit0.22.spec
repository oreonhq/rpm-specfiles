%global source0_hash 41fe8c660ae4257887cf66394862d21dbca4a6ddd26f04a3560410406a2f819a
%bcond check 0
%global debug_package %{nil}
%global crate toml_edit
Name:           rust-toml_edit0.22
Version:        0.22.27
Release:        1%{?dist}
Summary:        Yet another format-preserving TOML parser.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/toml_edit
Source0:        https://static.crates.io/crates/toml_edit/toml_edit-%{version}.crate
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
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+display-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+display-devel

This package contains library source intended for building other packages which
use the "display" feature of the "%{crate}" crate.

%package     -n %{name}+kstring-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+kstring-devel

This package contains library source intended for building other packages which
use the "kstring" feature of the "%{crate}" crate.

%package     -n %{name}+parse-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+parse-devel

This package contains library source intended for building other packages which
use the "parse" feature of the "%{crate}" crate.

%package     -n %{name}+perf-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+perf-devel

This package contains library source intended for building other packages which
use the "perf" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_spanned-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+serde_spanned-devel

This package contains library source intended for building other packages which
use the "serde_spanned" feature of the "%{crate}" crate.

%package     -n %{name}+toml_write-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+toml_write-devel

This package contains library source intended for building other packages which
use the "toml_write" feature of the "%{crate}" crate.

%package     -n %{name}+unbounded-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+unbounded-devel

This package contains library source intended for building other packages which
use the "unbounded" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-debug-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+unstable-debug-devel

This package contains library source intended for building other packages which
use the "unstable-debug" feature of the "%{crate}" crate.

%package     -n %{name}+winnow-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+winnow-devel

This package contains library source intended for building other packages which
use the "winnow" feature of the "%{crate}" crate.

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
%files -n rust-toml_edit0.22-devel -f %{oreon_filedir}/rust-toml_edit0.22-devel.list

%changelog

%autochangelog
