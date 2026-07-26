%global source0_hash be6a957f04a2feba9b305536b132deceba1f455db295b221a63e75567fadbcfc

Name:           perl-AnyData
Version:        0.12
Release:        32%{?dist}
Summary:        Easy access to data in many formats
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AnyData
Source0:        https://cpan.metacpan.org/authors/id/J/JZ/JZUCKER/AnyData-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:	perl(CGI)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
# Not tested:   perl(HTML::TableExtract)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::File)
BuildRequires:	perl(Test::More)
# Not tested:   perl(XML::Twig)
Requires:  perl(CGI)
Requires:  perl(constant)
Requires:  perl(Data::Dumper)
Requires:  perl(HTML::TableExtract)
Requires:  perl(Exporter)
Requires:  perl(IO::File)
Requires:  perl(XML::Twig)

%description
The AnyData modules provide simple and uniform access to data from
many sources -- perl arrays, local files, remote files retrievable via
http or ftp -- and in many formats including flat files (CSV, Fixed
Length, Tab Delimited, etc), standard format files (Web Logs,
Passwd files, etc.),  structured files (XML, HTML Tables) and binary 
files with parseable headers (mp3s, jpgs, pngs, etc).  

There are two separate modules, each providing a different interface:
AnyData.pm provides a simple tied hash interface and DBD::AnyData
provides a DBI/SQL interface.  You can use either or both depending on
your needs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AnyData-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/AnyData.pm
%{perl_vendorlib}/AnyData/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
