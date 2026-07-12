%global source0_hash 18cba2392a0b7550bbc3d7c98c6fc5d81f6699d308e4a17e1a143ba4521005a3

Name:           perl-Getopt-Long-Descriptive
Summary:        Getopt::Long with usage text
Version:        0.117
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Getopt-Long-Descriptive
Source0:        https://cpan.metacpan.org/modules/by-module/Getopt/Getopt-Long-Descriptive-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long) >= 2.55
BuildRequires:  perl(List::Util)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Validate) >= 0.97
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter) >= 0.972
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.005
# Optional tests:
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(Moose::Conflicts)
# Dependencies
# (none)

Provides:       perl(Getopt::Long::Descriptive)
Provides:       perl(Getopt::Long::Descriptive)
%description
Convenient wrapper for Getopt::Long and program usage output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Getopt-Long-Descriptive-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes eg/ README
%{perl_vendorlib}/Getopt/
%{_mandir}/man3/Getopt::Long::Descriptive.3*
%{_mandir}/man3/Getopt::Long::Descriptive::Opts.3*
%{_mandir}/man3/Getopt::Long::Descriptive::Usage.3*

%changelog
%autochangelog
