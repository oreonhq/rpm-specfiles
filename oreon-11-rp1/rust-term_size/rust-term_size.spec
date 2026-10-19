%global source0_hash 1e4129646ca0ed8f45d09b929036bafad5377103edd06e50bf574b353d2b08d9
%bcond check 0
%global debug_package %{nil}
%global crate term_size
Name:           rust-term_size
Version:        0.3.2
Release:        1%{?dist}
Summary:        functions for determining terminal sizes and dimensions
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/term_size
Source0:        https://static.crates.io/crates/term_size/term_size-%{version}.crate
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
Summary:        functions for determining terminal sizes and dimensions
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        functions for determining terminal sizes and dimensions
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        functions for determining terminal sizes and dimensions
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+travis-devel
Summary:        functions for determining terminal sizes and dimensions
BuildArch:      noarch
%description -n %{name}+travis-devel

This package contains library source intended for building other packages which
use the "travis" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        functions for determining terminal sizes and dimensions
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-term_size-devel -f %{oreon_filedir}/rust-term_size-devel.list

%changelog

%autochangelog
