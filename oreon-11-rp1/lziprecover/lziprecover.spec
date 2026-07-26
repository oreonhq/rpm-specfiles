%global source0_hash a867b41e4caab6906910d95065f32907a3673f52fd56bc912ab26f8acc18753d

Name:           lziprecover
Version:        1.26
Release:        1%{?dist}
Summary:        Data recovery tool and decompressor for files in the lzip compressed format

License:        GPL-3.0-or-later
URL:            https://www.nongnu.org/lzip/lziprecover.html
Source0:        https://download-mirror.savannah.gnu.org/releases/lzip/lziprecover/lziprecover-%{version}.tar.lz
Source1:        https://download-mirror.savannah.gnu.org/releases/lzip/lziprecover/lziprecover-%{version}.tar.lz.sig
BuildRequires: make
BuildRequires:  lzip gcc-c++

%description
Lziprecover is a data recovery tool and decompressor for files in the lzip 
compressed data format (.lz) able to repair slightly damaged files, recover 
badly damaged files from two or more copies, extract undamaged members 
from multi-member files, decompress files and test integrity of files.

Lziprecover is able to recover or decompress files produced by any of the 
compressors in the lzip family; lzip, plzip, minilzip/lzlib, clzip and 
pdlzip. This recovery capability contributes to make the lzip format one 
of the best options for long-term data archiving. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# file needs to be copied, because it is used in "make check"
cp -a COPYING{,.txt}
# convert CRLF to LF
sed -i 's/\r//' COPYING.txt 

%build
%configure CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" CPPFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make install install-man DESTDIR=$RPM_BUILD_ROOT

# if install-info is present, this is created by upstream's makefile
rm -Rf $RPM_BUILD_ROOT%{_infodir}/dir

%check
make check

%files
# TODO is currently empty
%license COPYING.txt
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/lziprecover
%{_infodir}/lziprecover.info*
%{_mandir}/man1/lziprecover.1*

%changelog
%autochangelog
