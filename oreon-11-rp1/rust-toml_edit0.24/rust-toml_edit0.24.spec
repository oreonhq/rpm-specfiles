%global source0_hash 01f2eadbbc6b377a847be05f60791ef1058d9f696ecb51d2c07fe911d8569d8e
%bcond check 0
%global debug_package %{nil}
%global crate toml_edit
%global crate_version 0.24.1+spec-1.1.0
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-toml_edit0.24
Version:        0.24.1
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

%package     -n %{name}+anstream-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+anstream-devel

This package contains library source intended for building other packages which
use the "anstream" feature of the "%{crate}" crate.

%package     -n %{name}+anstyle-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+anstyle-devel

This package contains library source intended for building other packages which
use the "anstyle" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+display-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+display-devel

This package contains library source intended for building other packages which
use the "display" feature of the "%{crate}" crate.

%package     -n %{name}+parse-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+parse-devel

This package contains library source intended for building other packages which
use the "parse" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_core-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+serde_core-devel

This package contains library source intended for building other packages which
use the "serde_core" feature of the "%{crate}" crate.

%package     -n %{name}+serde_spanned-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+serde_spanned-devel

This package contains library source intended for building other packages which
use the "serde_spanned" feature of the "%{crate}" crate.

%package     -n %{name}+toml_parser-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+toml_parser-devel

This package contains library source intended for building other packages which
use the "toml_parser" feature of the "%{crate}" crate.

%package     -n %{name}+toml_writer-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+toml_writer-devel

This package contains library source intended for building other packages which
use the "toml_writer" feature of the "%{crate}" crate.

%package     -n %{name}+unbounded-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+unbounded-devel

This package contains library source intended for building other packages which
use the "unbounded" feature of the "%{crate}" crate.

%package     -n %{name}+winnow-devel
Summary:        Yet another format-preserving TOML parser.
BuildArch:      noarch
%description -n %{name}+winnow-devel

This package contains library source intended for building other packages which
use the "winnow" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-toml_edit0.24-devel -f %{oreon_filedir}/rust-toml_edit0.24-devel.list

%changelog

%autochangelog
