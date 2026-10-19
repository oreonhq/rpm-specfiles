%global source0_hash 27a87d8ad779bf9f8d1b997bfd44319108986f1243a0ebfe87b5083ce0d32a5b
%bcond check 0
%global cargo_install_lib 0
%global crate mdsh
Name:           rust-mdsh
Version:        0.7.0
Release:        1%{?dist}
Summary:        Markdown shell pre-processor
License:        MIT
URL:            https://crates.io/crates/mdsh
Source0:        https://static.crates.io/crates/mdsh/mdsh-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Markdown shell pre-processor
License:        MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
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
%files -n mdsh -f %{oreon_filedir}/mdsh.list

%changelog

%autochangelog
