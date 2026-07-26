%global source0_hash 9358719be14799fc61e04989df7fdb9c0541402b0b8a7bdd181ff464f1cd2dfd

Name:           perl-Apache-Htpasswd
Version:        1.9
Release:        37%{?dist}
Summary:        Manage Unix crypt-style password file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Apache-Htpasswd
Source0:        https://cpan.metacpan.org/authors/id/K/KM/KMELTZ/Apache-Htpasswd-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::PasswdMD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker) %{!?el7:>= 6.76}
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
This module comes with a set of methods to use with htaccess password files.
These files (and htaccess) are used to do Basic Authentication on a web server.
The passwords file is a flat-file with login name and their associated
encrypted password. You can use this for non-Apache files if you wish, but it
was written specifically for .htaccess style files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-Htpasswd-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor %{!?el7:NO_PACKLIST=1 NO_PERLLOCAL=1}
%make_build

%install
%make_install
%if 0%{?el7}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name perllocal.pod -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
%endif
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README
%{perl_vendorlib}/Apache
%{_mandir}/man3/Apache::Htpasswd.3pm.*

%changelog
%autochangelog
