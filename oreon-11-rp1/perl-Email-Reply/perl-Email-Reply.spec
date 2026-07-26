%global source0_hash ba4fd80ac5017d6d132e0358c786b0ecd1c7adcbeee5c19fb3da2964791a56f0

Name:           perl-Email-Reply
Version:        1.204
Release:        30%{?dist}
Summary:        Reply to an email message
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Reply
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-Reply-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
# Module Runtime
BuildRequires:  perl(Email::Abstract) >= 2.01
BuildRequires:  perl(Email::Address) >= 1.80
BuildRequires:  perl(Email::MIME) >= 1.82
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Email::MIME::Modifier)
BuildRequires:  perl(Email::Simple)
BuildRequires:  perl(Email::Simple::Creator)
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
# (none)

%description
This package provides a simple way to reply to email messages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Reply-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::Reply.3*

%changelog
%autochangelog
