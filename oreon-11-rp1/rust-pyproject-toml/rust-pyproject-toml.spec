%global source0_hash f6d755483ad14b49e76713b52285235461a5b4f73f17612353e11a5de36a5fd2
%bcond check 1
%global debug_package %{nil}
%global crate pyproject-toml
Name:           rust-pyproject-toml
Version:        0.13.7
Release:        1%{?dist}
Summary:        Pyproject.toml parser in Rust
License:        MIT
URL:            https://crates.io/crates/pyproject-toml
Source0:        https://static.crates.io/crates/pyproject-toml/pyproject-toml-%{version}.crate
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
Summary:        Pyproject.toml parser in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+glob-devel
Summary:        Pyproject.toml parser in Rust
BuildArch:      noarch
%description -n %{name}+glob-devel

This package contains library source intended for building other packages which
use the "glob" feature of the "%{crate}" crate.

%package     -n %{name}+pep639-glob-devel
Summary:        Pyproject.toml parser in Rust
BuildArch:      noarch
%description -n %{name}+pep639-glob-devel

This package contains library source intended for building other packages which
use the "pep639-glob" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Pyproject.toml parser in Rust
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

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
%files -n rust-pyproject-toml-devel -f %{oreon_filedir}/rust-pyproject-toml-devel.list

%changelog

%autochangelog
