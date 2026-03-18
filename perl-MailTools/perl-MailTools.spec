Summary:	Various ancient mail-related perl modules
Name:		perl-MailTools
Version:	2.22
Release:	4%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/MailTools
Source0:	https://cpan.metacpan.org/authors/id/M/MA/MARKOV/MailTools-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(base)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Config)
BuildRequires:	perl(Date::Format)
BuildRequires:	perl(Date::Parse)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(Net::Domain) >= 1.05
BuildRequires:	perl(Net::NNTP)
BuildRequires:	perl(Net::SMTP) >= 1.28
BuildRequires:	perl(Net::SMTP::SSL)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(strict)
# Test Suite
BuildRequires:	perl(Test::More)
BuildRequires:	perl(warnings)
# Extra Tests
BuildRequires:	perl(Test::Pod)
# Dependencies
Requires:	perl(Net::Domain) >= 1.05
Requires:	perl(Net::NNTP)

%description
MailTools is a set of ancient Perl modules related to mail applications.

%prep
%setup -q -n MailTools-%{version}

# Set up example scripts
cd examples
for file in *.PL; do
	perl $file
done
chmod -c -x *_demo
# Remove example-generation scripts, no longer needed
rm *.PL
cd -
sed -i -e '/^examples\/.*\.PL/d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test
make test TEST_FILES="xt/*.t"

%files
%doc ChangeLog README* examples/
%dir %{perl_vendorlib}/Mail/
%dir %{perl_vendorlib}/Mail/Field/
%dir %{perl_vendorlib}/Mail/Mailer/
%doc %{perl_vendorlib}/Mail/Address.pod
%doc %{perl_vendorlib}/Mail/Cap.pod
%doc %{perl_vendorlib}/Mail/Field.pod
%doc %{perl_vendorlib}/Mail/Field/AddrList.pod
%doc %{perl_vendorlib}/Mail/Field/Date.pod
%doc %{perl_vendorlib}/Mail/Field/Generic.pod
%doc %{perl_vendorlib}/Mail/Filter.pod
%doc %{perl_vendorlib}/Mail/Header.pod
%doc %{perl_vendorlib}/Mail/Internet.pod
%doc %{perl_vendorlib}/Mail/Mailer.pod
%doc %{perl_vendorlib}/Mail/Send.pod
%doc %{perl_vendorlib}/Mail/Util.pod
%doc %{perl_vendorlib}/MailTools.pod
%{perl_vendorlib}/Mail/Address.pm
%{perl_vendorlib}/Mail/Cap.pm
%{perl_vendorlib}/Mail/Filter.pm
%{perl_vendorlib}/Mail/Header.pm
%{perl_vendorlib}/Mail/Internet.pm
%{perl_vendorlib}/Mail/Field.pm
%{perl_vendorlib}/Mail/Mailer.pm
%{perl_vendorlib}/Mail/Send.pm
%{perl_vendorlib}/Mail/Util.pm
%{perl_vendorlib}/Mail/Field/AddrList.pm
%{perl_vendorlib}/Mail/Field/Date.pm
%{perl_vendorlib}/Mail/Field/Generic.pm
%{perl_vendorlib}/Mail/Mailer/qmail.pm
%{perl_vendorlib}/Mail/Mailer/rfc822.pm
%{perl_vendorlib}/Mail/Mailer/sendmail.pm
%{perl_vendorlib}/Mail/Mailer/smtp.pm
%{perl_vendorlib}/Mail/Mailer/smtps.pm
%{perl_vendorlib}/Mail/Mailer/testfile.pm
%{perl_vendorlib}/MailTools.pm
%{_mandir}/man3/Mail::Address.3*
%{_mandir}/man3/Mail::Cap.3*
%{_mandir}/man3/Mail::Field.3*
%{_mandir}/man3/Mail::Field::AddrList.3*
%{_mandir}/man3/Mail::Field::Date.3*
%{_mandir}/man3/Mail::Field::Generic.3*
%{_mandir}/man3/Mail::Filter.3*
%{_mandir}/man3/Mail::Header.3*
%{_mandir}/man3/Mail::Internet.3*
%{_mandir}/man3/Mail::Mailer.3*
%{_mandir}/man3/Mail::Send.3*
%{_mandir}/man3/Mail::Util.3*
%{_mandir}/man3/MailTools.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.22-4
- Prepare for Oreon 11 (RP1)
