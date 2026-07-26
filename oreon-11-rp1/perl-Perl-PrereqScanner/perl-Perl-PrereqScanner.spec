%global source0_hash 01181d38a2e7aff838d262122563c50636ba4b3652ee5d1d4f8ef5ba3f5b186b

Name:           perl-Perl-PrereqScanner
Version:        1.100
Release:        8%{?dist}
Summary:        Tool to scan your Perl code for its prerequisites
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-PrereqScanner
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Perl-PrereqScanner-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.124
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
# Getopt::Long::Descriptive not used at tests
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Module::Path)
BuildRequires:  perl(Moo) >= 2.000000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(PPI) >= 1.215
# Scalar::Util not used at tests
BuildRequires:  perl(String::RewritePrefix) >= 0.005
BuildRequires:  perl(Types::Standard)
# Tests only
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
# Optional tests only
# CPAN::Meta not useful
Requires:       perl(Module::Path)

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPAN::Meta::Requirements\\)$ 

%description
The scanner will extract loosely your distribution prerequisites from
your files.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-PrereqScanner-%{version}

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
cp -a corpus t %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_libexecdir}/%{name}/bin
ln -s %{_bindir}/scan_prereqs %{buildroot}%{_libexecdir}/%{name}/bin
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
