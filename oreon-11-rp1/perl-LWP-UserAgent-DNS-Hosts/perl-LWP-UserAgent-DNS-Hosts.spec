%global source0_hash 996979443f086ffc8b366bdbba4486591d93f9217bc204b3e5d66b947220871f
Name:           perl-LWP-UserAgent-DNS-Hosts
Version:        0.14
Release:        1%{?dist}
Summary:        Override LWP HTTP/HTTPS request's host like /etc/hosts
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-UserAgent-DNS-Hosts
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MASAKI/LWP-UserAgent-DNS-Hosts-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(LWP::Protocol)
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Test::Fake::HTTPD)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::UseAllModules)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
