%global source0_hash b3c9c2dde0085c49c34fa6bf6aef9e615b95a5bf578b467c8fef7d1ac5320a1f
Name:           perl-Test-HTTP-LocalServer
Version:        0.76
Release:        1%{?dist}
Summary:        Spawn a local HTTP server for testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-HTTP-LocalServer/
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/Test-HTTP-LocalServer-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(POSIX)
Requires:       perl(CGI)
Requires:       perl(Getopt::Long)
Requires:       perl(HTTP::Daemon)
Requires:       perl(HTTP::Request::AsCGI)
Requires:       perl(Socket)
Requires:       perl(Time::HiRes)
Requires:       perl(URI)
Requires:       perl(strict)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Request::AsCGI)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Markdown)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements a tiny web server suitable for running "live" tests
of HTTP clients against it. It also takes care of cleaning %%ENV from
settings that influence the use of a local proxy etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-HTTP-LocalServer-%{version}
perl -pi -e 's/\r//' lib/Test/HTTP/cookie-server

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
