%global source0_hash 1bc03214a29c4fc461a7aa11b9a3debde419b1271fa5110273ded961774e2b6f

Name:		psftools
Version:	1.0.10
Release:	19%{?dist}
Summary:	Conversion tools for .PSF fonts

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://www.seasip.info/Unix/PSF/
Source0:	https://www.seasip.info/Unix/PSF/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:	gcc

%description
The PSFTOOLS are designed to manipulate fixed-width bitmap fonts, such as DOS
or Linux console fonts. Both the PSF1 (8 pixels wide) and PSF2 (any width)
formats are supported; the default output format is PSF2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure --disable-shared
make %{?_smp_mflags}

%install
%make_install

%files
%{_bindir}/*
%{_mandir}/man1/*
%exclude %{_includedir}/*.h
%exclude %{_libdir}/*
%doc doc/*.txt
%doc NEWS AUTHORS
%license COPYING

%changelog
%autochangelog
