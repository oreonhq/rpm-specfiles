Name:           perl-Devel-LexAlias
Version:        0.05
Release:        42%{?dist}
Summary:        Alias lexical variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-LexAlias
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Devel-LexAlias-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
# Module Runtime
BuildRequires:  perl(Devel::Caller) >= 0.03
BuildRequires:  perl(DynaLoader)
# Test Suite
BuildRequires:  perl(Test::More)
# Dependencies

%{?perl_default_filter}

%description
Devel::LexAlias provides the ability to alias a lexical variable in a
subroutines scope to one of your choosing.

%prep
%setup -q -n Devel-LexAlias-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes
%{perl_vendorarch}/auto/Devel/
%{perl_vendorarch}/Devel/
%{_mandir}/man3/Devel::LexAlias.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.05-42
- Prepare for Oreon 11 (RP1)
