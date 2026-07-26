%global source0_hash fad783557b61e858de0708953af5b54185d235a891edafce86f7083b0a3c21c7

Name:           perl-HTML-FormFu-Element-reCAPTCHA
Version:        1.00
Release:        34%{?dist}
Summary:        reCAPTCHA component for HTML::FormFu frame work
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-FormFu-Element-reCAPTCHA
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFRANKS/HTML-FormFu-Element-reCAPTCHA-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Captcha::reCAPTCHA) >= 0.93
BuildRequires:  perl(Clone) >= 0.31
BuildRequires:  perl(HTML::FormFu::Constraint)
BuildRequires:  perl(HTML::FormFu::Element::Multi)
BuildRequires:  perl(HTML::FormFu::Util) >= 1.00
BuildRequires:  perl(Moose) >= 1.00
BuildRequires:  perl(MooseX::Attribute::Chained) >= 1.0.1
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(HTML::FormFu) >= 1.00
BuildRequires:  perl(Test::More)
Requires:       perl(Captcha::reCAPTCHA) >= 0.93
Requires:       perl(Clone) >= 0.31
Requires:       perl(HTML::FormFu::Constraint)
Requires:       perl(HTML::FormFu::Element::Multi)
Requires:       perl(HTML::FormFu::Util) >= 1.00
Requires:       perl(Moose) >= 1.00
Requires:       perl(MooseX::Attribute::Chained) >= 1.0.1

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Captcha::reCAPTCHA|Clone|HTML::FormFu::Util|Moose|MooseX::Attribute::Chained)\\)$

%description
A wrapper around Captcha::reCAPTCHA. The reCAPTCHA fields aren't added to
the form as "real" FormFu fields - so the values are never available via
params method, etc. You can check that the reCAPTCHA verified correctly, by
the usual methods: "submitted_and_valid" in HTML::FormFu or "has_errors" in
HTML::FormFu.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-FormFu-Element-reCAPTCHA-%{version}

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
%doc Changes LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
