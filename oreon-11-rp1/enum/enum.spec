%global source0_hash 9ba7fda59f183ca4dfd4b5f6654af8a0d36bbe3a846a16be764d8a32869ee480

Name: enum
Version: 1.1
Release: 32%{?dist}
Summary: Seq- and jot-like enumerator

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://fedorahosted.org/enum
Source0: https://fedorahosted.org/releases/e/n/enum/%{name}-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: make

%description
Utility enum enumerates values (numbers) between two values, possibly
further adjusted by a step and/or a count, all given on the command line.
Before printing, values are passed through a formatter. Very fine control
over input interpretation and output is possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-doc-rebuild
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%check
make check

%files
%doc COPYING ChangeLog
%_mandir/man1/enum.1*
%_bindir/enum

%changelog
%autochangelog
