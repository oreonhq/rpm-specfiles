%global source0_hash 21259647a6609289341efddd6850a24e1c05c418330f8f5644034ce2f88cc593

Name:           perl-Net-IRC
Version:        0.79
Release:        41%{?dist}
Summary:        Perl interface to the Internet Relay Chat protocol
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-IRC
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APEIRON/Net-IRC-%{version}.tar.gz
# Avoid interactive build
Patch0:         Net-IRC-0.79-confirm.patch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::INET)
# XXX: BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test)
Requires:       perl(IO::Socket::SSL)
Requires:       perl(Time::HiRes)

%description
Perl implementation of the IRC protocol (RFC 1459).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn Net-IRC-%{version}
%patch -P0 -p1
chmod -x irctest

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README irctest
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
