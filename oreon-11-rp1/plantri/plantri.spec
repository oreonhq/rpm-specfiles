%global source0_hash e78a944116fec9f2c9f5e484206276cc2b0043bae803e9815f4b2683614629b8

Name:           plantri
Version:        5.8
Release:        %autorelease
Summary:        Generate certain types of planar graphs

%global upstreamver %{gsub %version %. %{quote:}}

License:        Apache-2.0
URL:            https://users.cecs.anu.edu.au/~bdm/plantri/
Source:         %{url}plantri%{upstreamver}.tar.gz
# Eliminate many warnings about use of uninitialized variables
Patch:          %{name}-uninitialized.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make

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

%files
%doc fullgen-guide.txt more-counts.txt plantri-guide.txt
%license LICENSE-2.0.txt
%{_bindir}/plantri
%{_bindir}/fullgen

%changelog
%autochangelog
