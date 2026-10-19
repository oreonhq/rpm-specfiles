%global source0_hash 9f517ff4f36da6a1bae02e05a59865736a5e594329ff1f958eac5865989ba2e3
%bcond check 1
%global debug_package %{nil}
%global crate rutabaga_gfx
Name:           rust-rutabaga_gfx
Version:        0.1.75
Release:        1%{?dist}
Summary:        Cross-platform, open-source, Rust-based graphics paravirtualization
License:        BSD-3-Clause
URL:            https://crates.io/crates/rutabaga_gfx
Source0:        https://static.crates.io/crates/rutabaga_gfx/rutabaga_gfx-%{version}.crate
ExcludeArch: ppc64le s390x
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
Summary:        Cross-platform, open-source, Rust-based graphics paravirtualization
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gbm-devel
Summary:        Cross-platform, open-source, Rust-based graphics paravirtualization
BuildArch:      noarch
%description -n %{name}+gbm-devel

This package contains library source intended for building other packages which
use the "gbm" feature of the "%{crate}" crate.

%package     -n %{name}+gfxstream-devel
Summary:        Cross-platform, open-source, Rust-based graphics paravirtualization
BuildArch:      noarch
%description -n %{name}+gfxstream-devel

This package contains library source intended for building other packages which
use the "gfxstream" feature of the "%{crate}" crate.

%package     -n %{name}+virgl_renderer-devel
Summary:        Cross-platform, open-source, Rust-based graphics paravirtualization
BuildArch:      noarch
%description -n %{name}+virgl_renderer-devel

This package contains library source intended for building other packages which
use the "virgl_renderer" feature of the "%{crate}" crate.

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
%files -n rust-rutabaga_gfx-devel -f %{oreon_filedir}/rust-rutabaga_gfx-devel.list

%changelog

%autochangelog
