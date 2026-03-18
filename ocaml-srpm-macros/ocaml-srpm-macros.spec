# OCaml has a bytecode backend that works on anything with a C
# compiler, and a native code backend available on a subset of
# architectures.  A further subset of architectures support native
# dynamic linking.
#
# This package contains a file needed to define some RPM macros
# which are required before any SRPM is built.
#
# See also: https://bugzilla.redhat.com/show_bug.cgi?id=1087794

Name:           ocaml-srpm-macros
Version:        11
Release:        3%{?dist}

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


%build


%install
mkdir -p $RPM_BUILD_ROOT%{rpmmacrodir}
install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{rpmmacrodir}/macros.ocaml-srpm


%files
%{rpmmacrodir}/macros.ocaml-srpm


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 11-3
- Prepare for Oreon 11 (RP1)
