%global source0_hash c4589d5ec21e206cacb61f909820f7164b47c26603138545a1ab1e4c2e95556e
Name:		perl-GPS-OID
Version:	0.07
Release:        1%{?dist}
Summary:        Package for PRN - Object ID conversions
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/GPS-OID
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRDVT/GPS-OID-%{version}.tar.gz
BuildArch:	noarch
Provides:	perl-GPS-PRN = %{version}-%{release}
Provides:	perl(GPS::OID) = %{version}
Obsoletes:	perl-GPS-PRN < 0.07
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GPS-OID-%{version}
chmod -c a-x scripts/GPS-OID-example.pl

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
