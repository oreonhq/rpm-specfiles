%global source0_hash 98727bc8ec8ef4ed2aafd3ae0f2bd145d8aa7215e8d5cab6ef6688979242f33c
Name:           azove
Version:        2.0
Release:        1%{?dist}
Summary:        Another Zero-One Vertex Enumeration tool
License:        GPL-2.0-or-later
URL:            https://people.mpi-inf.mpg.de/alumni/d1/2019/behle/azove.html
Source0:        https://people.mpi-inf.mpg.de/alumni/d1/2019/behle/%{name}-%{version}.tar.gz
Source1:        %{name}2.1
Patch:          %{name}-include.patch
Patch:          %{name}-memory.patch
Patch:          %{name}-map.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
