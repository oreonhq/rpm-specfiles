%global source0_hash b1de0e32a83f131e002238d7ccde18211c0a5397f60cbfffcb112868c2e0e20e
%bcond check 0
%global debug_package %{nil}
%global crate tokio-current-thread
Name:           rust-tokio-current-thread
Version:        0.1.7
Release:        1%{?dist}
Summary:        Single threaded executor which manage many tasks concurrently on the...
License:        MIT
URL:            https://crates.io/crates/tokio-current-thread
Source0:        https://static.crates.io/crates/tokio-current-thread/tokio-current-thread-%{version}.crate
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
Summary:        Single threaded executor which manage many tasks concurrently on the...
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
%files -n rust-tokio-current-thread-devel -f %{oreon_filedir}/rust-tokio-current-thread-devel.list

%changelog

%autochangelog
