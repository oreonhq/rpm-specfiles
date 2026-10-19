%global source0_hash 8458304d9ba64d4cc871ed5aa43b07fa8d0a89451a39aed33f5cd58dd4a618c7
%bcond check 1
%global crate just
Name:           rust-just
Version:        1.47.1
Release:        1%{?dist}
Summary:        Just a command runner
License:        CC0-1.0
URL:            https://crates.io/crates/just
Source0:        https://static.crates.io/crates/just/just-%{version}.crate
Patch:          just-fix-metadata-auto.diff
Patch:          just-fix-metadata.diff
Patch2:         just-exclude-unwanted-files.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Just a command runner
License:        %{shrink:
                CC0-1.0
                AND Apache-2.0
                AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception)
                AND (Apache-2.0 OR MIT)
                AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
                AND BSD-2-Clause
                AND MIT
                AND (MIT-0 OR Apache-2.0)
                AND MPL-2.0
                AND Unicode-DFS-2016
                AND (Unlicense OR MIT)
                }
Recommends:     fzf
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Just a command runner
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
target/rpm/just --man > target/rpm/just.1
%install
%cargo_install
install -D -m644 -pv target/rpm/just.1    %{buildroot}%{_mandir}/man1/just.1
install -D -m644 -pv completions/just.bash %{buildroot}%{bash_completions_dir}/just
install -D -m644 -pv completions/just.fish %{buildroot}%{fish_completions_dir}/just.fish
install -D -m644 -pv completions/just.zsh  %{buildroot}%{zsh_completions_dir}/_just
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -- -- %{shrink:
    --skip completions::bash
    --skip completions::tests::scripts
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n just -f %{oreon_filedir}/just.list
%files -n rust-just-devel -f %{oreon_filedir}/rust-just-devel.list

%changelog

%autochangelog
