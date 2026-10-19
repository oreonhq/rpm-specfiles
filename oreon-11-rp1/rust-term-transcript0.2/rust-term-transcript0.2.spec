%global source0_hash 6d77280c9041d978e4ffedbdd19f710a1360085510c5e99dbcfec8e2f2bd4285
%global debug_package %{nil}
%bcond check 1
%global crate term-transcript
Name:           rust-term-transcript0.2
Version:        0.2.0
Release:        1%{?dist}
Summary:        Snapshotting and snapshot testing for CLI / REPL applications
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/term-transcript
Source0:        https://static.crates.io/crates/term-transcript/term-transcript-%{version}.crate
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
Summary:        Snapshotting and snapshot testing for CLI / REPL applications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+svg-devel
Summary:        Snapshotting and snapshot testing for CLI / REPL applications
BuildArch:      noarch
%description -n %{name}+svg-devel

This package contains library source intended for building other packages which
use the "svg" feature of the "%{crate}" crate.

%package     -n %{name}+test-devel
Summary:        Snapshotting and snapshot testing for CLI / REPL applications
BuildArch:      noarch
%description -n %{name}+test-devel

This package contains library source intended for building other packages which
use the "test" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-term-transcript0.2-devel -f %{oreon_filedir}/rust-term-transcript0.2-devel.list

%changelog

%autochangelog
