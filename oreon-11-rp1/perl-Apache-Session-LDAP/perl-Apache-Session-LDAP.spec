%global source0_hash 5138f95531e21e5b1bb373beee6c9bbbcb1b337cc84e007f439a21ccf64cba3b
Name:		perl-Apache-Session-LDAP
Version:	0.5
Release:        1%{?dist}
Summary:        LDAP implementation of Apache::Session
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Apache-Session-LDAP
Source0:        https://cpan.metacpan.org/modules/by-module/Apache/Apache-Session-LDAP-%{version}.tar.gz
Patch0:		Apache-Session-LDAP-0.5-synopsis-cafile.patch
BuildArch:	noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Apache::Session)
BuildRequires:  perl(Apache::Session::Generate::MD5)
BuildRequires:  perl(Apache::Session::Lock::Null)
BuildRequires:  perl(Apache::Session::Serialize::Base64)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
LDAP implementation of Apache::Session. Sessions are stored as LDAP entries
inside a branch.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Apache-Session-LDAP-%{version}

# Fix certificate bundle location in SYNOPSIS
%patch -P0

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
