%global source0_hash 5c0e531d93d39c34eef561e929e8a7f86d77a5af08aac4f6d6e39976c51858e9
%bcond check 0
%global debug_package %{nil}
%global crate built
Name:           rust-built
Version:        0.8.1
Release:        1%{?dist}
Summary:        Provides a crate with information from the time it was built.
License:        MIT
URL:            https://crates.io/crates/built
Source0:        https://static.crates.io/crates/built/built-%{version}.crate
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

%package     -n %{name}+cargo-lock-devel
Summary:        Provides a crate with information from the time it was built.
BuildArch:      noarch
%description -n %{name}+cargo-lock-devel

This package contains library source intended for building other packages which
use the "cargo-lock" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Provides a crate with information from the time it was built.
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+dependency-tree-devel
Summary:        Provides a crate with information from the time it was built.
BuildArch:      noarch
%description -n %{name}+dependency-tree-devel

This package contains library source intended for building other packages which
use the "dependency-tree" feature of the "%{crate}" crate.

%package     -n %{name}+git2-devel
Summary:        Provides a crate with information from the time it was built.
BuildArch:      noarch
%description -n %{name}+git2-devel

This package contains library source intended for building other packages which
use the "git2" feature of the "%{crate}" crate.

%package     -n %{name}+gix-devel
Summary:        Provides a crate with information from the time it was built.
BuildArch:      noarch
%description -n %{name}+gix-devel

This package contains library source intended for building other packages which
use the "gix" feature of the "%{crate}" crate.

%package     -n %{name}+semver-devel
Summary:        Provides a crate with information from the time it was built.
BuildArch:      noarch
%description -n %{name}+semver-devel

This package contains library source intended for building other packages which
use the "semver" feature of the "%{crate}" crate.

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
%files -n rust-built-devel -f %{oreon_filedir}/rust-built-devel.list

%changelog

%autochangelog
