%global source2_hash e7a93b009565cfce55919a381437ac4db883e9da2126fa28b91d12732bc53d96
%global source0_hash 7b3e555514060b92290d154f53655c5eb0fa62b16eb04c03434ff72d1a66a0d8
%global source1_hash 4c93ea9c1f636451729a840978f1667a53886af37ba854fdcce109721c63d43e
%global unicodedir %{_datadir}/unicode
%global ucddir %{unicodedir}/ucd
Name:           unicode-ucd
Version:        18.0.0
Release:        1%{?dist}
Summary:        Unicode Character Database
License:        Unicode-3.0
URL:            http://www.unicode.org/ucd/
Source0:        https://www.unicode.org/Public/%{version}/ucd/UCD.zip
Source1:        https://www.unicode.org/Public/%{version}/ucd/Unihan.zip
Source2:        https://www.unicode.org/license.txt
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description
The Unicode Character Database (UCD) consists of a number of data files listing
Unicode character properties and related data. It also includes data files
containing test data for conformance to several important Unicode algorithms.

%package unihan
Summary:        Unicode Han Database
Requires:       %{name} = %{version}-%{release}
%description unihan
This package contains Unihan.zip which contains the data files for the Unified
Han database of Hanzi/Kanji/Hanja Chinese characters.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -c

grep -q "%{version}" ReadMe.txt || (echo "zip file seems not %{version}" ; exit 1)

%build

%{nil}
%install
mkdir -p %{buildroot}%{ucddir}
cp -ar . %{buildroot}%{ucddir}
cp -p %{SOURCE1} %{buildroot}%{ucddir}
cp %{SOURCE2} .
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n unicode-ucd-unihan -f %{oreon_filedir}/unicode-ucd-unihan.list

%changelog

%autochangelog
