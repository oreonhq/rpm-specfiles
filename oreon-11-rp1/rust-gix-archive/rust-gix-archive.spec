%global source0_hash 1c4ef97efd3920d3525104c5f253dec94dc935f953a50055954939177aed2cdd
%bcond check 0
%global debug_package %{nil}
%global crate gix-archive
Name:           rust-gix-archive
Version:        0.36.1
Release:        1%{?dist}
Summary:        archive generation from of a worktree stream
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-archive
Source0:        https://static.crates.io/crates/gix-archive/gix-archive-%{version}.crate
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
Summary:        archive generation from of a worktree stream
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        archive generation from of a worktree stream
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+flate2-devel
Summary:        archive generation from of a worktree stream
BuildArch:      noarch
%description -n %{name}+flate2-devel

This package contains library source intended for building other packages which
use the "flate2" feature of the "%{crate}" crate.

%package     -n %{name}+gix-path-devel
Summary:        archive generation from of a worktree stream
BuildArch:      noarch
%description -n %{name}+gix-path-devel

This package contains library source intended for building other packages which
use the "gix-path" feature of the "%{crate}" crate.

%package     -n %{name}+rawzip-devel
Summary:        archive generation from of a worktree stream
BuildArch:      noarch
%description -n %{name}+rawzip-devel

This package contains library source intended for building other packages which
use the "rawzip" feature of the "%{crate}" crate.

%package     -n %{name}+tar-devel
Summary:        archive generation from of a worktree stream
BuildArch:      noarch
%description -n %{name}+tar-devel

This package contains library source intended for building other packages which
use the "tar" feature of the "%{crate}" crate.

%package     -n %{name}+tar_gz-devel
Summary:        archive generation from of a worktree stream
BuildArch:      noarch
%description -n %{name}+tar_gz-devel

This package contains library source intended for building other packages which
use the "tar_gz" feature of the "%{crate}" crate.

%package     -n %{name}+zip-devel
Summary:        archive generation from of a worktree stream
BuildArch:      noarch
%description -n %{name}+zip-devel

This package contains library source intended for building other packages which
use the "zip" feature of the "%{crate}" crate.

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
%files -n rust-gix-archive-devel -f %{oreon_filedir}/rust-gix-archive-devel.list

%changelog

%autochangelog
