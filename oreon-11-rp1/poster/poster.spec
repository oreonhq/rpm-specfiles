%global source0_hash 63bd6f01e40e68dda0ac11a4f416c70457bc6bbd254af720b7ea2874875fa4ba

Summary:        Scales PostScript images to span multiple pages
Name:           poster
Version:        20060221
Release:        40%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
Source:         ftp://ftp.kde.org/pub/kde/printing/%{name}.tar.bz2
URL:            http://printing.kde.org/downloads/

# Fixes a gs crash, see https://bugzilla.redhat.com/show_bug.cgi?id=436969
Patch0:         poster.fixes_gs_crash.patch

BuildRequires:  gcc
%description
Poster scales PostScript images to a larger size, and prints them on
larger media and/or tiles them to print on multiple sheets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0

%build
# The included Makefile is badly written
%{__cc} %{optflags} -lm -o poster poster.c %{?__global_ldflags}

%install
%{__install} -D -m755 -p poster   %{buildroot}%{_bindir}/poster
%{__install} -D -m644 -p poster.1 %{buildroot}%{_mandir}/man1/poster.1

%files
%{_mandir}/man1/poster.1*
%{_bindir}/poster
%doc COPYING ChangeLog README manual.ps

%changelog
%autochangelog
