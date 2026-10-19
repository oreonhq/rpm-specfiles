%global source0_hash 07ba0ad7e047712414213ff67533e6dd477af0a4e1d14fb52343e53d30ea9397
%bcond check 0
%global debug_package %{nil}
%global crate path-dedot
Name:           rust-path-dedot
Version:        3.1.1
Release:        1%{?dist}
Summary:        Parse path with dots in Path and PathBuf
License:        MIT
URL:            https://crates.io/crates/path-dedot
Source0:        https://static.crates.io/crates/path-dedot/path-dedot-%{version}.crate
Patch:          path-dedot-fix-metadata.diff
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
Summary:        Parse path with dots in Path and PathBuf
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+lazy_static-devel
Summary:        Parse path with dots in Path and PathBuf
BuildArch:      noarch
%description -n %{name}+lazy_static-devel

This package contains library source intended for building other packages which
use the "lazy_static" feature of the "%{crate}" crate.

%package     -n %{name}+lazy_static_cache-devel
Summary:        Parse path with dots in Path and PathBuf
BuildArch:      noarch
%description -n %{name}+lazy_static_cache-devel

This package contains library source intended for building other packages which
use the "lazy_static_cache" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell_cache-devel
Summary:        Parse path with dots in Path and PathBuf
BuildArch:      noarch
%description -n %{name}+once_cell_cache-devel

This package contains library source intended for building other packages which
use the "once_cell_cache" feature of the "%{crate}" crate.

%package     -n %{name}+unsafe_cache-devel
Summary:        Parse path with dots in Path and PathBuf
BuildArch:      noarch
%description -n %{name}+unsafe_cache-devel

This package contains library source intended for building other packages which
use the "unsafe_cache" feature of the "%{crate}" crate.

%package     -n %{name}+use_unix_paths_on_wasm-devel
Summary:        Parse path with dots in Path and PathBuf
BuildArch:      noarch
%description -n %{name}+use_unix_paths_on_wasm-devel

This package contains library source intended for building other packages which
use the "use_unix_paths_on_wasm" feature of the "%{crate}" crate.

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
%files -n rust-path-dedot-devel -f %{oreon_filedir}/rust-path-dedot-devel.list

%changelog

%autochangelog
