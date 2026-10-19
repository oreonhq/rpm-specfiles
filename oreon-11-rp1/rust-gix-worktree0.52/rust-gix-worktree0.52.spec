%global source0_hash d69955eb5e2910832f88d041964b809eee01dadd579237e0b55efec58fd406fd
%bcond check 0
%global debug_package %{nil}
%global crate gix-worktree
Name:           rust-gix-worktree0.52
Version:        0.52.0
Release:        1%{?dist}
Summary:        A crate of the gitoxide project for shared worktree related types and...
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
Summary:        A crate of the gitoxide project for shared worktree related types and...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+attributes-devel
Summary:        A crate of the gitoxide project for shared worktree related types and...
BuildArch:      noarch
%description -n %{name}+attributes-devel

This package contains library source intended for building other packages which
use the "attributes" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        A crate of the gitoxide project for shared worktree related types and...
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+gix-attributes-devel
Summary:        A crate of the gitoxide project for shared worktree related types and...
BuildArch:      noarch
%description -n %{name}+gix-attributes-devel

This package contains library source intended for building other packages which
use the "gix-attributes" feature of the "%{crate}" crate.

%package     -n %{name}+gix-validate-devel
Summary:        A crate of the gitoxide project for shared worktree related types and...
BuildArch:      noarch
%description -n %{name}+gix-validate-devel

This package contains library source intended for building other packages which
use the "gix-validate" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A crate of the gitoxide project for shared worktree related types and...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        A crate of the gitoxide project for shared worktree related types and...
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
%files -n rust-gix-worktree0.52-devel -f %{oreon_filedir}/rust-gix-worktree0.52-devel.list

%changelog

%autochangelog
