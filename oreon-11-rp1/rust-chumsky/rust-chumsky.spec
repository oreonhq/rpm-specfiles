%global source0_hash e0d2bfadce76f963d776feff99db6dc33783829539258314776383b33e2a00f8
%bcond check 0
%global debug_package %{nil}
%global crate chumsky
Name:           rust-chumsky
Version:        0.13.0
Release:        1%{?dist}
Summary:        Parser library for humans with powerful error recovery
License:        MIT
URL:            https://crates.io/crates/chumsky
Source0:        https://static.crates.io/crates/chumsky/chumsky-%{version}.crate
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
Summary:        Parser library for humans with powerful error recovery
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Parser library for humans with powerful error recovery
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+stacker-devel
Summary:        Parser library for humans with powerful error recovery
BuildArch:      noarch
%description -n %{name}+stacker-devel

This package contains library source intended for building other packages which
use the "stacker" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Parser library for humans with powerful error recovery
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-chumsky-devel -f %{oreon_filedir}/rust-chumsky-devel.list

%changelog

%autochangelog
