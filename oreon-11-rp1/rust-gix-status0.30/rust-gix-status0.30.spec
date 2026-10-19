%global source0_hash 68c6d2a8c521ffa205fe7e268c82e6d1378ba37cd826ca10ab6129fdc29a4b65
%bcond check 0
%global debug_package %{nil}
%global crate gix-status
Name:           rust-gix-status0.30
Version:        0.30.0
Release:        1%{?dist}
Summary:        A crate of the gitoxide project dealing with 'git status'-like functi...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-status
Source0:        https://static.crates.io/crates/gix-status/gix-status-%{version}.crate
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

%package     -n %{name}+document-features-devel
Summary:        A crate of the gitoxide project dealing with 'git status'-like functi...
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+gix-diff-devel
Summary:        A crate of the gitoxide project dealing with 'git status'-like functi...
BuildArch:      noarch
%description -n %{name}+gix-diff-devel

This package contains library source intended for building other packages which
use the "gix-diff" feature of the "%{crate}" crate.

%package     -n %{name}+gix-dir-devel
Summary:        A crate of the gitoxide project dealing with 'git status'-like functi...
BuildArch:      noarch
%description -n %{name}+gix-dir-devel

This package contains library source intended for building other packages which
use the "gix-dir" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        A crate of the gitoxide project dealing with 'git status'-like functi...
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+worktree-rewrites-devel
Summary:        A crate of the gitoxide project dealing with 'git status'-like functi...
BuildArch:      noarch
%description -n %{name}+worktree-rewrites-devel

This package contains library source intended for building other packages which
use the "worktree-rewrites" feature of the "%{crate}" crate.

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
%files -n rust-gix-status0.30-devel -f %{oreon_filedir}/rust-gix-status0.30-devel.list

%changelog

%autochangelog
