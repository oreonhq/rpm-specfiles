%global source0_hash 9a8444b8ed4662e1a0c97f3eceda29630001a1bbb2632201e50312623e594213
%bcond check 0
%global debug_package %{nil}
%global crate gix-worktree-stream
Name:           rust-gix-worktree-stream0.32
Version:        0.32.0
Release:        1%{?dist}
Summary:        generate a byte-stream from a git-tree
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-worktree-stream
Source0:        https://static.crates.io/crates/gix-worktree-stream/gix-worktree-stream-%{version}.crate
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

%package     -n %{name}+sha1-devel
Summary:        generate a byte-stream from a git-tree
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

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
%files -n rust-gix-worktree-stream0.32-devel -f %{oreon_filedir}/rust-gix-worktree-stream0.32-devel.list

%changelog

%autochangelog
