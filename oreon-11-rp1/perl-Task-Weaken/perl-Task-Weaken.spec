%global source0_hash 2383fedb9dbaef646468ea824afbf7c801076720cfba0df2a7a074726dcd66be

Name:           perl-Task-Weaken
Version:        1.06
Release:        23%{?dist}
Summary:        Ensure that a platform has weaken support
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Weaken
Source0:        https://cpan.metacpan.org/modules/by-module/Task/Task-Weaken-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Scalar::Util) >= 1.14
# Tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More) >= 0.42
# Dependencies
Requires:       perl(Scalar::Util) >= 1.14

Provides:       perl(Task::Weaken)
%description
One recurring problem in modules that use Scalar::Util's weaken function is
that it is not present in the pure-perl variant.

This restores the functionality testing to a dependency you do once in
your Makefile.PL, rather than something you have to write extra tests
for each time you write a module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Task-Weaken-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} -c $RPM_BUILD_ROOT

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Task/
%{_mandir}/man3/Task::Weaken.3*

%changelog
%autochangelog
