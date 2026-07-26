%global source0_hash c147fe0a94b32d323ef60be9fdcc9b683d1a82cd7513786229ef294310b5b6e2

Name: pngnq
Summary: Pngnq is a tool for quantizing PNG images in RGBA format
Version: 1.1
Release: 38%{?dist}
License: BSD-4-Clause and MIT and BSD-3-Clause
URL: http://pngnq.sourceforge.net/
Source0: http://downloads.sourceforge.net/pngnq/pngnq-%{version}.tar.gz
Patch0: pngnq-libpng15.patch
Patch1: pngnq-c99.patch
Patch2: pngnq-gcc14.patch

BuildRequires: make
BuildRequires: libpng-devel
BuildRequires: gcc

%description
Pngnq is a tool for quantizing PNG images in RGBA format.

The neuquant algorithm uses a neural network to optimise the color
map selection. This is fast and quite accurate, giving good results
on many types of images.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__make} DESTDIR=%{buildroot} install

%files
%doc COPYING README*
%{_bindir}/*
%{_mandir}/man1/*1*

%changelog
%autochangelog
