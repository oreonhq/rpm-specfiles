%global source0_hash 037e2a1a92236d0aff7e845093f64661d6df4c02c9fcc61a60e9e1d736fa392f
%bcond check 0
%global debug_package %{nil}
%global crate clap_complete
Name:           rust-clap_complete
Version:        4.6.11
Release:        1%{?dist}
Summary:        Generate shell completion scripts for your clap::Command
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/clap_complete
Source0:        https://static.crates.io/crates/clap_complete/clap_complete-%{version}.crate
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
Summary:        Generate shell completion scripts for your clap::Command
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Generate shell completion scripts for your clap::Command
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-doc-devel
Summary:        Generate shell completion scripts for your clap::Command
BuildArch:      noarch
%description -n %{name}+unstable-doc-devel

This package contains library source intended for building other packages which
use the "unstable-doc" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-dynamic-devel
Summary:        Generate shell completion scripts for your clap::Command
BuildArch:      noarch
%description -n %{name}+unstable-dynamic-devel

This package contains library source intended for building other packages which
use the "unstable-dynamic" feature of the "%{crate}" crate.

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
%files -n rust-clap_complete-devel -f %{oreon_filedir}/rust-clap_complete-devel.list

%changelog

%autochangelog
