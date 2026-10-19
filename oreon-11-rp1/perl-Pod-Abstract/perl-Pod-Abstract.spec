%global source0_hash 11bab4ba691dd73d5be6c6f5088d624d128a81233b75bd690af041540214efa6
Name:           perl-Pod-Abstract
Version:        0.26
Release:        2%{?dist}
Summary:        Abstract document tree for Perl POD documents
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Pod-Abstract
Source0:        https://cpan.metacpan.org/authors/id/B/BL/BLILBURNE/Pod-Abstract-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Task::Weaken)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Pod::Parser)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
POD::Abstract provides a means to load a POD (or POD compatible) document
without direct reference to it's syntax, and perform manipulations on the
abstract syntax tree.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pod-Abstract-%{version}
chmod 644 lib/Pod/Abstract/Filter/*.pm 
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
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -pe "s{^bin}{%{_bindir}}" %{buildroot}%{_libexecdir}/%{name}/t/02_roundtrip.t
perl -i -pe "s{^lib/Pod}{%{perl_vendorlib}/Pod}" %{buildroot}%{_libexecdir}/%{name}/t/02_roundtrip.t
perl -i -pe "s{lib/Pod}{%{perl_vendorlib}/Pod}" %{buildroot}%{_libexecdir}/%{name}/t/06_pa_example.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Pod-Abstract-tests -f %{oreon_filedir}/perl-Pod-Abstract-tests.list

%changelog

%autochangelog
