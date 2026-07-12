%global source0_hash d537cb09ce5aab3f447a6bb4415e46cc06efe01611cd56289b5582bdb46221e8

Name:           perl-FCGI-Client 
Summary:        Client library for the fastcgi protocol 
Version:        0.09
Release:        22%{?dist}
# lib/FCGI/Client.pm -> GPL+ or Artistic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl 
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/FCGI-Client-%{version}.tar.gz 
URL:            https://metacpan.org/release/FCGI-Client
BuildArch:      noarch

# build requirements
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(strict)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(autodie)

%{?perl_default_filter}

Provides:       perl(FCGI::Client)
%description
FCGI::Client is a client library for the fastcgi protocol.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n FCGI-Client-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README.md scripts
%{perl_vendorlib}/FCGI*
%{_mandir}/man3/FCGI*.3*

%changelog
%autochangelog
