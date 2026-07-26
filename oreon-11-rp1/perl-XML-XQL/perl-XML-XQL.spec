%global source0_hash e618d657530d22ff5c807b794be74ade0524faa8f21e95ef2d674d971f8c6458

Name:           perl-XML-XQL
Version:        0.68
Release:        55%{?dist}
Summary:        Perl module for querying XML tree structures with XQL
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-XQL
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJMATHER/XML-XQL-%{version}.tar.gz
Patch0:         %{name}-tput-147465.patch
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Manip) >= 5.33
BuildRequires:  perl(fields)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(overload)
BuildRequires:  perl(Parse::Yapp::Driver)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(XML::DOM) >= 1.29
BuildRequires:  perl(XML::Parser) >= 2.30
BuildRequires:  perl(XML::RegExp)
# Tests only
# -
Requires:       perl(Date::Manip) >= 5.33
Requires:       perl(POSIX)
Requires:       perl(XML::DOM)
Requires:       perl(XML::Parser) >= 2.30

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Date::Manip\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(XML::\(DOM::.+\|XQL)\\)\\s*$

%description
This is a Perl extension that allows you to perform XQL queries on XML
object trees. Currently only the XML::DOM module is supported, but
other implementations, like XML::Grove, may soon follow.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-XQL-%{version}
%patch -P0 -p0

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README samples
%{_bindir}/xql.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
