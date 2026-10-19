%global source0_hash f020237b6c8eed93db2e2cb53c00c60a8e1bc73da7d073199a1180401450218d
%bcond check 0
%global debug_package %{nil}
%global crate regex
Name:           rust-regex
Version:        1.13.1
Release:        1%{?dist}
Summary:        Implementation of regular expressions for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/regex
Source0:        https://static.crates.io/crates/regex/regex-%{version}.crate
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
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+pattern-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+pattern-devel

This package contains library source intended for building other packages which
use the "pattern" feature of the "%{crate}" crate.

%package     -n %{name}+perf-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+perf-devel

This package contains library source intended for building other packages which
use the "perf" feature of the "%{crate}" crate.

%package     -n %{name}+perf-backtrack-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+perf-backtrack-devel

This package contains library source intended for building other packages which
use the "perf-backtrack" feature of the "%{crate}" crate.

%package     -n %{name}+perf-cache-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+perf-cache-devel

This package contains library source intended for building other packages which
use the "perf-cache" feature of the "%{crate}" crate.

%package     -n %{name}+perf-dfa-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+perf-dfa-devel

This package contains library source intended for building other packages which
use the "perf-dfa" feature of the "%{crate}" crate.

%package     -n %{name}+perf-dfa-full-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+perf-dfa-full-devel

This package contains library source intended for building other packages which
use the "perf-dfa-full" feature of the "%{crate}" crate.

%package     -n %{name}+perf-inline-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+perf-inline-devel

This package contains library source intended for building other packages which
use the "perf-inline" feature of the "%{crate}" crate.

%package     -n %{name}+perf-literal-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+perf-literal-devel

This package contains library source intended for building other packages which
use the "perf-literal" feature of the "%{crate}" crate.

%package     -n %{name}+perf-onepass-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+perf-onepass-devel

This package contains library source intended for building other packages which
use the "perf-onepass" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+unicode-devel

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-age-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+unicode-age-devel

This package contains library source intended for building other packages which
use the "unicode-age" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-bool-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+unicode-bool-devel

This package contains library source intended for building other packages which
use the "unicode-bool" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-case-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+unicode-case-devel

This package contains library source intended for building other packages which
use the "unicode-case" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-gencat-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+unicode-gencat-devel

This package contains library source intended for building other packages which
use the "unicode-gencat" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-perl-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+unicode-perl-devel

This package contains library source intended for building other packages which
use the "unicode-perl" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-script-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+unicode-script-devel

This package contains library source intended for building other packages which
use the "unicode-script" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-segment-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+unicode-segment-devel

This package contains library source intended for building other packages which
use the "unicode-segment" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+use_std-devel
Summary:        Implementation of regular expressions for Rust
BuildArch:      noarch
%description -n %{name}+use_std-devel

This package contains library source intended for building other packages which
use the "use_std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
sed -r -i 's@^mod fuzz;@// &@' tests/lib.rs
sed -r -i 's@^([[:blank:]]*)(load!\("fowler/)@\1// \2@' tests/lib.rs
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
%files -n rust-regex-devel -f %{oreon_filedir}/rust-regex-devel.list

%changelog

%autochangelog
