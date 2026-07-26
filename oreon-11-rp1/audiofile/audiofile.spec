%global source0_hash cdc60df19ab08bfe55344395739bb08f50fc15c92da3962fac334d3bff116965

%global make_check 1

Summary: Library for accessing various audio file formats
Name: audiofile
Version: 0.3.6
Release: 44%{?dist}
Epoch: 1
# library is LGPL / the two programs GPL / see README
License: LGPL-2.1-or-later and GPL-2.0-or-later
Source: http://audiofile.68k.org/%{name}-%{version}.tar.gz
URL: http://audiofile.68k.org/
BuildRequires:  gcc-c++
BuildRequires: libtool
BuildRequires: alsa-lib-devel
BuildRequires: flac-devel
BuildRequires: make
BuildRequires: chrpath
# optional for rebuilding manual pages from .txt
#BuildRequires: asciidoc

Patch0: audiofile-0.3.6-CVE-2015-7747.patch
# fixes to make build with GCC 6
Patch1: audiofile-0.3.6-left-shift-neg.patch
Patch2: audiofile-0.3.6-narrowing.patch
# pull requests #42,#43,#44
Patch3: audiofile-0.3.6-pull42.patch
Patch4: audiofile-0.3.6-pull43.patch
Patch5: audiofile-0.3.6-pull44.patch
Patch6: 822b732fd31ffcb78f6920001e9b1fbd815fa712.patch
Patch7: 941774c8c0e79007196d7f1e7afdc97689f869b3.patch
Patch8: fde6d79fb8363c4a329a184ef0b107156602b225.patch
Patch9: integer-overflow.patch
Patch10: audiofile-0.3.6-CVE-2022-24599.patch

%description
The Audio File library is an implementation of the Audio File Library
from SGI, which provides an API for accessing audio file formats like
AIFF/AIFF-C, WAVE, and NeXT/Sun .snd/.au files. This library is used
by the EsounD daemon.

Install audiofile if you are installing EsounD or you need an API for
any of the sound file formats it can handle.

%package devel
Summary: Development files for Audio File applications
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
The audiofile-devel package contains libraries, include files, and
other resources you can use to develop Audio File applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1 -b .CVE-2015-7747
%patch -P 1 -p1 -b .left-shift-neg
%patch -P 2 -p1 -b .narrowing-conversion
%patch -P 3 -p1 -b .pull42
%patch -P 4 -p1 -b .pull43
%patch -P 5 -p1 -b .pull44
%patch -P 6 -p1 -b .CVE-2018-17095
%patch -P 7 -p1 -b .CVE-2018-13440
%patch -P 8 -p1 -b .CVE-2018-13440
%patch -P 9 -p1 -b .integer-overflow
%patch -P 10 -p1 -b .CVE-2022-24599

%build
%configure --disable-rpath
%make_build

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

chrpath --delete $RPM_BUILD_ROOT%{_bindir}/sfconvert
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/sfinfo

#%check
#%if %{make_check}
#make check
#%endif

%ldconfig_scriptlets

%files
%license COPYING COPYING.GPL
%doc ACKNOWLEDGEMENTS AUTHORS NEWS NOTES README TODO
%{_bindir}/sfconvert
%{_bindir}/sfinfo
%{_libdir}/lib*.so.1*
%{_mandir}/man1/*

%files devel
%doc ChangeLog docs/*.3.txt
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_mandir}/man3/*

%changelog
%autochangelog
