%global source0_hash cd98c8104b70d7672bfa26b4513b78adf2b4b9220e586aa8beb1a508500365a6

Name:           perl-XML-LibXML-Simple
Version:        1.01
Release:        19%{?dist}
Summary:        Read XML strings or files
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-LibXML-Simple
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/XML-LibXML-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::More) >= 0.54
BuildRequires:  perl(XML::LibXML) >= 1.64
Requires:       perl(XML::LibXML) >= 1.64

# drop unversioned Requires on XML::LibXML
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(XML::LibXML\\)$

Provides:       perl(XML::LibXML::Simple)
%description
This Perl module reads XML from strings or files.  It is a blunt rewrite
of XML::Simple (by Grant McLean) to use the XML::LibXML parser for XML
structures, where the original uses plain Perl or SAX parsers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n XML-LibXML-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
