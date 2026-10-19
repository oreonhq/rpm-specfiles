%global source0_hash 8b8c00544d0e44d092c825b6a9b7c3d5e6df835b68c21f4f9ca9392fe005f9e5
%bcond check 1
%global crate rbspy
Name:           rust-rbspy
Version:        0.34.1
Release:        1%{?dist}
Summary:        Sampling CPU profiler for Ruby
License:        MIT
URL:            https://crates.io/crates/rbspy
Source0:        https://static.crates.io/crates/rbspy/rbspy-%{version}.crate
Patch:          rbspy-fix-metadata-auto.diff
Patch:          rbspy-fix-metadata.diff
ExcludeArch:    %{ix86}
%if %{with check}
%endif
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  ruby
BuildRequires:  rubygems
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Sampling CPU profiler for Ruby
License:        %{shrink:
    MIT AND
    Apache-2.0 AND
    CDDL-1.0 AND
    MPL-2.0 AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (Apache-2.0 OR BSD-2-Clause OR MIT) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (Unlicense OR MIT)
}
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Sampling CPU profiler for Ruby
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%ifarch s390x
%{cargo_test -- -- %{shrink:
    --skip core::ruby_spy::tests::test_get_trace
    --skip core::ruby_spy::tests::test_get_trace_when_process_has_exited
    --skip sampler::tests::test_sample_single_process_with_time_limit
    --skip sampler::tests::test_sample_single_process
    --skip sampler::tests::test_sample_subprocesses
    --skip test_get_ruby_stack_trace
}}
%else
%{cargo_test -- -- %{shrink:
    --skip core::ruby_spy::tests::test_get_trace
    --skip core::ruby_spy::tests::test_get_trace_when_process_has_exited
    --skip sampler::tests::test_sample_single_process_with_time_limit
    --skip sampler::tests::test_sample_single_process
    --skip sampler::tests::test_sample_subprocesses
}}
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rbspy -f %{oreon_filedir}/rbspy.list
%files -n rust-rbspy-devel -f %{oreon_filedir}/rust-rbspy-devel.list

%changelog

%autochangelog
