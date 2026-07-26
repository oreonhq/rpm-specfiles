%global source0_hash 11200cc6b0b7ba16884a72dccb58ef694f7aa26cd2b2041e555580f064d2d9e9

Summary: An Optical Character Recognition program
Name: ocrad
Version: 0.29
Release: 6%{?dist}
License: GPL-3.0-or-later
Source: ftp://ftp.gnu.org/gnu/ocrad/%{name}-%{version}.tar.lz
Patch0: ocrad-0.25-nostatic.patch
URL: http://www.gnu.org/software/ocrad/ocrad.html
BuildRequires: make
BuildRequires: lzip gcc-c++
BuildRequires: libpng-devel

%description
GNU Ocrad is an OCR (Optical Character Recognition) program based on a feature
extraction method. It reads images in pbm (bitmap), pgm (greyscale) or ppm
(color) formats and produces text in byte (8-bit) or UTF-8 formats.
Also includes a layout analyser able to separate the columns or blocks of text
normally found on printed pages.
Ocrad can be used as a stand-alone console application, or as a backend to
other programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1 -b .nostatic

%build
%configure
make CXXFLAGS="$RPM_OPT_FLAGS" %{?_smp_flags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
install -p doc/ocrad.1 ${RPM_BUILD_ROOT}%{_mandir}/man1
rm -f ${RPM_BUILD_ROOT}%{_infodir}/dir

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/ocrad
%attr(0644,root,root) %{_mandir}/man1/*
%attr(0644,root,root) %{_infodir}/ocrad.info.gz

%changelog
%autochangelog
