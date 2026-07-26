%global source0_hash f54a637f6c17ef2d94f767da641afea9bec726c31501cb828d9b948b1507c7c4

Name: swarp
Version: 2.38.0
Release: 29%{?dist}
Summary: Tool that resamples and co-adds together FITS images

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://www.astromatic.net/software/%{name}
Source: http://www.astromatic.net/download/swarp/swarp-%{version}.tar.gz
Patch: fix-gcc15.patch

# https://gcc.gnu.org/gcc-10/porting_to.html#common
# https://github.com/astromatic/sextractor/issues/12
%define _legacy_common_support 1

BuildRequires: make
BuildRequires: gcc

%description
SWarp is a program that resamples and co-adds together FITS images 
using any arbitrary astrometric projection defined in the WCS standard. 

%package doc
Summary: Documentation for %{name}
BuildArch: noarch

%description doc
This package contains the documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --enable-threads
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS BUGS COPYRIGHT HISTORY README THANKS TODO
%license COPYRIGHT
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/manx/*
%{_datadir}/%{name}/

%files doc
%doc doc/swarp.pdf 
%license COPYRIGHT

%changelog
%autochangelog
