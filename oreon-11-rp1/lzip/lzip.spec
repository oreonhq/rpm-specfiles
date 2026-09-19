%global source0_hash 641cf30961525cbe3b340cc883436c8854e9f5032f459f444de4782b621e6572

Name:           lzip
Version:        1.26
Release:        1%{?dist}
Summary:        LZMA compressor with integrity checking

License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/lzip/lzip.html
Source0:        http://download-mirror.savannah.gnu.org/releases/lzip/lzip-%{version}.tar.gz
Source1:        http://download-mirror.savannah.gnu.org/releases/lzip/lzip-%{version}.tar.gz.sig
BuildRequires: make
BuildRequires:  gcc-c++

%description
Lzip compresses data using LZMA (Lempel-Ziv-Markov chain-Algorithm). It
supports integrity checking using CRC (Cyclic Redundancy Check). To archive
multiple files, tar can be used with lzip. Please note, that the lzip file
format (.lz) is not compatible with the lzma file format (.lzma).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# file needs to be copied, because it is used in "make check"
cp -a COPYING{,.txt}
# convert CRLF to LF
sed -i 's/\r//' COPYING.txt 

%build
%configure CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}"
%make_build

%install
%make_install install-man

# if install-info is present, this is created by upstream's makefile
rm -Rf $RPM_BUILD_ROOT%{_infodir}/dir

%check
make check

%files
%license COPYING.txt
# TODO is currently empty
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/lzip
%{_infodir}/lzip.info*
%{_mandir}/man1/lzip.1*

%changelog
%autochangelog
