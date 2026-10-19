%global source0_hash 23e3600093de3daa60dbbfd1edff258504f41f0fcfcb5537ddff78711b0d2eb2
%bcond check 1
Name:           hyfetch
Version:        2.1.0
Release:        1%{?dist}
Summary:        Customizable Linux System Information Script
License:        %{shrink:
    Apache-2.0 AND
    Apache-2.0 OR BSL-1.0 AND
    Apache-2.0 OR MIT AND
    Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT AND
    ISC AND
    LGPL-3.0-or-later AND
    MIT AND
    MIT OR Apache-2.0 AND
    MIT OR Apache-2.0 OR CC0-1.0 AND
    MPL-2.0 AND
    Unlicense OR MIT
}
URL:            https://github.com/hykilpikonna/hyfetch
Source0:        https://github.com/hykilpikonna/hyfetch/archive/%{version}/hyfetch-%{version}.tar.gz
Source1:        hyfetch-vendor-%{version}.tar.gz
Patch0:         hyfetch-fix-metadata-auto.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description
HyFetch is a command line tool to display information about your
Linux system, such as amount of installed packages, OS and kernel
version, active GTK theme, CPU info, and used/available memory.
It is a fork of neofetch, and adds pride flag coloration to the OS logo.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1 -a1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
%install
install -pDm755 target/release/hyfetch %{buildroot}%{_bindir}/hyfetch
install -pDm644 docs/hyfetch.1 %{buildroot}%{_mandir}/man1/hyfetch.1
install -pDm644 hyfetch/scripts/autocomplete.bash %{buildroot}%{bash_completions_dir}/hyfetch
install -pDm644 hyfetch/scripts/autocomplete.zsh %{buildroot}%{zsh_completions_dir}/_hyfetch
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
