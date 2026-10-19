%global source0_hash e6718ae9798d44598b65d91d835c55defb2ef0f9b8a96c59fbe1f983dd749975
%bcond check 1
%global debug_package %{nil}
%global crate ironrdp-rdpdr
Name:           rust-ironrdp-rdpdr
Version:        0.3.0
Release:        1%{?dist}
Summary:        RDPDR channel implementation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp-rdpdr
Source0:        https://static.crates.io/crates/ironrdp-rdpdr/ironrdp-rdpdr-%{version}.crate
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
Summary:        RDPDR channel implementation
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
%files -n rust-ironrdp-rdpdr-devel -f %{oreon_filedir}/rust-ironrdp-rdpdr-devel.list

%changelog

%autochangelog
