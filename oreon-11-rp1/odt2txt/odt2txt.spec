%global source0_hash 23a889109ca9087a719c638758f14cc3b867a5dcf30a6c90bf6a0985073556dd

Name:           odt2txt
Version:        0.5
Release:        18%{?dist}
Summary:        Converts an OpenDocument to plain text

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://stosberg.net/odt2txt/
Source0:        https://github.com/dstosberg/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         odt2txt-makefile.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  zlib-devel

%description
odt2txt is a command-line tool which extracts the text out of OpenDocument Texts
produced by LibreOffice, OpenOffice, StarOffice, KOffice and others.

odt2txt is...

* small
* supports multiple output encodings
* adopts to your locale
* able to substitute common characters which the output charset does
  not contain with ascii look-a-likes
* written in C, has few dependencies
* portable (runs on Linux, *BSD, Solaris, HP-UX, Windows, Cygwin)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
%make_install PREFIX=%{_prefix}

%files
%license GPL-2
%doc README.md
%{_bindir}/odt2txt
%{_mandir}/man*/*

%changelog
%autochangelog
