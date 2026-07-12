%global source0_hash b7a878d44dea67d64df2ca18020d9d868a95596debd16f1a264874209332b07f

Name:           perl-Class-Trigger
Version:        0.15
Release:        17%{?dist}
Summary:        Mixin to add / call inheritable triggers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Trigger
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-Trigger-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(base)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IO::WrapTie)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.32
# Dependencies

Provides:       perl(Class::Trigger)
Provides:       perl(Class::Trigger)
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Class-Trigger-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Trigger.3*

%changelog
%autochangelog
