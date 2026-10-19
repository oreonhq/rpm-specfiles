%global source0_hash 60a33da3b49fab7994e8a39e649b664c3e9383da29434e9ea256782c2ea1ef80
Name:           perl-Mail-Sender
Version:        0.900003
Epoch:          1
Release:        1%{?dist}
Summary:        Module for sending mails with attachments through an SMTP server
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-Sender
Source0:        https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/Mail-Sender-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Mail::Sender)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
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
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
find $RPM_BUILD_ROOT -type f -name Win32.pm -delete
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
