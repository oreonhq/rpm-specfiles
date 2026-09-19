%global source0_hash 18821588b2dc5bf159aa37d3bcb7b885d85ffd1e19f23a0c57a58723fea85f48

Summary:	Binary diff/patch utility
Name:		bsdiff
Version:	4.3
Release:	39%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
Source0:	http://www.daemonology.net/bsdiff/bsdiff-%{version}.tar.gz
URL:		http://www.daemonology.net/bsdiff/
BuildRequires:  gcc
BuildRequires:	bzip2-devel

%description
bsdiff and bspatch are tools for building and applying patches to binary files.
By using suffix sorting (specifically, Larsson and Sadakane's qsufsort) and
taking advantage of how executable files change, bsdiff routinely produces
binary patches 50-80% smaller than those produced by Xdelta, and 15% smaller
than those produced by .RTPatch.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{__cc} bsdiff.c -o bsdiff ${RPM_OPT_FLAGS} -lbz2
%{__cc} bspatch.c -o bspatch ${RPM_OPT_FLAGS} -lbz2

%install
rm -rf ${RPM_BUILD_ROOT}
install -d -m 755 ${RPM_BUILD_ROOT}%{_bindir}
install -d -m 755 ${RPM_BUILD_ROOT}%{_mandir}/man1
install -m 755 bsdiff bspatch ${RPM_BUILD_ROOT}%{_bindir}
install -m 644 bsdiff.1 bspatch.1 ${RPM_BUILD_ROOT}%{_mandir}/man1

%files
%{_bindir}/bsdiff
%{_bindir}/bspatch
%{_mandir}/man1/*

%changelog
%autochangelog
