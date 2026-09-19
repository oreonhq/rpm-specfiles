%global source0_hash faaa0c97827e6e2a4b015110aff27b84427a6ca7334a5d28f0e6c11ab7e21c08

Name:           perl-Syntax-Highlight-Engine-Kate
Version:        0.16
Release:        1%{?dist}
Summary:        Port to Perl of the syntax highlight engine of the Kate text editor
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Syntax-Highlight-Engine-Kate
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Syntax-Highlight-Engine-Kate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install) >= 0.91
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Basename)
# lib not used
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Term::ANSIColor not used
BuildRequires:  perl(XML::Dumper)
BuildRequires:  perl(XML::TokeParser)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(diagnostics)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Differences) >= 0.61
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 1.00
BuildRequires:  perl(Test::Warn) >= 0.30
BuildRequires:  perl(Time::HiRes)
# Optional tests:
# Test::Pod 1.00 not used
Requires:       perl(base)

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TestHighlight\\)

%description
Syntax::Highlight::Engine::Kate is a port to perl of the syntax highlight
engine of the Kate text editor.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Syntax-Highlight-Engine-Kate-%{version}
find -type f -exec chmod -c -x {} +
# Remove bundled modules
rm -rf ./inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

# Help generators to recognize Perl scripts
for F in `find t -name *.t`; do
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
cp -a t samples %{buildroot}%{_libexecdir}/%{name}
ln -s %{_docdir}/%{name}/REGISTERED %{buildroot}%{_libexecdir}/%{name}/REGISTERED
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README REGISTERED
%dir %{perl_vendorlib}/Syntax
%dir %{perl_vendorlib}/Syntax/Highlight
%dir %{perl_vendorlib}/Syntax/Highlight/Engine
%{perl_vendorlib}/Syntax/Highlight/Engine/Kate*
%{_mandir}/man3/Syntax::Highlight::Engine::Kate*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
