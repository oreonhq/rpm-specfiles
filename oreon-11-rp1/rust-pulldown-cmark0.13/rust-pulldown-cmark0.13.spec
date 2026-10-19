%global source0_hash e9f068eba8e7071c5f9511831b44f32c740d5adf574e990f946ddb53db2f314e
%bcond check 0
%global debug_package %{nil}
%global crate pulldown-cmark
Name:           rust-pulldown-cmark0.13
Version:        0.13.4
Release:        1%{?dist}
Summary:        A pull parser for CommonMark
License:        MIT
URL:            https://crates.io/crates/pulldown-cmark
Source0:        https://static.crates.io/crates/pulldown-cmark/pulldown-cmark-%{version}.crate
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
Summary:        A pull parser for CommonMark
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gen-tests-devel
Summary:        A pull parser for CommonMark
BuildArch:      noarch
%description -n %{name}+gen-tests-devel

This package contains library source intended for building other packages which
use the "gen-tests" feature of the "%{crate}" crate.

%package     -n %{name}+getopts-devel
Summary:        A pull parser for CommonMark
BuildArch:      noarch
%description -n %{name}+getopts-devel

This package contains library source intended for building other packages which
use the "getopts" feature of the "%{crate}" crate.

%package     -n %{name}+html-devel
Summary:        A pull parser for CommonMark
BuildArch:      noarch
%description -n %{name}+html-devel

This package contains library source intended for building other packages which
use the "html" feature of the "%{crate}" crate.

%package     -n %{name}+pulldown-cmark-escape-devel
Summary:        A pull parser for CommonMark
BuildArch:      noarch
%description -n %{name}+pulldown-cmark-escape-devel

This package contains library source intended for building other packages which
use the "pulldown-cmark-escape" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A pull parser for CommonMark
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        A pull parser for CommonMark
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

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
%files -n rust-pulldown-cmark0.13-devel -f %{oreon_filedir}/rust-pulldown-cmark0.13-devel.list

%changelog

%autochangelog
