%global source0_hash 5310f83460045475071666b5423db2f0aa82d6685c802ec7abe6c2c410639b96

Name:           perl-String-MkPasswd
Version:        0.05
Release:        4%{?dist}
Summary:        Perl module for generating random passwords
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/String-MkPasswd
Source0:        https://cpan.metacpan.org/modules/by-module/String/String-MkPasswd-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildArch:      noarch

%description
This packages provides a perl module to generate random passwords.

%package scripts
Requires:       %{name} = %{version}-%{release}
Summary:        Perl script for generating random passwords

%description scripts
This packages provides a perl script to generate random passwords.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-MkPasswd-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%dir %{perl_vendorlib}/String
%{perl_vendorlib}/String/MkPasswd.pm
%{_mandir}/man3/String::MkPasswd.3pm*

%files scripts
%{_bindir}/mkpasswd.pl
%{_mandir}/man1/mkpasswd.pl.1*

%changelog
%autochangelog
