%global source0_hash 8c12f68b5974cafc99d74942abefc8597193035aafd2763128e6aaafca4b7ed6

Name:           perl-Email-Abstract
Version:        3.010
Release:        7%{?dist}
Summary:        Unified interface to mail representations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Abstract
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-Abstract-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Email::MIME)
BuildRequires:  perl(Email::Simple) >= 1.998
BuildRequires:  perl(Mail::Internet)
BuildRequires:  perl(Mail::Message)
BuildRequires:  perl(MIME::Entity) >= 5.508
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(Module::Pluggable) >= 1.5
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.96
# Dependencies
Requires:       perl(Email::MIME)
Requires:       perl(Mail::Internet)
Requires:       perl(Mail::Message)
Requires:       perl(MIME::Entity) >= 5.501
Requires:       perl(MIME::Parser)

%description
"Email::Abstract" provides module writers with the ability to write
representation-independent mail handling code. For instance, in the
cases of "Mail::Thread" or "Mail::ListDetector", a key part of the code
involves reading the headers from a mail object. Where previously one
would either have to specify the mail class required, or to build a new
object from scratch, "Email::Abstract" can be used to perform certain
simple operations on an object regardless of its underlying
representation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Email-Abstract-%{version}

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
%doc Changes README
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::Abstract.3*
%{_mandir}/man3/Email::Abstract::EmailMIME.3*
%{_mandir}/man3/Email::Abstract::EmailSimple.3*
%{_mandir}/man3/Email::Abstract::MIMEEntity.3*
%{_mandir}/man3/Email::Abstract::MailInternet.3*
%{_mandir}/man3/Email::Abstract::MailMessage.3*
%{_mandir}/man3/Email::Abstract::Plugin.3*

%changelog
%autochangelog
