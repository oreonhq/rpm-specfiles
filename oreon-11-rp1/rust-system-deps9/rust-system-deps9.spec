%global source0_hash 8a0dae2cbca1f0ff93795713cfe0a4c02f760e3c0b8ae2ab4ec4045808ff429f
%bcond check 0
%global debug_package %{nil}
%global crate system-deps
Name:           rust-system-deps9
Version:        9.0.0
Release:        1%{?dist}
Summary:        Discover and configure system dependencies from declarative dependencies in Cargo.toml
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/system-deps
Source0:        https://static.crates.io/crates/system-deps/system-deps-%{version}.crate
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
Summary:        Discover and configure system dependencies from declarative dependencies in Cargo.toml
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+binary-devel
Summary:        Discover and configure system dependencies from declarative dependencies in Cargo.toml
BuildArch:      noarch
%description -n %{name}+binary-devel

This package contains library source intended for building other packages which
use the "binary" feature of the "%{crate}" crate.

%package     -n %{name}+gz-devel
Summary:        Discover and configure system dependencies from declarative dependencies in Cargo.toml
BuildArch:      noarch
%description -n %{name}+gz-devel

This package contains library source intended for building other packages which
use the "gz" feature of the "%{crate}" crate.

%package     -n %{name}+inno-devel
Summary:        Discover and configure system dependencies from declarative dependencies in Cargo.toml
BuildArch:      noarch
%description -n %{name}+inno-devel

This package contains library source intended for building other packages which
use the "inno" feature of the "%{crate}" crate.

%package     -n %{name}+pkg-devel
Summary:        Discover and configure system dependencies from declarative dependencies in Cargo.toml
BuildArch:      noarch
%description -n %{name}+pkg-devel

This package contains library source intended for building other packages which
use the "pkg" feature of the "%{crate}" crate.

%package     -n %{name}+system-deps-meta-devel
Summary:        Discover and configure system dependencies from declarative dependencies in Cargo.toml
BuildArch:      noarch
%description -n %{name}+system-deps-meta-devel

This package contains library source intended for building other packages which
use the "system-deps-meta" feature of the "%{crate}" crate.

%package     -n %{name}+xz-devel
Summary:        Discover and configure system dependencies from declarative dependencies in Cargo.toml
BuildArch:      noarch
%description -n %{name}+xz-devel

This package contains library source intended for building other packages which
use the "xz" feature of the "%{crate}" crate.

%package     -n %{name}+zip-devel
Summary:        Discover and configure system dependencies from declarative dependencies in Cargo.toml
BuildArch:      noarch
%description -n %{name}+zip-devel

This package contains library source intended for building other packages which
use the "zip" feature of the "%{crate}" crate.

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
%files -n rust-system-deps9-devel -f %{oreon_filedir}/rust-system-deps9-devel.list

%changelog

%autochangelog
