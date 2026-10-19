%global source0_hash 4cd7bb61b51d41192d1498c1051aa6a4ccd75aeb09b71d2ec706a7084a4a9303
Name:           perl-mime-construct
Version:        1.11
Release:        1%{?dist}
Summary:        Construct/send MIME messages from the command line
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/mime-construct-%{version}
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROSCH/mime-construct-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Proc::WaitStat)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
mime-construct constructs and (by default) mails MIME messages.  
It is entirely driven from the command line, it is designed to be used 
by other programs, or people who act like programs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mime-construct-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
