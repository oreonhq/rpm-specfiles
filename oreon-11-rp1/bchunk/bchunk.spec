%global source0_hash e7d99b5b60ff0b94c540379f6396a670210400124544fb1af985dd3551eabd89

%global _hardened_build 1
%global debug_package %{nil}

Summary: CD image format converter from .bin/.cue to .iso/.cdr
Name: bchunk
Version: 1.2.2
Release: 21%{?dist}
URL: http://he.fi/bchunk/
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Source0: http://he.fi/bchunk/bchunk-%{version}.tar.gz
Patch0: bchunk-1.2.2-CFLAGS.patch

BuildRequires: gcc
BuildRequires: make

%description
The bchunk package contains a UNIX/C rewrite of the BinChunker program.
BinChunker converts a CD image in a .bin/.cue format (sometimes .raw/.cue)
into a set of .iso and .cdr tracks.  The .bin/.cue format is used by some
non-UNIX CD-writing software, but is not supported on most other
CD-writing programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 bchunk $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 bchunk.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc ChangeLog README
%license COPYING
%{_bindir}/bchunk
%{_mandir}/man1/bchunk.1.gz

%changelog
%autochangelog
