Name:           perl-Module-CPANfile
Version:        1.1004
Release:        24%{?dist}
Summary:        Parse cpanfile
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-CPANfile
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Module-CPANfile-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(CPAN::Meta) >= 2.12091
BuildRequires:  perl(CPAN::Meta::Feature) >= 2.12091
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.12091
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# tests
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(lib)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(CPAN::Meta) >= 2.12091
Requires:       perl(CPAN::Meta::Prereqs) >= 2.12091
Requires:       perl(CPAN::Meta::Feature) >= 2.12091
Requires:       perl(Data::Dumper)
Requires:       perl(Pod::Usage)

%?perl_default_filter
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(CPAN::Meta\\)$
# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(t::Utils\\)

%description
Module::CPANfile is a tool to handle cpanfile format to load application
specific dependencies, not just for CPAN distributions.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Module-CPANfile-%{version}
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
# Remove author tests
rm %{buildroot}%{_libexecdir}/%{name}/t/author-pod-syntax.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/mymeta-cpanfile
%{_bindir}/cpanfile-dump
%{perl_vendorlib}/Module/CPANfile*
%{perl_vendorlib}/cpanfile*
%{_mandir}/man1/mymeta-cpanfile*
%{_mandir}/man1/cpanfile-dump*
%{_mandir}/man3/Module::CPANfile*
%{_mandir}/man3/cpanfile*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1004-24
- Prepare for Oreon 11 (RP1)
