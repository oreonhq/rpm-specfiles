%global source0_hash e8619f6b7fa7915ae17d0215db0f564b10a0428b147f145df94c81f4f41297f0
%bcond check 1
%global cargo_install_lib 0
%global crate gengo-bin
Name:           rust-gengo-bin
Version:        0.15.0
Release:        1%{?dist}
Summary:        Get the language distribution stats of your repository
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gengo-bin
Source0:        https://static.crates.io/crates/gengo-bin/gengo-bin-%{version}.crate
Source10:       gengo.1
Source11:       gengo-git.1
Source12:       gengo-directory.1
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n gengo
Summary:        Get the language distribution stats of your repository
License:        %{shrink:
                Apache-2.0 AND
                (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND
                (Apache-2.0 OR MIT) AND
                (Apache-2.0 OR MIT OR Zlib) AND
                BSD-3-Clause AND
                MIT AND
                (MIT OR Unlicense) AND
                MPL-2.0 AND
                Unicode-3.0 AND
                Unicode-DFS-2016 AND
                Zlib
                }
%description -n gengo

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
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}'
%oreon_autofiles gengo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%{cargo_test -- -- --exact %{shrink:
    --skip test_json_output_on_javascript_repo
    --skip test_color_breakdown_javascript_repo
    --skip test_color_javascript_repo
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n gengo -f %{oreon_filedir}/gengo.list

%changelog

%autochangelog
