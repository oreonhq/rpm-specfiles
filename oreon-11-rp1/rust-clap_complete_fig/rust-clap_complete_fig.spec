%global source0_hash d494102c8ff3951810c72baf96910b980fb065ca5d3101243e6a8dc19747c86b
%bcond check 1
%global debug_package %{nil}
%global crate clap_complete_fig
Name:           rust-clap_complete_fig
Version:        4.5.2
Release:        1%{?dist}
Summary:        Generator library used with clap for Fig completion scripts
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/clap_complete_fig
Source0:        https://static.crates.io/crates/clap_complete_fig/clap_complete_fig-%{version}.crate
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
Summary:        Generator library used with clap for Fig completion scripts
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-clap_complete_fig-devel -f %{oreon_filedir}/rust-clap_complete_fig-devel.list

%changelog

%autochangelog
