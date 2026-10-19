%global source0_hash 9cc6b15e217c21f0b7e3f4d9d32d3f71565d7a06f78fb22354f61b45ce988c91
%bcond check 1
%global crate sequoia-sq
Name:           rust-sequoia-sq
Version:        1.4.1
Release:        1%{?dist}
Summary:        Command-line frontends for Sequoia
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-sq
Source0:        https://static.crates.io/crates/sequoia-sq/sequoia-sq-%{version}.crate
Patch:          sequoia-sq-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Command-line frontends for Sequoia
License:        %{shrink:
    LGPL-2.0-or-later AND
    Apache-2.0 AND
    BSL-1.0 AND
    BSD-3-Clause AND
    MIT AND
    MPL-2.0 AND
    Unicode-3.0 AND
    Unicode-DFS-2016 AND
    Zlib AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (BSD-2-Clause OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
Obsoletes:      sequoia-wot < 0.13.0-1
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -vr subplot/
rm -v tests/sq-subplot.rs
%oreon_vendor_cargo
%build

export ASSET_OUT_DIR=target/assets
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
mkdir -p %{buildroot}/%{_mandir}/man1
cp -pav target/assets/man-pages/sq*.1 %{buildroot}/%{_mandir}/man1/
install -Dpm 0644 target/assets/shell-completions/sq.bash \
    %{buildroot}/%{bash_completions_dir}/sq.bash
install -Dpm 0644 target/assets/shell-completions/sq.fish \
    %{buildroot}/%{fish_completions_dir}/sq.fish
install -Dpm 0644 target/assets/shell-completions/_sq \
    %{buildroot}/%{zsh_completions_dir}/_sq
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n sequoia-sq -f %{oreon_filedir}/sequoia-sq.list

%changelog

%autochangelog
