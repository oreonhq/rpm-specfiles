%global source0_hash c1ff3b0b14a86d8146808bdc59d8d207f220120309ccf16decfb0dc236c144b0
Name:           perl-Text-vCard
Version:        3.09
Release:        1%{?dist}
Summary:        Package to edit and create a single vCard (RFC 2426)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-vCard
Source0:        https://cpan.metacpan.org/authors/id/L/LL/LLAP/Text-vCard-%{version}.tar.gz
BuildArch:      noarch
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Text::vFile::asData\\)$
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Directory::Scratch)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Text::vFile::asData)
BuildRequires:  perl(URI)
BuildRequires:  perl(Unicode::LineBreak)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
