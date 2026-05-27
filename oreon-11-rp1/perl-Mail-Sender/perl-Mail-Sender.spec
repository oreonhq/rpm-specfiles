%global source0_hash 4413eb49f520a8318151811ccb05a8d542973aada20aa503ad32f9ffc98a39bf

Name:           perl-Mail-Sender
Version:        0.903
# I really wish CPAN maintainers would stop fscking around with versions.
# we went from 0.900003 to 0.901
Epoch:          1
Release:        28%{?dist}
Summary:        Module for sending mails with attachments through an SMTP server

# There is also a clause which says that it may not be used for SPAM.
# However, since spamming is illegal in the US, this isn't really a use restriction.
# Instead, its a friendly reminder of the law, so we won't list it here.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Sender
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/Mail-Sender-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Try::Tiny) >= 0.24
BuildRequires:  perl(warnings)

%description
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Mail-Sender-%{version}
%{__perl} -pi -e 's/\r\n/\n/' README


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags} < /dev/null


%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

# Remove the Win32 module in order to avoid requiring perl(Win32API::Registry)
find $RPM_BUILD_ROOT -type f -name Win32.pm -delete


%check
make test


%files
# License: perl + spam exception.
# See the main POD page for the copyright information.
# For the Artistic and GPL license text(s), see the perl package.
%doc Changes README
%{perl_vendorlib}/Mail/
%{_mandir}/man3/*.3pm*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.903-28
- Prepare for Oreon 11 (RP1)
