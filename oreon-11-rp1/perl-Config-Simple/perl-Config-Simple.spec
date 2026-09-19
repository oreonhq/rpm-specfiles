%global source0_hash cb78a975ad8463f992f35f392227aaf188d533c9092373742b3c2bb592781054

Name:           perl-Config-Simple
Version:        4.59
Release:        50%{?dist}
Summary:        Simple configuration file class 

#see README
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-Simple
Source0:        http://cpan.org/authors/id/S/SH/SHERZODR/Config-Simple-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:  perl(Data::Dumper)

%description
Simple configuration file class.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-Simple-%{version}
chmod -x README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
chmod -x $RPM_BUILD_ROOT%{perl_vendorlib}/Config/Simple.pm

%check
make test

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
