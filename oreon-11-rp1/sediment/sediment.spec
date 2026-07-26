%global source0_hash 29bb1620a0dd29d73ba1212eb75a1e652e5039ba41d6218232bff9cd30d39ea2

Name:		sediment
Version:	0.9.4
Release:	4%{?dist}
Summary:	A function reordering tool set

License:	GPL-3.0-or-later
URL:		https://github.com/wcohen/sediment
Source0:	https://github.com/wcohen/sediment/archive/%{version}/%{name}-%{version}.tar.gz

# sphinx is used for building documentation:
BuildRequires: make
BuildRequires: python3-sphinx >= 2.0
BuildRequires: automake
BuildRequires: autoconf
#Requires: gcc-python3-plugin
Requires: python3dist(gv)
BuildArch: noarch

%description
The sediment tool set allows reordering of the functions in compiled
programs built with RPM to reduce the frequency of TLB misses and
decrease the number of pages in the resident set.  Sediment generates
call graphs from program execution and converts the call graphs into
link order information to improve code locality.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sediment-%{version}

%build
autoreconf -iv
%configure
# doc makefile using sphinx does not work with parallel build
make

%install
%make_install

%files
%{_bindir}/gv2link
%{_bindir}/perf2gv
%{_bindir}/gen_profile_merge
%{_bindir}/make_sediment_rpmmacros
%{_libexecdir}/%{name}
%{_docdir}/sediment/html
%doc README AUTHORS NEWS COPYING
%{_mandir}/man1/*

%changelog
%autochangelog
