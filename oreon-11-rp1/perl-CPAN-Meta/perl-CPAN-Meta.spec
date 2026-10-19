%global source0_hash 3918f4a72f44317b43488d7f68644931111ed69b5067e13a32a5e96ac158b0a5
Name:           perl-CPAN-Meta
Summary:        Distribution metadata for a CPAN dist
Version:        2.150015
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Meta
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/CPAN-Meta-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(CPAN::Meta::YAML) >= 0.011
Requires:       perl(Encode)
Requires:       perl(JSON::PP) >= 2.27300
Requires:       perl(version) >= 0.88
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPAN::Meta::Converter\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(CPAN::Meta::Requirements\\)$
Provides:       perl(CPAN::Meta)
Provides:       perl(CPAN::Meta::Converter)
Provides:       perl(CPAN::Meta::Feature)
Provides:       perl(CPAN::Meta::Merge)
Provides:       perl(CPAN::Meta::Prereqs)
Provides:       perl(CPAN::Meta::Validator)
Provides:       perl(Parse::CPAN::Meta)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Software distributions released to the CPAN include a META.json or, for older
distributions, META.yml, which describes the distribution, its contents, and
the requirements for building and installing the distribution. The data
structure stored in the META.json file is described in CPAN::Meta::Spec.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n CPAN-Meta-%{version}

# Silence rpmlint warnings
perl -MConfig -pi -e 's,^#!.*perl,$Config{startperl},' t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
