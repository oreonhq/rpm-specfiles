%global source0_hash 11ec05c52be0a07b08061f7dd003e7d7092e0472bc731b4af7bb1ef876109802
%bcond check 0
%global debug_package %{nil}
%global crate proc-macro-error2
Name:           rust-proc-macro-error2
Version:        2.0.1
Release:        1%{?dist}
Summary:        Almost drop-in replacement to panics in proc-macros
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/proc-macro-error2
Source0:        https://static.crates.io/crates/proc-macro-error2/proc-macro-error2-%{version}.crate
Patch:          proc-macro-error2-fix-metadata.diff
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
Summary:        Almost drop-in replacement to panics in proc-macros
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Almost drop-in replacement to panics in proc-macros
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+syn-error-devel
Summary:        Almost drop-in replacement to panics in proc-macros
BuildArch:      noarch
%description -n %{name}+syn-error-devel

This package contains library source intended for building other packages which
use the "syn-error" feature of the "%{crate}" crate.

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
%files -n rust-proc-macro-error2-devel -f %{oreon_filedir}/rust-proc-macro-error2-devel.list

%changelog

%autochangelog
