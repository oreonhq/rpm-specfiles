%global source0_hash c1ff3b0b14a86d8146808bdc59d8d207f220120309ccf16decfb0dc236c144b0

Name:           perl-Text-vCard
Version:        3.09
Release:        28%{?dist}
Summary:        Package to edit and create a single vCard (RFC 2426)
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-vCard
Source0:        https://cpan.metacpan.org/authors/id/L/LL/LLAP/Text-vCard-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Directory::Scratch)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64) >= 3.07
BuildRequires:  perl(MIME::QuotedPrint) >= 3.07
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Text::vFile::asData) >= 0.07
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Unicode::LineBreak)
BuildRequires:  perl(URI)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Text::vFile::asData\\)$

%description
vCards are electronic business cards used by various message user
agents (MUAs) and defined in RFC 2426.  They are a simple and
extensible representation for common contact information such as
name, company, telephone, fax, address, email, etc. and some
less common information such as IM or Googletalk handles.

This package provides an interface for manipulating vCards.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-vCard-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
