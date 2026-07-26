%global source0_hash c224bf43dbd9c1b5555265b2b4453c81994b604a995c7923aa339e1e46f45dc4

Name:           perl-Task-Kensho-Toolchain
Version:        0.41
Release:        13%{?dist}
Summary:        Glimpse at an Enlightened Perl (basic toolchain)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Kensho-Toolchain
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Task-Kensho-Toolchain-%{version}.tar.gz
# Carton does not work in our distribution
Patch0:         Task-Kensho-Toolchain-0.39-Do-not-use-Carton.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# No run-time dependency is needed for tests.
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(App::cpanminus)
Requires:       perl(App::cpm)
Requires:       perl(App::FatPacker)
Requires:       perl(App::perlbrew)
# Do not use perl(Carton)
# Carton is not provided by Fedora. Carton does not work correctly, if the
# system uses perl installed by a vendor package with modules stripped from
# core as Fedora does.
Requires:       perl(CPAN::Mini)
Requires:       perl(local::lib)
Requires:       perl(Pinto)
Requires:       perl(version)

%{?perl_default_filter}

%description
Task::Kensho is a list of recommended modules for Enlightened Perl
development. CPAN is wonderful, but there are too many wheels and you have
to pick and choose amongst the various competing technologies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Task-Kensho-Toolchain-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENCE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
