%global source0_hash d273983c5a657a70a3e8f2a01329822f3b8c8172b73826411a55751e404a0a4a
%bcond check 0
%global debug_package %{nil}
%global crate nom
Name:           rust-nom7
Version:        7.1.3
Release:        1%{?dist}
Summary:        Byte-oriented, zero-copy, parser combinators library
License:        MIT
URL:            https://crates.io/crates/nom
Source0:        https://static.crates.io/crates/nom/nom-%{version}.crate
Patch:          nom-fix-metadata.diff
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
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+docsrs-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+docsrs-devel

This package contains library source intended for building other packages which
use the "docsrs" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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

%ifarch %{ix86} %{arm}
%cargo_test -- -- --skip issue_848_overflow_incomplete_bits_to_bytes
%else
%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-nom7-devel -f %{oreon_filedir}/rust-nom7-devel.list

%changelog

%autochangelog
