%global source0_hash ad8553b9b26413251cbf30e620595c7a41b3887f03da04579c0e6b0d6a06b4b2
%bcond check 0
%global debug_package %{nil}
%global crate regex-automata
Name:           rust-regex-automata
Version:        0.4.18
Release:        1%{?dist}
Summary:        Automata construction and matching using regular expressions
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/regex-automata
Source0:        https://static.crates.io/crates/regex-automata/regex-automata-%{version}.crate
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
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+dfa-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+dfa-devel

This package contains library source intended for building other packages which
use the "dfa" feature of the "%{crate}" crate.

%package     -n %{name}+dfa-build-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+dfa-build-devel

This package contains library source intended for building other packages which
use the "dfa-build" feature of the "%{crate}" crate.

%package     -n %{name}+dfa-onepass-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+dfa-onepass-devel

This package contains library source intended for building other packages which
use the "dfa-onepass" feature of the "%{crate}" crate.

%package     -n %{name}+dfa-search-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+dfa-search-devel

This package contains library source intended for building other packages which
use the "dfa-search" feature of the "%{crate}" crate.

%package     -n %{name}+hybrid-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+hybrid-devel

This package contains library source intended for building other packages which
use the "hybrid" feature of the "%{crate}" crate.

%package     -n %{name}+internal-instrument-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+internal-instrument-devel

This package contains library source intended for building other packages which
use the "internal-instrument" feature of the "%{crate}" crate.

%package     -n %{name}+internal-instrument-pikevm-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+internal-instrument-pikevm-devel

This package contains library source intended for building other packages which
use the "internal-instrument-pikevm" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+meta-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+meta-devel

This package contains library source intended for building other packages which
use the "meta" feature of the "%{crate}" crate.

%package     -n %{name}+nfa-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+nfa-devel

This package contains library source intended for building other packages which
use the "nfa" feature of the "%{crate}" crate.

%package     -n %{name}+nfa-backtrack-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+nfa-backtrack-devel

This package contains library source intended for building other packages which
use the "nfa-backtrack" feature of the "%{crate}" crate.

%package     -n %{name}+nfa-pikevm-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+nfa-pikevm-devel

This package contains library source intended for building other packages which
use the "nfa-pikevm" feature of the "%{crate}" crate.

%package     -n %{name}+nfa-thompson-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+nfa-thompson-devel

This package contains library source intended for building other packages which
use the "nfa-thompson" feature of the "%{crate}" crate.

%package     -n %{name}+perf-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+perf-devel

This package contains library source intended for building other packages which
use the "perf" feature of the "%{crate}" crate.

%package     -n %{name}+perf-inline-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+perf-inline-devel

This package contains library source intended for building other packages which
use the "perf-inline" feature of the "%{crate}" crate.

%package     -n %{name}+perf-literal-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+perf-literal-devel

This package contains library source intended for building other packages which
use the "perf-literal" feature of the "%{crate}" crate.

%package     -n %{name}+perf-literal-multisubstring-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+perf-literal-multisubstring-devel

This package contains library source intended for building other packages which
use the "perf-literal-multisubstring" feature of the "%{crate}" crate.

%package     -n %{name}+perf-literal-substring-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+perf-literal-substring-devel

This package contains library source intended for building other packages which
use the "perf-literal-substring" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+syntax-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+syntax-devel

This package contains library source intended for building other packages which
use the "syntax" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+unicode-devel

This package contains library source intended for building other packages which
use the "unicode" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-age-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+unicode-age-devel

This package contains library source intended for building other packages which
use the "unicode-age" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-bool-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+unicode-bool-devel

This package contains library source intended for building other packages which
use the "unicode-bool" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-case-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+unicode-case-devel

This package contains library source intended for building other packages which
use the "unicode-case" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-gencat-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+unicode-gencat-devel

This package contains library source intended for building other packages which
use the "unicode-gencat" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-perl-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+unicode-perl-devel

This package contains library source intended for building other packages which
use the "unicode-perl" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-script-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+unicode-script-devel

This package contains library source intended for building other packages which
use the "unicode-script" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-segment-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+unicode-segment-devel

This package contains library source intended for building other packages which
use the "unicode-segment" feature of the "%{crate}" crate.

%package     -n %{name}+unicode-word-boundary-devel
Summary:        Automata construction and matching using regular expressions
BuildArch:      noarch
%description -n %{name}+unicode-word-boundary-devel

This package contains library source intended for building other packages which
use the "unicode-word-boundary" feature of the "%{crate}" crate.

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

%cargo_test -- --lib
%cargo_test -- --doc -- --skip nfa::thompson::compiler::Config::nfa_size_limit
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-regex-automata-devel -f %{oreon_filedir}/rust-regex-automata-devel.list

%changelog

%autochangelog
