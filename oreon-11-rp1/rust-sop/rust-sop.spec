%global source0_hash 178bb001c144c5b83c9420f5ac1c4acc3b6e13b2f40914d150dddf54babf4714
%bcond check 1
%global debug_package %{nil}
%global crate sop
Name:           rust-sop
Version:        0.8.2
Release:        1%{?dist}
Summary:        Rust Interface for the Stateless OpenPGP Interface
License:        MIT
URL:            https://crates.io/crates/sop
Source0:        https://static.crates.io/crates/sop/sop-%{version}.crate
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
Summary:        Rust Interface for the Stateless OpenPGP Interface
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+anyhow-devel
Summary:        Rust Interface for the Stateless OpenPGP Interface
BuildArch:      noarch
%description -n %{name}+anyhow-devel

This package contains library source intended for building other packages which
use the "anyhow" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Rust Interface for the Stateless OpenPGP Interface
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        Rust Interface for the Stateless OpenPGP Interface
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+clap_complete-devel
Summary:        Rust Interface for the Stateless OpenPGP Interface
BuildArch:      noarch
%description -n %{name}+clap_complete-devel

This package contains library source intended for building other packages which
use the "clap_complete" feature of the "%{crate}" crate.

%package     -n %{name}+clap_mangen-devel
Summary:        Rust Interface for the Stateless OpenPGP Interface
BuildArch:      noarch
%description -n %{name}+clap_mangen-devel

This package contains library source intended for building other packages which
use the "clap_mangen" feature of the "%{crate}" crate.

%package     -n %{name}+cli-devel
Summary:        Rust Interface for the Stateless OpenPGP Interface
BuildArch:      noarch
%description -n %{name}+cli-devel

This package contains library source intended for building other packages which
use the "cli" feature of the "%{crate}" crate.

%package     -n %{name}+cliv-devel
Summary:        Rust Interface for the Stateless OpenPGP Interface
BuildArch:      noarch
%description -n %{name}+cliv-devel

This package contains library source intended for building other packages which
use the "cliv" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Rust Interface for the Stateless OpenPGP Interface
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

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
%files -n rust-sop-devel -f %{oreon_filedir}/rust-sop-devel.list

%changelog

%autochangelog
