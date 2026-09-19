%global source0_hash bc27d65807799945615ef4b4d55189f6bda5fc50993d401acfd9fb91277cfa19

Name:   perl-MIME-Lite-TT-HTML
Version:        0.04
Release:        33%{?dist}
Summary:        MIME::Lite::TT::HTML - Create html mail with MIME::Lite and TT

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MIME-Lite-TT-HTML-%{version}
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHUNZI/MIME-Lite-TT-HTML-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Carp)
BuildRequires: perl(DateTime::Format::Mail)
BuildRequires: perl(Encode)
BuildRequires: perl(HTML::FormatText::WithLinks)
BuildRequires: perl(MIME::Lite)
BuildRequires: perl(MIME::Words)
BuildRequires: perl(Module::Build)
BuildRequires: perl(strict)
BuildRequires: perl(Template)
BuildRequires: perl(Test::More)

%description
This module provide easy interface to make MIME::Lite object with html
formatted mail.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MIME-Lite-TT-HTML-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README LICENSE
%{perl_vendorlib}/MIME/Lite/TT/*
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
