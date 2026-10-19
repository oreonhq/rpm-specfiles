%global source0_hash 5d7dfd5278fe9ccb360b3b8ee82a61b874477d54766944086f9e3bc9f98c3fed
%bcond check 1
%global crate jql
Name:           rust-jql
Version:        8.0.9
Release:        1%{?dist}
Summary:        JQL is a fast and simple command-line tool to manipulate JSON data
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/jql
Source0:        https://static.crates.io/crates/jql/jql-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        JQL is a fast and simple command-line tool to manipulate JSON data
License:        (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND EPL-2.0 AND MIT AND (Unlicense OR MIT)
%description -n %{crate}

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n jql -f %{oreon_filedir}/jql.list

%changelog

%autochangelog
