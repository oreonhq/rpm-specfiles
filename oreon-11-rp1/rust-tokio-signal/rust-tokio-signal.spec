%global source0_hash e8f46863230f9a05cf52d173721ec391b9c5782a2465f593029922b8782b9ffe
%bcond check 0
%global debug_package %{nil}
%global crate tokio-signal
Name:           rust-tokio-signal
Version:        0.1.5
Release:        1%{?dist}
Summary:        An implementation of an asynchronous Unix signal handling backed futu...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tokio-signal
Source0:        https://static.crates.io/crates/tokio-signal/tokio-signal-%{version}.crate
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
Summary:        An implementation of an asynchronous Unix signal handling backed futu...
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
%files -n rust-tokio-signal-devel -f %{oreon_filedir}/rust-tokio-signal-devel.list

%changelog

%autochangelog
