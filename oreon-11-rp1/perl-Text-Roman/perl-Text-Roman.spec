%global source0_hash cb4a08a3b151802ffb2fce3258a416542ab81db0f739ee474a9583ffb73e046a

Name:           perl-Text-Roman
Version:        3.5
Release:        32%{?dist}
Summary:        Conversion between Roman algorisms and Arabic numerals
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Roman
Source0:        https://cpan.metacpan.org/authors/id/S/SY/SYP/Text-Roman-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(warnings)
Requires:       perl(Carp)
Requires:       perl(Exporter)

Provides:       perl(Text::Roman)
%description
This package supports both conventional Roman algorisms (which range from 1
to 3999) and Milhar Romans, a variation which uses a bar across the
algorism to indicate multiplication by 1000.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Text-Roman-%{version}
chmod a-x eg/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README eg
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
