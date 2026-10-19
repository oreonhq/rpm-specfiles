%global source0_hash b7a878d44dea67d64df2ca18020d9d868a95596debd16f1a264874209332b07f
Name:           perl-Class-Trigger
Version:        0.15
Release:        1%{?dist}
Summary:        Mixin to add / call inheritable triggers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Trigger
Source0:        https://cpan.metacpan.org/modules/by-module/Class/Class-Trigger-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Class::Trigger)
Provides:       perl(Class::Trigger)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IO::WrapTie)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
