# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 868ae8d9f15283f67be3193b1f2eebb73e3a4b16b313b6932b4c66474906e1c3


%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
# OCaml has a bytecode backend that works on anything with a C
# compiler, and a native code backend available on a subset of
# architectures.  A further subset of architectures support native
# dynamic linking.
#
# This package contains a file needed to define some RPM macros
# which are required before any SRPM is built.
#

Name:           ocaml-srpm-macros
Version:        11
Release:        2%{?dist}

Summary:        OCaml architecture macros
License:        GPL-2.0-or-later

BuildArch:      noarch

Source0:        macros.ocaml-srpm

# NB. This package MUST NOT Require anything (except for dependencies
# that RPM itself generates).

%description
This package contains macros needed by RPM in order to build
SRPMS.  It does not pull in any other OCaml dependencies.


%prep
echo "%{source0_hash}  %{SOURCE0}" | sha256sum -c -



%build


%install
mkdir -p $RPM_BUILD_ROOT%{rpmmacrodir}
install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{rpmmacrodir}/macros.ocaml-srpm


%files
%{rpmmacrodir}/macros.ocaml-srpm


