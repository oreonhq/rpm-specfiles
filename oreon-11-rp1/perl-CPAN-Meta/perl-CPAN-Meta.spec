%global source0_hash 7c2bcbaf988d50ba8902a0d0cdf3c66b22aa7e968f5b67d1339a8995aff25dbd

Name:           perl-CPAN-Meta
Summary:        Distribution metadata for a CPAN dist
Version:        2.150013
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Meta
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/CPAN-Meta-2.150013.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(CPAN::Meta::YAML) >= 0.011
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(JSON::PP) >= 2.27300
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(version) >= 0.88
BuildRequires:  perl(warnings)
# Main test suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.20
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Dependencies
Requires:       perl(CPAN::Meta::YAML) >= 0.011
Requires:       perl(Encode)
Requires:       perl(JSON::PP) >= 2.27300
Requires:       perl(version) >= 0.88

# Avoid doc-file dependencies
%{?perl_default_filter}

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPAN::Meta::Converter\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(CPAN::Meta::Requirements\\)$

%description
Software distributions released to the CPAN include a META.json or, for older
distributions, META.yml, which describes the distribution, its contents, and
the requirements for building and installing the distribution. The data
structure stored in the META.json file is described in CPAN::Meta::Spec.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n CPAN-Meta-%{version}

# Silence rpmlint warnings
perl -MConfig -pi -e 's,^#!.*perl,$Config{startperl},' t/*.t

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
%doc Changes CONTRIBUTING.mkdn history README Todo t/
%{perl_vendorlib}/CPAN/
%{perl_vendorlib}/Parse/
%{_mandir}/man3/CPAN::Meta.3*
%{_mandir}/man3/CPAN::Meta::Converter.3*
%{_mandir}/man3/CPAN::Meta::Feature.3*
%{_mandir}/man3/CPAN::Meta::History.3*
%{_mandir}/man3/CPAN::Meta::History::Meta_1_0.3*
%{_mandir}/man3/CPAN::Meta::History::Meta_1_1.3*
%{_mandir}/man3/CPAN::Meta::History::Meta_1_2.3*
%{_mandir}/man3/CPAN::Meta::History::Meta_1_3.3*
%{_mandir}/man3/CPAN::Meta::History::Meta_1_4.3*
%{_mandir}/man3/CPAN::Meta::Merge.3*
%{_mandir}/man3/CPAN::Meta::Prereqs.3*
%{_mandir}/man3/CPAN::Meta::Spec.3*
%{_mandir}/man3/CPAN::Meta::Validator.3*
%{_mandir}/man3/Parse::CPAN::Meta.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.150013-1
- Import
