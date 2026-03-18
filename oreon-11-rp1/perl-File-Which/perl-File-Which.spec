Name:           perl-File-Which
Version:        1.27
Release:        15%{?dist}
Summary:        Portable implementation of the 'which' utility
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Which
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-Which-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec) >= 0.60
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Env)
BuildRequires:  perl(Config)
BuildRequires:  perl(Test::More) >= 0.80
Requires:       perl(File::Spec) >= 0.60

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Spec\\)$

%description
File::Which is a portable implementation (in Perl) of 'which', and can
be used to get the absolute filename of an executable program
installed somewhere in your PATH, or just check for its existence.

%prep
%setup -q -n File-Which-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/File/
%{_mandir}/man3/File::Which.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.27-15
- Prepare for Oreon 11 (RP1)
