%global source0_hash 868ae8d9f15283f67be3193b1f2eebb73e3a4b16b313b6932b4c66474906e1c3
%global debug_package %{nil}

Name: ocaml-srpm-macros
Version: 11
Release: 1%{?dist}
Summary: OCaml architecture macros
License: GPL-2.0-or-later
URL: https://ocaml.org/
BuildArch: noarch
Source0: macros.ocaml-srpm

BuildRequires: oreon-rpm-macros

%description
Architecture macros RPM needs before an OCaml SRPM is built. This package does not require the OCaml compiler.

%prep
%oreon_sha256

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.ocaml-srpm

%files
%{_rpmmacrodir}/macros.ocaml-srpm
