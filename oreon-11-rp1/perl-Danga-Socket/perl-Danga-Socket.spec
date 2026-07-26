%global source0_hash 953c3f787ef1a11d956b28084246ffe3fc0f80da8fcb14f48477025773dc8b74

Name:           perl-Danga-Socket
Version:        1.62
Release:        18%{?dist}
Summary:        Event loop and event-driven async socket base class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Danga-Socket
Source0:        https://cpan.metacpan.org/modules/by-module/Danga/Danga-Socket-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
# XXX: BuildRequires:  perl(BSD::Resource)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(fields)
BuildRequires:  perl(IO::Handle)
# XXX: BuildRequires:  perl(IO::KQueue)
# XXX: BuildRequires:  perl(IO::Poll)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Syscall)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(Test::More)

%description
This is an abstract base class for objects backed by a socket which
provides the basic framework for event-driven asynchronous IO, designed to
be fast. Danga::Socket is both a base class for objects, and an event loop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Danga-Socket-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES examples
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
