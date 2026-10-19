%global source0_hash dc08e0fa1a91ff5f24affeab052f198056645e1de004910bde7b82b50ea5982a
%bcond check 0
%global debug_package %{nil}
%global crate gix-diff
Name:           rust-gix-diff0.63
Version:        0.63.0
Release:        1%{?dist}
Summary:        Calculate differences between various git objects
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-diff
Source0:        https://static.crates.io/crates/gix-diff/gix-diff-%{version}.crate
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
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+blob-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+blob-devel

This package contains library source intended for building other packages which
use the "blob" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+gix-attributes-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+gix-attributes-devel

This package contains library source intended for building other packages which
use the "gix-attributes" feature of the "%{crate}" crate.

%package     -n %{name}+gix-command-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+gix-command-devel

This package contains library source intended for building other packages which
use the "gix-command" feature of the "%{crate}" crate.

%package     -n %{name}+gix-filter-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+gix-filter-devel

This package contains library source intended for building other packages which
use the "gix-filter" feature of the "%{crate}" crate.

%package     -n %{name}+gix-fs-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+gix-fs-devel

This package contains library source intended for building other packages which
use the "gix-fs" feature of the "%{crate}" crate.

%package     -n %{name}+gix-index-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+gix-index-devel

This package contains library source intended for building other packages which
use the "gix-index" feature of the "%{crate}" crate.

%package     -n %{name}+gix-path-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+gix-path-devel

This package contains library source intended for building other packages which
use the "gix-path" feature of the "%{crate}" crate.

%package     -n %{name}+gix-pathspec-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+gix-pathspec-devel

This package contains library source intended for building other packages which
use the "gix-pathspec" feature of the "%{crate}" crate.

%package     -n %{name}+gix-tempfile-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+gix-tempfile-devel

This package contains library source intended for building other packages which
use the "gix-tempfile" feature of the "%{crate}" crate.

%package     -n %{name}+gix-trace-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+gix-trace-devel

This package contains library source intended for building other packages which
use the "gix-trace" feature of the "%{crate}" crate.

%package     -n %{name}+gix-traverse-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+gix-traverse-devel

This package contains library source intended for building other packages which
use the "gix-traverse" feature of the "%{crate}" crate.

%package     -n %{name}+gix-worktree-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+gix-worktree-devel

This package contains library source intended for building other packages which
use the "gix-worktree" feature of the "%{crate}" crate.

%package     -n %{name}+imara-diff-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+imara-diff-devel

This package contains library source intended for building other packages which
use the "imara-diff" feature of the "%{crate}" crate.

%package     -n %{name}+index-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+index-devel

This package contains library source intended for building other packages which
use the "index" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-devel
Summary:        Calculate differences between various git objects
BuildArch:      noarch
%description -n %{name}+wasm-devel

This package contains library source intended for building other packages which
use the "wasm" feature of the "%{crate}" crate.

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
%files -n rust-gix-diff0.63-devel -f %{oreon_filedir}/rust-gix-diff0.63-devel.list

%changelog

%autochangelog
