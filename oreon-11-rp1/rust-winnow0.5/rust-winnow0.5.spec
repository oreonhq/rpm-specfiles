%global source0_hash f593a95398737aeed53e489c785df13f3618e41dbcd6718c6addbf1395aa6876
%bcond check 1
%global debug_package %{nil}
%global crate winnow
Name:           rust-winnow0.5
Version:        0.5.40
Release:        1%{?dist}
Summary:        A byte-oriented, zero-copy, parser combinators library
License:        MIT
URL:            https://crates.io/crates/winnow
Source0:        https://static.crates.io/crates/winnow/winnow-%{version}.crate
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
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-doc-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+unstable-doc-devel

This package contains library source intended for building other packages which
use the "unstable-doc" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-recover-devel
Summary:        A byte-oriented, zero-copy, parser combinators library
BuildArch:      noarch
%description -n %{name}+unstable-recover-devel

This package contains library source intended for building other packages which
use the "unstable-recover" feature of the "%{crate}" crate.

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
%files -n rust-winnow0.5-devel -f %{oreon_filedir}/rust-winnow0.5-devel.list

%changelog

%autochangelog
