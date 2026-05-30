%global source0_hash 1b022a0a6451827d060ee9cbfe9b2d8edbac2a3d7155cbee33ea93274b830fb5

# Extra tests require Test::Pod::Coverage::TrustMe, not yet available in Fedora
%bcond_with perl_CPAN_Changes_enables_extra_test

Name:		perl-CPAN-Changes
Summary:	Read and write Changes files
Version:	0.500005
Release:	3%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/CPAN-Changes
Source0:        https://cpan.metacpan.org/modules/by-module/CPAN/CPAN-Changes-%{version}.tar.gz


BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Encode)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Moo) >= 1.006000
BuildRequires:	perl(Moo::Role)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Quote) >= 1.005000
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Types::Standard)
BuildRequires:	perl(version)
BuildRequires:	perl(warnings)
# Script Runtime
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(Pod::Usage)
# Test Suite
BuildRequires:	perl(constant)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.96
# Optional Tests
BuildRequires:	perl(Test::Differences)
# Extra Tests
%if %{with perl_CPAN_Changes_enables_extra_test}
BuildRequires:	findutils
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage::TrustMe) => 0.002000
%endif
# Dependencies
# (none)

%description
It is standard practice to include a Changes file in your distribution. The
purpose of the Changes file is to help a user figure out what has changed
since the last release.

People have devised many ways to write the Changes file. A preliminary
specification has been created (CPAN::Changes::Spec) to encourage module
authors to write clear and concise Changes.

This module will help users programmatically read and write Changes files
that conform to the specification.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n CPAN-Changes-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test
%if %{with perl_CPAN_Changes_enables_extra_test}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes README
%{_bindir}/tidy_changelog
%{perl_vendorlib}/CPAN/
%{perl_vendorlib}/Test/
%{_mandir}/man1/tidy_changelog.1*
%{_mandir}/man3/CPAN::Changes.3*
%{_mandir}/man3/CPAN::Changes::Entry.3*
%{_mandir}/man3/CPAN::Changes::Group.3*
%{_mandir}/man3/CPAN::Changes::Parser.3*
%{_mandir}/man3/CPAN::Changes::Release.3*
%{_mandir}/man3/CPAN::Changes::Spec.3*
%{_mandir}/man3/Test::CPAN::Changes.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.500005-3
- Prepare for Oreon 11 (RP1)
