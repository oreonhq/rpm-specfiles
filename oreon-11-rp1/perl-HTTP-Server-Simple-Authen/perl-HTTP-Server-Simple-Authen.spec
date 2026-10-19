%global source0_hash 2dddc8ab9dc8986980151e4ba836a6bbf091f45cf195be1768ebdb4a993ed59b
Name:           perl-HTTP-Server-Simple-Authen
Version:        0.04
Release:        1%{?dist}
Summary:        Authentication plugin for HTTP::Server::Simple
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Server-Simple-Authen
Source0:        https://cpan.metacpan.org/modules/by-module/HTTP/HTTP-Server-Simple-Authen-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Authen::Simple) >= 0.04
Requires:       perl(HTTP::Server::Simple) >= 0.16
Requires:       perl(Test::More) >= 0.32
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Authen::Simple)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
%description
HTTP::Server::Simple::Authen is an HTTP::Server::Simple plugin to allow
HTTP authentication. Authentication scheme is pluggable and you can use
whatever Authentication protocol that Authen::Simple supports.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Server-Simple-Authen-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
