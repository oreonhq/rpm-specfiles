%global source0_hash 98727bc8ec8ef4ed2aafd3ae0f2bd145d8aa7215e8d5cab6ef6688979242f33c

Name:           azove
Version:        2.0
Release:        33%{?dist}
Summary:        Another Zero-One Vertex Enumeration tool

License:        GPL-2.0-or-later
URL:            https://people.mpi-inf.mpg.de/alumni/d1/2019/behle/azove.html
Source0:        https://people.mpi-inf.mpg.de/alumni/d1/2019/behle/%{name}-%{version}.tar.gz
# Man page written by Jerry James from text found in the sources.  Therefore,
# the copyright and license of the man page is the same as the sources.
Source1:        %{name}2.1
# Sent upstream 2 Mar 2012: add an include that used to be implicit.
Patch:          %{name}-include.patch
# Polymake patch to use static node allocation.  Dynamic node allocation is
# unreliable on newer Linux kernels.
Patch:          %{name}-memory.patch
# Use std::unordered_multimap instead of the deprecated __gnu_cxx::hash_multimap
Patch:          %{name}-map.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make

%description
Azove is a tool designed for counting (without explicit enumeration) and
enumeration of 0/1 vertices.  Given a polytope by a linear relaxation or facet
description `P = {x | Ax <= b}`, all 0/1 points lying in P can be counted or
enumerated.  This is done by intersecting the polytope P with the
unit-hypercube `[0,1] d`.  The integral vertices (no fractional ones) of this
intersection will be enumerated.  If P is a 0/1 polytope, azove solves the
vertex enumeration problem.  In fact it can also solve the 0/1 knapsack
problem and the 0/1 subset sum problem.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

%build
%make_build COMPILER_FLAGS='%{build_cflags} %{build_ldflags}'

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -p %{name}2 %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 -p %{SOURCE1} %{buildroot}%{_mandir}/man1

%files
%doc INSTALL README
%license COPYING
%{_bindir}/%{name}2
%{_mandir}/man1/%{name}2.1*

%changelog
%autochangelog
