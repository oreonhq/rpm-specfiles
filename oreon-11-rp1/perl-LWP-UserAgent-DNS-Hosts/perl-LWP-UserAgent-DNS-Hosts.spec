%global source0_hash 996979443f086ffc8b366bdbba4486591d93f9217bc204b3e5d66b947220871f

Name:           perl-LWP-UserAgent-DNS-Hosts
Version:        0.14
Release:        16%{?dist}
Summary:        Override LWP HTTP/HTTPS request's host like /etc/hosts

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-UserAgent-DNS-Hosts
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MASAKI/LWP-UserAgent-DNS-Hosts-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# runtime
BuildRequires:  perl(parent)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(LWP::Protocol)
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Scope::Guard)
# tests:
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::UseAllModules)
BuildRequires:  perl(Test::Fake::HTTPD) >= 0.08
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(File::Temp)

%{?perl_default_filter}

%description
LWP::UserAgent::DNS::Hosts is a module to override HTTP/HTTPS request peer
addresses that uses LWP::UserAgent.  This module concept was got from
LWP::Protocol::PSGI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n LWP-UserAgent-DNS-Hosts-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
