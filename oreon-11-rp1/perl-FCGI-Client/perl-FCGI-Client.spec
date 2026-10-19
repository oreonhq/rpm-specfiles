%global source0_hash d537cb09ce5aab3f447a6bb4415e46cc06efe01611cd56289b5582bdb46221e8
Name:           perl-FCGI-Client 
Summary:        Client library for the fastcgi protocol
Version:        0.09
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl 
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/FCGI-Client-%{version}.tar.gz
URL:            https://metacpan.org/release/FCGI-Client
BuildArch:      noarch
%{?perl_default_filter}
Provides:       perl(FCGI::Client)
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moo)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(autodie)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
