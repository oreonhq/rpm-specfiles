%global source0_hash fe20da34e0d3ba0cf6388701f44ac22224cf65130ddbc5fcbc27bc4949a6e1ad

Summary:       Free de-archiver for old ARC and ARK archives
Name:          nomarch
Version:       1.4
Release:       36%{?dist}
License:       GPL-2.0-or-later
URL:           https://www.svgalib.org/rus/nomarch.html
Source0:       https://www.ibiblio.org/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: make

%description
nomarch is a free de-archiving only replacement for the non-free arc archiver
from SEA. It can list, extract and test *.arc and *.ark archives. This is a
very outdated archive format, which should never be used for anything new, but
quite common for old CP/M or MS-DOS stuff.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install \
  BINDIR="%{buildroot}%{_bindir}" MANDIR="%{buildroot}%{_mandir}/man1"

%files
%license COPYING
%doc ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
