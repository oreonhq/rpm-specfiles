%global source0_hash ffd68cd406309e764be6af4d5cbcc309e132c13f3597c6a4570a1f218edd2c63

Name:           cd-discid
Version:        1.4
Release:        32%{?dist}
Summary:        Utility to get CDDB discid information

# Also "Larry Wall's Artistic" upstream, but that's not accepted in Fedora
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://linukz.org/cd-discid.shtml
Source0:        http://linukz.org/download/%{name}-%{version}.tar.gz
# https://github.com/taem/cd-discid/issues/5
Patch0:         https://patch-diff.githubusercontent.com/raw/taem/cd-discid/pull/6.patch
BuildRequires:  gcc
BuildRequires: make

%description
cd-discid is a backend utility to get CDDB discid information for a
CD-ROM disc.  It was originally designed for cdgrab (now abcde), but
can be used for any purpose requiring CDDB data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
%set_build_flags
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix} STRIP=:

%files
%license COPYING
%doc changelog README
%{_bindir}/cd-discid
%{_mandir}/man1/cd-discid.1*

%changelog
%autochangelog
