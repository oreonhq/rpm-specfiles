%global source0_hash ce52f92afd3620741f37196d9bb141af4f39c41d052c17d31c6cc986f0a4e4a1
%bcond check 0
%global debug_package %{nil}
%global crate subplot
Name:           rust-subplot
Version:        0.14.0
Release:        1%{?dist}
Summary:        tools for specifying, documenting,
License:        MIT-0
URL:            https://crates.io/crates/subplot
Source0:        https://static.crates.io/crates/subplot/subplot-%{version}.crate
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

%package     -n %{name}+clap-devel
Summary:        tools for specifying, documenting,
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-cli-devel
Summary:        tools for specifying, documenting,
BuildArch:      noarch
%description -n %{name}+unstable-cli-devel

This package contains library source intended for building other packages which
use the "unstable-cli" feature of the "%{crate}" crate.

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
%files -n rust-subplot-devel -f %{oreon_filedir}/rust-subplot-devel.list

%changelog

%autochangelog
