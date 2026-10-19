%global source0_hash b7b13833a0306bcb94e6a0ef52354fdb8c404b8dec452bc6e87e72e376cfac63
%bcond check 1
%global cargo_install_lib 0
%global crate onefetch
Name:           rust-onefetch
Version:        2.27.1
Release:        1%{?dist}
Summary:        Command-line Git information tool
License:        MIT
URL:            https://crates.io/crates/onefetch
Source0:        https://static.crates.io/crates/onefetch/onefetch-%{version}.crate
Patch:          onefetch-fix-metadata-auto.diff
Patch:          onefetch-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  help2man
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Command-line Git information tool
License:        %{shrink:
                (0BSD OR Apache-2.0 OR MIT) AND
                Apache-2.0 AND
                (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND
                (Apache-2.0 OR BSD-3-Clause) AND
                (Apache-2.0 OR BSL-1.0) AND
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
%description -n %{crate}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
help2man --no-info --output=onefetch.1 --name='%{summary}' target/rpm/onefetch
%install
%cargo_install
install -t %{buildroot}%{_mandir}/man1 -D -p -m 0644 onefetch.1
target/rpm/onefetch --generate bash > onefetch.bash
target/rpm/onefetch --generate fish > onefetch.fish
target/rpm/onefetch --generate zsh > _onefetch
install -Dpm 0644 onefetch.bash -t %{buildroot}/%{bash_completions_dir}
install -Dpm 0644 onefetch.fish -t %{buildroot}/%{fish_completions_dir}
install -Dpm 0644 _onefetch -t %{buildroot}/%{zsh_completions_dir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n onefetch -f %{oreon_filedir}/onefetch.list

%changelog

%autochangelog
