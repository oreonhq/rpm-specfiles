%global source0_hash bba533d06c197608087f03d0b1e7e327d74165e7b49a46a372a7af2c1f1883dc
Name:           perl-Module-Faker
Version:        0.027
Release:        1%{?dist}
Summary:        Build fake dists for testing CPAN tools
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Faker
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Module-Faker-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Path::Class) >= 0.06
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Path::Class\\)\s*$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Archive::Any::Create)
BuildRequires:  perl(Archive::Any::Create::Zip)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Converter)
BuildRequires:  perl(CPAN::Meta::Merge)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Fake)
BuildRequires:  perl(Data::Fake::Names)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Next)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Template)
BuildRequires:  perl(experimental)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Module::Faker is a tool for building fake CPAN modules and, perhaps more
importantly, fake CPAN distributions. These are useful for running tools
that operate against CPAN distributions without having to use real CPAN
distributions. This is much more useful when testing an entire CPAN
instance, rather than a single distribution, for which see CPAN::Faker.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Faker-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t eg %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Module-Faker-tests -f %{oreon_filedir}/perl-Module-Faker-tests.list

%changelog

%autochangelog
