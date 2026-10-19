%global source0_hash f54a637f6c17ef2d94f767da641afea9bec726c31501cb828d9b948b1507c7c4
Name: swarp
Version: 2.38.0
Release:        1%{?dist}
Summary:        Tool that resamples and co-adds together FITS images
License: GPL-3.0-or-later
URL: http://www.astromatic.net/software/%{name}
Source0:        http://www.astromatic.net/download/swarp/swarp-%{version}.tar.gz
Patch: fix-gcc15.patch
%define _legacy_common_support 1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
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
%oreon_prep
%build

%configure --enable-threads
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n swarp-doc -f %{oreon_filedir}/swarp-doc.list

%changelog

%autochangelog
