%global source0_hash 78e027d501cc5e6a249b913773b629e5d14cf89a7c077b1894faac1f7b5e4072

Name:           perl-WWW-Twilio-TwiML
Version:        1.05
Release:        30%{?dist}
Summary:        Light and fast TwiML generator
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Twilio-TwiML

Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCOTTW/WWW-Twilio-TwiML-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Testing
BuildRequires:  perl(Test::More)

%description
WWW::Twilio::TwiML creates Twilio-compatible TwiML documents. Documents can
be built by creating and nesting one element at a time or by chaining
objects. Elements can contain attributes, text content, or other elements.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Twilio-TwiML-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
