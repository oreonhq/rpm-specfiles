%global source0_hash 3ed36b627476e2072c129900a17c977a38052b5497e27308159bc881fbf4eecf
%bcond check 0
%global debug_package %{nil}
%global crate gix-worktree
Name:           rust-gix-worktree
Version:        0.56.0
Release:        1%{?dist}
Summary:        Of the gitoxide project for shared worktree related types and utilities
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-worktree
Source0:        https://static.crates.io/crates/gix-worktree/gix-worktree-%{version}.crate
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
Summary:        Of the gitoxide project for shared worktree related types and utilities
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+attributes-devel
Summary:        Of the gitoxide project for shared worktree related types and utilities
BuildArch:      noarch
%description -n %{name}+attributes-devel

This package contains library source intended for building other packages which
use the "attributes" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Of the gitoxide project for shared worktree related types and utilities
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+gix-features-devel
Summary:        Of the gitoxide project for shared worktree related types and utilities
BuildArch:      noarch
%description -n %{name}+gix-features-devel

This package contains library source intended for building other packages which
use the "gix-features" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Of the gitoxide project for shared worktree related types and utilities
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Of the gitoxide project for shared worktree related types and utilities
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Of the gitoxide project for shared worktree related types and utilities
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+sha256-devel
Summary:        Of the gitoxide project for shared worktree related types and utilities
BuildArch:      noarch
%description -n %{name}+sha256-devel

This package contains library source intended for building other packages which
use the "sha256" feature of the "%{crate}" crate.

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
%files -n rust-gix-worktree-devel -f %{oreon_filedir}/rust-gix-worktree-devel.list

%changelog

%autochangelog
