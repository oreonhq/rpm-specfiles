%global source0_hash 531e46835a22af56d1e3b66f04844bed63158bc094a628bec1d321d9b4c44bf2
%bcond check 1
%global debug_package %{nil}
%global crate fancy-regex
Name:           rust-fancy-regex0.13
Version:        0.13.0
Release:        1%{?dist}
Summary:        An implementation of regexes, supporting a relatively rich set of features
License:        MIT
URL:            https://crates.io/crates/fancy-regex
Source0:        https://static.crates.io/crates/fancy-regex/fancy-regex-%{version}.crate
Patch:          fancy-regex-fix-metadata.diff
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
Summary:        An implementation of regexes, supporting a relatively rich set of features
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+perf-devel
Summary:        An implementation of regexes, supporting a relatively rich set of features
BuildArch:      noarch
%description -n %{name}+perf-devel

This package contains library source intended for building other packages which
use the "perf" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        An implementation of regexes, supporting a relatively rich set of features
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+track_caller-devel
Summary:        An implementation of regexes, supporting a relatively rich set of features
BuildArch:      noarch
%description -n %{name}+track_caller-devel

This package contains library source intended for building other packages which
use the "track_caller" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-devel
Summary:        An implementation of regexes, supporting a relatively rich set of features
BuildArch:      noarch
%description -n %{name}+unicode-devel

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

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
%files -n rust-fancy-regex0.13-devel -f %{oreon_filedir}/rust-fancy-regex0.13-devel.list

%changelog

%autochangelog
