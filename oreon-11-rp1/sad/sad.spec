%global source0_hash a67902b9edb287861668ee3e39482c17b41c60e244ece62b3f8016250286294f
%bcond check 0
%global cargo_install_lib 0
Name:           sad
Version:        0.4.32
Release:        1%{?dist}
Summary:        CLI search and replace tool
SourceLicense:  MIT
License:        (MIT OR Apache-2.0) AND Unicode-DFS-2016 AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MIT AND (Unlicense OR MIT)
URL:            https://github.com/ms-jpq/sad
Source0:        https://github.com/ms-jpq/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Recommends:     fzf
Recommends:     (git-delta or diff-so-fancy)
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n sad-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
