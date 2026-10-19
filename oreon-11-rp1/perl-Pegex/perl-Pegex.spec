%global source0_hash 4dc8d335de80b25247cdb3f946f0d10d9ba0b3c34b0ed7d00316fd068fd05edc
Name:           perl-Pegex
Version:        0.75
Release:        19%{?dist}
Summary:        Pegex Parser Generator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pegex
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Pegex-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Dumper)
Requires:       perl(JSON::PP)
Requires:       perl(Term::ANSIColor)
Requires:       perl(XXX) >= 0.35
Requires:       perl(YAML::PP) >= 0.019
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(YAML::PP\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((TestAST|TestML)
%global __requires_exclude %{__requires_exclude}|^perl\\((TestAST|TestML)
Provides:       perl(Pegex)
Provides:       perl(Pegex::Base)
Provides:       perl(Pegex::Parser)
Provides:       perl(Pegex::Base)
Provides:       perl(Pegex::Parser)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(YAML::PP)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Pegex is an Acmeist parser framework. It is a PEG parser grammar syntax,
combined with PCRE compatible regular expressions as the match tokens.
Pegex draws heavily from Perl 6 rules, but works equivalently in many
modern programming languages.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(List::Util)
Requires:       perl(YAML::PP) >= 0.019
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Pegex-%{version}
# Remove author tests
rm t/author-pod-syntax.t
perl -i -ne 'print $_ unless m{^t/author-pod-syntax\.t}' MANIFEST
# Remove shebangs
for F in t/pegex-tml/*; do
    perl -i -ne 'print $_ unless m{^#!}' "$F"
    chmod -x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a inc t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/000-compile-modules.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Pegex-tests -f %{oreon_filedir}/perl-Pegex-tests.list

%changelog

%autochangelog
