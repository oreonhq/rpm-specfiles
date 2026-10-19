%global source0_hash e78a944116fec9f2c9f5e484206276cc2b0043bae803e9815f4b2683614629b8
Name:           plantri
Version:        5.8
Release:        1%{?dist}
Summary:        Generate certain types of planar graphs
%global upstreamver %{gsub %version %. %{quote:}}
License:        Apache-2.0
URL:            https://users.cecs.anu.edu.au/~bdm/plantri/
Source0:        https://users.cecs.anu.edu.au/~bdm/%{name}/%{name}58.tar.gz
Patch:          %{name}-uninitialized.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Plantri and fullgen are programs for generating certain types of planar
graphs.  The authors are Gunnar Brinkmann (University of Ghent) and Brendan
McKay (Australian National University).

Graphs are generated in such a way that exactly one member of each isomorphism
class is output without the need for storing them.  The speed of generation is
more than 2,000,000 graphs per second in many cases, so extremely large
classes of graph can be exhaustively listed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}%{upstreamver} -p1

%build

%make_build CFLAGS='%{build_cflags}' LDFLAGS='%{build_ldflags}'
%install
mkdir -p %{buildroot}%{_bindir}
cp -p plantri fullgen %{buildroot}%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
