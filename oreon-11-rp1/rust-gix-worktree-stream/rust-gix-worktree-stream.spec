%global source0_hash de5ec0ccbab39c9994656ea031ded8ffd90b370a3cc8e360fbe3c4ebe7c64964
%bcond check 0
%global debug_package %{nil}
%global crate gix-worktree-stream
Name:           rust-gix-worktree-stream
Version:        0.36.1
Release:        1%{?dist}
Summary:        Generate a byte-stream from a git-tree
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

%package     -n %{name}+default-devel
Summary:        Generate a byte-stream from a git-tree
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Generate a byte-stream from a git-tree
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha256-devel
Summary:        Generate a byte-stream from a git-tree
BuildArch:      noarch
%description -n %{name}+sha256-devel

This package contains library source intended for building other packages which
use the "sha256" feature of the "%{crate}" crate.

%prep
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
%files -n rust-gix-worktree-stream-devel -f %{oreon_filedir}/rust-gix-worktree-stream-devel.list

%changelog

%autochangelog
