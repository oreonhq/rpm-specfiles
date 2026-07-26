%global source0_hash 844c01e78ba4bfb89c0702995a86f488de7c29b40a75e7af0e4f39d55624dba0

Name:           perl-Text-Kakasi
Version:        2.04
Release:        63%{?dist}
Summary:        Kakasi library module for perl

License:        GPL-2.0-or-later
Url:            https://metacpan.org/release/Text-Kakasi
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/Text-Kakasi-2.04.tar.gz
Patch:          Text-Kakasi-1.04-perl580.diff

BuildRequires: make
BuildRequires:  perl-interpreter >= 2:5.8.0
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  kakasi-devel >= 2.3.1, kakasi-dict
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  gcc
Requires:       kakasi >= 2.3.1

%description
This module provides libkakasi interface for perl. libkakasi is a part
of KAKASI.  KAKASI is the language processing filter to convert Kanji
characters to Hiragana, Katakana or Romaji and may be helpful to read
Japanese documents.
More information about KAKASI is available at <http://kakasi.namazu.org/>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Text-Kakasi-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

file=$RPM_BUILD_ROOT%{_mandir}/man3/Text::Kakasi.3pm
iconv -f euc-jp -t utf-8 < "$file" > "${file}_"
mv -f "${file}_" "$file"

%check
make test

%files
%license COPYING
%{perl_vendorarch}/Text/
%{perl_vendorarch}/auto/Text/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
