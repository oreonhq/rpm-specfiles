%global source0_hash 04cbc81e786968f9a4109ad6c2f9b81e879ac0c6b6080a9d217443b61dfd2498

Name:           perl-PAR-Dist
Version:        0.53
Release:        5%{?dist}
Summary:        Toolkit for creating and manipulating Perl PAR distributions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PAR-Dist
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSCHUPP/PAR-Dist-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
# perl(ExtUtils::Install) not tested
BuildRequires:  perl(ExtUtils::MY)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
# perl(LWP::Simple) not tested
# perl(Module::Signature) >= 0.25 not tested
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML::Tiny)
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
Requires:       perl(Archive::Zip)
Requires:       perl(Cwd)
Requires:       perl(ExtUtils::Install)
Requires:       perl(ExtUtils::MY)
Requires:       perl(File::Copy)
Requires:       perl(File::Find)
Requires:       perl(File::Path)
Requires:       perl(File::Temp)
Requires:       perl(LWP::Simple)
Requires:       perl(Module::Signature) >= 0.25
Requires:       perl(YAML::Tiny)

Provides:       perl(PAR::Dist)
%description
This module creates and manipulates PAR distributions. They are architecture-
specific PAR files, containing everything under blib/ of CPAN distributions
after their make or Build stage, a META.yml describing metadata of the
original CPAN distribution, and a MANIFEST detailing all files within it.
Digitally signed PAR distributions will also contain a SIGNATURE file.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n PAR-Dist-%{version}

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

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories. The easiest solution
# is to copy the tests into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset PERL_TEST_POD
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/PAR*
%{_mandir}/man3/PAR::Dist*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
