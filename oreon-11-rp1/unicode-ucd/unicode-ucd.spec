# for other future directories from http://www.unicode.org/Public
%global unicodedir %{_datadir}/unicode
%global ucddir %{unicodedir}/ucd

Name:           unicode-ucd
Version:        17.0.0
Release:        2%{?dist}
Summary:        Unicode Character Database

# http://www.unicode.org/terms_of_use.html in ReadMe.txt redirects to:
# http://www.unicode.org/copyright.html
# which links to https://www.unicode.org/license.txt
# https://github.com/spdx/license-list-XML/issues/2105
License:        Unicode-3.0
URL:            http://www.unicode.org/ucd/
# update with "fbrnch update-sources -f"
Source0:        https://www.unicode.org/Public/%{version}/ucd/UCD.zip
Source1:        https://www.unicode.org/Public/%{version}/ucd/Unihan.zip
Source2:        https://www.unicode.org/license.txt
BuildArch:      noarch

%description
The Unicode Character Database (UCD) consists of a number of data files listing
Unicode character properties and related data. It also includes data files
containing test data for conformance to several important Unicode algorithms.


%package unihan
Summary:        Unicode Han Database
# for the license and dirs
Requires:       %{name} = %{version}-%{release}

%description unihan
This package contains Unihan.zip which contains the data files for the Unified
Han database of Hanzi/Kanji/Hanja Chinese characters.


%prep
%setup -q -c

grep -q "%{version}" ReadMe.txt || (echo "zip file seems not %{version}" ; exit 1)


%build
%{nil}


%install
mkdir -p %{buildroot}%{ucddir}
cp -ar . %{buildroot}%{ucddir}
cp -p %{SOURCE1} %{buildroot}%{ucddir}
cp %{SOURCE2} .


%files
%license license.txt
%dir %{unicodedir}
%{ucddir}
%exclude %{ucddir}/Unihan.zip

%files unihan
%{ucddir}/Unihan.zip


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 17.0.0-2
- Prepare for Oreon 11 (RP1)
