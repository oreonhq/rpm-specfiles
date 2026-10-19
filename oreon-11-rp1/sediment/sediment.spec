%global source0_hash 29bb1620a0dd29d73ba1212eb75a1e652e5039ba41d6218232bff9cd30d39ea2
Name:		sediment
Version:	0.9.4
Release:        1%{?dist}
Summary:        A function reordering tool set
License:	GPL-3.0-or-later
URL:		https://github.com/wcohen/sediment
Source0:        https://github.com/wcohen/sediment/archive/%{version}/%{name}-%{version}.tar.gz
Requires: python3dist(gv)
BuildArch: noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  python3-sphinx
# /oreon:deps
%description
The sediment tool set allows reordering of the functions in compiled
programs built with RPM to reduce the frequency of TLB misses and
decrease the number of pages in the resident set.  Sediment generates
call graphs from program execution and converts the call graphs into
link order information to improve code locality.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sediment-%{version}
%oreon_prep
%build

autoreconf -iv
%configure
make
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
