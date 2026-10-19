%global source0_hash 0493c6fb308d367d0aed7acd341adbc1c2f216c135073e4b73b652c5d0d6b54c
%bcond check 0
%global debug_package %{nil}
%global crate hyphenation
Name:           rust-hyphenation0.7
Version:        0.7.1
Release:        1%{?dist}
Summary:        Knuth-Liang hyphenation for a variety of languages
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/hyphenation
Source0:        https://static.crates.io/crates/hyphenation/hyphenation-%{version}.crate
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

%package     -n %{name}+build_dictionaries-devel
Summary:        Knuth-Liang hyphenation for a variety of languages
BuildArch:      noarch
%description -n %{name}+build_dictionaries-devel

This package contains library source intended for building other packages which
use the "build_dictionaries" feature of the "%{crate}" crate.

%package     -n %{name}+embed_all-devel
Summary:        Knuth-Liang hyphenation for a variety of languages
BuildArch:      noarch
%description -n %{name}+embed_all-devel

This package contains library source intended for building other packages which
use the "embed_all" feature of the "%{crate}" crate.

%package     -n %{name}+nfc-devel
Summary:        Knuth-Liang hyphenation for a variety of languages
BuildArch:      noarch
%description -n %{name}+nfc-devel

This package contains library source intended for building other packages which
use the "nfc" feature of the "%{crate}" crate.

%package     -n %{name}+nfd-devel
Summary:        Knuth-Liang hyphenation for a variety of languages
BuildArch:      noarch
%description -n %{name}+nfd-devel

This package contains library source intended for building other packages which
use the "nfd" feature of the "%{crate}" crate.

%package     -n %{name}+nfkc-devel
Summary:        Knuth-Liang hyphenation for a variety of languages
BuildArch:      noarch
%description -n %{name}+nfkc-devel

This package contains library source intended for building other packages which
use the "nfkc" feature of the "%{crate}" crate.

%package     -n %{name}+nfkd-devel
Summary:        Knuth-Liang hyphenation for a variety of languages
BuildArch:      noarch
%description -n %{name}+nfkd-devel

This package contains library source intended for building other packages which
use the "nfkd" feature of the "%{crate}" crate.

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
%files -n rust-hyphenation0.7-devel -f %{oreon_filedir}/rust-hyphenation0.7-devel.list

%changelog

%autochangelog
