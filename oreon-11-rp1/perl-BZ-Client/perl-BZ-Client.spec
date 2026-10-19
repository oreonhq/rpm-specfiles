%global source0_hash 1d4f4306f55664ad11d16cc34ff50989b10fe4542a7ac55c643ff7a188ba4842
Name:           perl-BZ-Client
Version:        4.4004
Release:        1%{?dist}
Summary:        A client for the Bugzilla web services API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/BZ-Client
Source0:        https://cpan.metacpan.org/authors/id/D/DJ/DJZORT/BZ-Client-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Clone)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::CookieJar)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Text::Password::Pronounceable)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Writer)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module provides an interface to the Bugzilla web services API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n BZ-Client-%{version}
chmod 644 Changes README LICENSE

%build

%{__perl} Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
