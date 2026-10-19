%global source2_hash 5f9cf9fb6acb1972b35ae29119ce563bb60ec097656bc4b69b9bac2d04c7a147
%global source0_hash 63d63b8177c1596c5dff1b5468c67c11d5d7d13ea04d83bab181505c91b3eff4
%bcond check 0
%global crate tree-sitter-cli
Name:           rust-tree-sitter-cli
Version:        0.25.10
Release:        1%{?dist}
Summary:        CLI tool for developing, testing, and using Tree-sitter parsers
License:        MIT
URL:            https://crates.io/crates/tree-sitter-cli
Source0:        https://static.crates.io/crates/tree-sitter-cli/tree-sitter-cli-%{version}.crate
Source2:        https://github.com/tree-sitter/tree-sitter/raw/v%{version}/LICENSE#/LICENSE.upstream
Patch:          tree-sitter-cli-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        CLI tool for developing, testing, and using Tree-sitter parsers
License:        %{shrink:
                MIT
                AND (MIT OR Apache-2.0)
                AND Apache-2.0
                AND (Apache-2.0 OR BSL-1.0)
                AND (Apache-2.0 OR MIT)
                AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
                AND (BSD-2-Clause OR Apache-2.0 OR MIT)
                AND ISC
                AND BSD-2-Clause
                AND BSD-3-Clause
                AND LGPL-3.0-or-later
                AND LicenseRef-Fedora-Public-Domain
                AND Unicode-3.0
                AND Unicode-DFS-2016
                AND (Unlicense OR MIT)
                AND Zlib
                AND (Zlib OR Apache-2.0 OR MIT)
                }
Recommends:     gcc
Recommends:     nodejs
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        CLI tool for developing, testing, and using Tree-sitter parsers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE2} LICENSE
rm -rf npm
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n tree-sitter-cli -f %{oreon_filedir}/tree-sitter-cli.list
%files -n rust-tree-sitter-cli-devel -f %{oreon_filedir}/rust-tree-sitter-cli-devel.list

%changelog

%autochangelog
