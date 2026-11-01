%global source0_hash bdf8d36a4d932e974095890774ef15b1831d91c4e16afac3914399bf38824e0d
%global debug_package %{nil}

Name: ocaml-srpm-macros
Version: 11
Release: 2%{?dist}
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
