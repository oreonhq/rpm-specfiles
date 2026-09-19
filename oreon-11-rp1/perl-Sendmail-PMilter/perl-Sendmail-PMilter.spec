%global source0_hash bb5265360d3c00b312e5ede02484ec2200a5252e48bebb4978420711d8d49b66

Summary:	Perl binding of Sendmail Milter protocol
Name:		perl-Sendmail-PMilter
Version:	1.27
Release:	5%{?dist}
License:	BSD-3-Clause
URL:		https://metacpan.org/release/Sendmail-PMilter
Source0:	https://cpan.metacpan.org/authors/id/G/GW/GWHAYWOOD/Sendmail-PMilter-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket::INET)
BuildRequires:	perl(IO::Socket::IP)
BuildRequires:	perl(IO::Socket::UNIX)
BuildRequires:	perl(parent)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Socket)
BuildRequires:	perl(Socket6)
BuildRequires:	perl(strict)
BuildRequires:	perl(Symbol)
BuildRequires:	perl(Thread::Semaphore)
BuildRequires:	perl(threads)
BuildRequires:	perl(threads::shared)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(UNIVERSAL)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test::More)
# Dependencies
Requires:	perl(IO::Socket::INET)
Requires:	perl(IO::Socket::IP)
Requires:	perl(IO::Socket::UNIX)
Requires:	perl(Socket6)
Requires:	perl(Thread::Semaphore)
Requires:	perl(threads)
Requires:	perl(threads::shared)

%description
Sendmail::PMilter is a mail filtering API implementing the Sendmail milter
protocol in pure Perl. This allows Sendmail servers (and perhaps other MTAs
implementing milter) to filter and modify mail in transit during the SMTP
connection, all in Perl.

It should be noted that PMilter 0.90 and later is NOT compatible with
scripts written for PMilter 0.5 and earlier.  The API has been reworked
significantly, and the enhanced APIs and rule logic provided by PMilter
0.5 and earlier has been factored out for inclusion in a separate package
called Mail::Milter.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sendmail-PMilter-%{version}

# Fix interpreters in examples and turn off exec bits to avoid extra deps
sed -i -e 's@/usr/local/bin/perl@/usr/bin/perl@' examples/*.pl
chmod -c -x examples/*.pl

%build
# Using "echo" to bypass the interactive 'yes/no' question in Makefile.PL
echo yes | perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
# Note: COPYRIGHT file is identical to LICENSE file
%license LICENSE
%doc ABOUT ACKNOWLEDGEMENTS Changes CONTRIBUTING README README.%{version} TODO
%doc examples/
%{perl_vendorlib}/Sendmail/
%{_mandir}/man3/Sendmail::PMilter.3*
%{_mandir}/man3/Sendmail::PMilter::Context.3*

%changelog
%autochangelog
