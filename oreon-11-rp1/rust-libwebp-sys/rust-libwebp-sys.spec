%global source0_hash 54cd30df7c7165ce74a456e4ca9732c603e8dc5e60784558c1c6dc047f876733
%bcond check 0
%global debug_package %{nil}
%global crate libwebp-sys
Name:           rust-libwebp-sys
Version:        0.9.6
Release:        1%{?dist}
Summary:        Bindings to libwebp (bindgen, static linking)
License:        MIT
URL:            https://crates.io/crates/libwebp-sys
Source0:        https://static.crates.io/crates/libwebp-sys/libwebp-sys-%{version}.crate
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
Summary:        Bindings to libwebp (bindgen, static linking)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+avx2-devel
Summary:        Bindings to libwebp (bindgen, static linking)
BuildArch:      noarch
%description -n %{name}+avx2-devel

This package contains library source intended for building other packages which
use the "avx2" feature of the "%{crate}" crate.

%package     -n %{name}+neon-devel
Summary:        Bindings to libwebp (bindgen, static linking)
BuildArch:      noarch
%description -n %{name}+neon-devel

This package contains library source intended for building other packages which
use the "neon" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Bindings to libwebp (bindgen, static linking)
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%package     -n %{name}+sse41-devel
Summary:        Bindings to libwebp (bindgen, static linking)
BuildArch:      noarch
%description -n %{name}+sse41-devel

This package contains library source intended for building other packages which
use the "sse41" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Bindings to libwebp (bindgen, static linking)
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-libwebp-sys-devel -f %{oreon_filedir}/rust-libwebp-sys-devel.list

%changelog

%autochangelog
