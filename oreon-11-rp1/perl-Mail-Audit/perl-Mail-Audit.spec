%global source0_hash 41a42dc3fbead585c732de5e35b46c3d3511358458bc31520abac1946c99d2e4
Name:           perl-Mail-Audit
Version:        2.228
Release:        1%{?dist}
Summary:        Library for creating easy mail filters
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Mail-Audit
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Mail-Audit-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Tempdir)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(MIME::Parser)
BuildRequires:  perl(Mail::Internet)
BuildRequires:  perl(Mail::Mailer)
BuildRequires:  perl(Mail::POP3Client)
BuildRequires:  perl(Mail::Send)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Mail::Audit was inspired by Tom Christiansen's audit_mail and deliverlib
programs. It allows a piece of email to be logged, examined, accepted into
a mailbox, filtered, resent elsewhere, rejected, replied to, and so on. It's
designed to allow you to easily create filter programs to stick in a .forward
file or similar.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Mail-Audit-%{version}
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
