%global source0_hash none
Name:           ocaml-srpm-macros
Version:        11
Release:        1%{?dist}
Summary:        OCaml architecture macros
License:        GPL-2.0-or-later
BuildArch:      noarch
Source0:        macros.ocaml-srpm
# oreon:deps

# /oreon:deps
%description
This package contains macros needed by RPM in order to build
SRPMS.  It does not pull in any other OCaml dependencies.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%build

%install
mkdir -p $RPM_BUILD_ROOT%{rpmmacrodir}
install -p -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{rpmmacrodir}/macros.ocaml-srpm
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 11-3
- Prepare for Oreon 11 (RP1)
