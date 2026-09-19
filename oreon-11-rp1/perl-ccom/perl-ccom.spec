%global source0_hash 05f04c7f0d4a4294d3af3df8ee07fdfe397ae1b30ac36d01ec1a381399e0830b

# Filter the Perl extension module
%{?perl_default_filter}

Summary:        Perl module for context-sensitive phonetic string replacement
Name:           perl-ccom
Version:        1.4.1
Release:        53%{?dist}
License:        LGPL-2.0-or-later
URL:            https://www.heise.de/ct/ftp/99/25/252/
Source0:        https://ftp.heise.de/ct/listings/phonet.tgz
Patch0:         perl-ccom-1.4.1-format-security.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
A perl module for context-sensitive phonetic string replacement to modify
strings according to predefined replacement rules in such a way that words
with the same pronunciation (e.g. "tail" and "tale") are converted to the
same string. This can, for example, be used to implement error-tolerant
search routines in address databases. It contains phonetic rules for German
only, but the software has been prepared for multi-language support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}
%patch -P0 -p0 -b .format-security

# Clean the strange packaging first
mv -f ccom*/* .
chmod 644 *.xs ccomlib/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

# Change man page encoding into UTF-8
iconv -f latin1 -t utf-8 -o blib/man3/ccom.3pm.utf8 blib/man3/ccom.3pm
touch -c -r blib/man3/ccom.3pm blib/man3/ccom.3pm.utf8
mv -f blib/man3/ccom.3pm.utf8 blib/man3/ccom.3pm

%install
%make_install
%if 0%{?rhel} && 0%{?rhel} <= 7
find $RPM_BUILD_ROOT \( -name perllocal.pod -o -name .packlist \) -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -exec rm -f {} ';'
%endif
chmod -R u+w $RPM_BUILD_ROOT/*

# Fix incorrect permissions
chmod 644 Changes readme_perl.txt ccom_test.pl

# Fix incorrect end-of-line encoding
sed -e 's/\r//' -i copying.lib -i readme_perl.txt

# Fix incorrect interpreter path
sed -e 's@#! /opt/perl5/bin/perl@#!%{_bindir}/perl@' -i ccom_test.pl

# Remove test/example from regulars
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/ccom_test.pl

%files
%license copying.lib
%doc Changes readme_perl.txt ccom_test.pl
%{_mandir}/man3/*.3pm*
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/auto/ccom
%{perl_vendorarch}/*.pm

%changelog
%autochangelog
