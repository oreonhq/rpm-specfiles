%global source0_hash 8b7f9389fb42d77f7b9e0a42f93da413e7b32d183db96bd35b3707840a29b094
Name:           perl-HTTP-Tiny-Paranoid
Version:        0.07
Release:        1%{?dist}
Summary:        Safer HTTP::Tiny
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/HTTP-Tiny-Paranoid
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBN/HTTP-Tiny-Paranoid-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Net::DNS::Paranoid)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is a subclass of HTTP::Tiny that performs exactly one
additional function: before connecting, it passes the hostname to
Net::DNS::Paranoid. If the hostname is rejected, then the request is
aborted before a connect is even attempted.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-Tiny-Paranoid-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

perl -I./lib -MHTTP::Tiny::Paranoid -e '1;'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
