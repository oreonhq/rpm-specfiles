%global source0_hash 211d617eaa4b735c96c9e0228fcbdb5120ef623f2b8cb67ffb84c3e02dbc28a4
%bcond check 0
%global debug_package %{nil}
%global crate clap_mangen
Name:           rust-clap_mangen
Version:        0.3.3
Release:        1%{?dist}
Summary:        A manpage generator for clap
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/clap_mangen
Source0:        https://static.crates.io/crates/clap_mangen/clap_mangen-%{version}.crate
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
Summary:        A manpage generator for clap
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        A manpage generator for clap
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

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
%files -n rust-clap_mangen-devel -f %{oreon_filedir}/rust-clap_mangen-devel.list

%changelog

%autochangelog
