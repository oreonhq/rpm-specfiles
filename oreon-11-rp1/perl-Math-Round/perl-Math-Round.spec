%global source0_hash 7b4d2775ad3b859a5fd61f7f3fc5cfba42b1a10df086d2ed15a0ae712c8fd402

Name:           perl-Math-Round
Version:        0.08
Release:        7%{?dist}
Summary:        Perl extension for rounding numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Round
Source0:        https://cpan.metacpan.org/modules/by-module/Math/Math-Round-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More) >= 0.88
# Dependencies
# (no additional dependencies)

%description
Math::Round supplies functions that will round numbers in different ways. The
functions round and nearest are exported by default; others are available as
described below. "use ... qw(:all)" exports all functions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Round-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Math/
%{_mandir}/man3/Math::Round.3*

%changelog
%autochangelog
