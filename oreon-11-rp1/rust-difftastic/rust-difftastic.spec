%global source1_hash 8e9b5a167e7e91e60e128d58e948d607d3403aada83e3c389f2fcc713a46573a
%global source0_hash 53994203ee7eb591cb58b558af7bbc1a6901eee74575e52fcf97def8d97beaa7
%bcond check 1
%global crate difftastic
Name:           rust-difftastic
Version:        0.70.0
Release:        1%{?dist}
Summary:        Structural diff that understands syntax
License:        MIT
URL:            https://crates.io/crates/difftastic
Source0:        https://static.crates.io/crates/difftastic/difftastic-%{version}.crate
Source1:        https://github.com/Wilfred/difftastic/raw/%{version}/difft.1
Patch:          difftastic-fix-metadata.diff
Patch2:         difftastic-disable-tree-sitter-clojure-orchard.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Structural diff that understands syntax
License:        %{shrink:
  MIT
  AND (Apache-2.0 OR MIT) AND BSD-3-Clause
  AND Unicode-DFS-2016
  AND Apache-2.0
  AND (Apache-2.0 OR BSL-1.0)
  AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
  AND CECILL-C
  AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain
  AND (Unlicense OR MIT)
  AND Zlib
}
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{SOURCE1} .
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -p difft.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n difftastic -f %{oreon_filedir}/difftastic.list

%changelog

%autochangelog
