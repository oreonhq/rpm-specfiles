%global source0_hash 2a1867f8f005bd7fb73c367e2e45dd628417906a2ca27597fe59cbf04279a222
%bcond check 1
%global debug_package %{nil}
%global crate sealed_test
Name:           rust-sealed_test
Version:        1.1.0
Release:        1%{?dist}
Summary:        Procmacro attribute to run your test in an isolated environment
License:        MIT
URL:            https://crates.io/crates/sealed_test
Source0:        https://static.crates.io/crates/sealed_test/sealed_test-%{version}.crate
Patch:          sealed_test-fix-metadata.diff
Patch10:        0001-Fix-test-code-with-cmd_lib-1.9.6-PathBuf-does-not-im.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  git-core
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
Summary:        Procmacro attribute to run your test in an isolated environment
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

git config --global user.name fedora
git config --global user.email fedora@example.com
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-sealed_test-devel -f %{oreon_filedir}/rust-sealed_test-devel.list

%changelog

%autochangelog
