%global source0_hash 1dd39b4b2077bd36e60ca28c31d494046e747759cb9b507a7d177bb64787c39e
%bcond check 1
%global debug_package %{nil}
%global crate shadow-rs
Name:           rust-shadow-rs
Version:        2.0.0
Release:        1%{?dist}
Summary:        Build-time information stored in your rust project
License:        MIT AND Apache-2.0
URL:            https://crates.io/crates/shadow-rs
Source0:        https://static.crates.io/crates/shadow-rs/shadow-rs-%{version}.crate
Patch:          shadow-rs-fix-metadata.diff
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
Summary:        Build-time information stored in your rust project
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+git2-devel
Summary:        Build-time information stored in your rust project
BuildArch:      noarch
%description -n %{name}+git2-devel

This package contains library source intended for building other packages which
use the "git2" feature of the "%{crate}" crate.

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

%{cargo_test -- -- %{shrink:
    --skip git::tests::test_git
    --skip git::tests::test_current_branch
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-shadow-rs-devel -f %{oreon_filedir}/rust-shadow-rs-devel.list

%changelog

%autochangelog
