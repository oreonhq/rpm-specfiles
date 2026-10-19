%global source0_hash 4f4cdac9e4065d7c48e30770f8665b8cef9a3a73a63a4056a33a5f395bc7cf75
%bcond check 0
%global debug_package %{nil}
%global crate fasteval
Name:           rust-fasteval
Version:        0.2.4
Release:        1%{?dist}
Summary:        Fast evaluation of algebraic expressions
License:        MIT
URL:            https://crates.io/crates/fasteval
Source0:        https://static.crates.io/crates/fasteval/fasteval-%{version}.crate
Patch:          0001-Rust-can-parse-Very-Long-nine-tails-since-1.55.0.patch
Patch:          0002-Docs-avoid-doc-test-error-when-unsafe-vars-are-not-e.patch
Patch:          0003-Docs-markdown-syntax-fix.patch
Patch:          0001-tests-update-to-scientic-notation.patch
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
Summary:        Fast evaluation of algebraic expressions
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alpha-keywords-devel
Summary:        Fast evaluation of algebraic expressions
BuildArch:      noarch
%description -n %{name}+alpha-keywords-devel

This package contains library source intended for building other packages which
use the "alpha-keywords" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Fast evaluation of algebraic expressions
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+unsafe-vars-devel
Summary:        Fast evaluation of algebraic expressions
BuildArch:      noarch
%description -n %{name}+unsafe-vars-devel

This package contains library source intended for building other packages which
use the "unsafe-vars" feature of the "%{crate}" crate.

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
%files -n rust-fasteval-devel -f %{oreon_filedir}/rust-fasteval-devel.list

%changelog

%autochangelog
