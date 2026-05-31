%global source0_hash 6281bd87cced7a885c38aa104498e3cd4b5f4c276087442cf68c67379318f27d

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Term_ANSIColor_enables_optional_test
%else
%bcond_with perl_Term_ANSIColor_enables_optional_test
%endif

Name:           perl-Term-ANSIColor
Version:        5.01
Release:        522%{?dist}
Summary:        Color screen output using ANSI escape sequences
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Term-ANSIColor
Source0:        https://cpan.metacpan.org/modules/by-module/Term/Term-ANSIColor-%{version}.tar.gz



BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
# Tests
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More)
# Optional tests
%if %{with perl_Term_ANSIColor_enables_optional_test} && !%{defined perl_bootstrap}
BuildRequires:  perl(IPC::System::Simple)
%endif

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::RRA.*\\)

%description
This module has two interfaces, one through color() and colored() and the
other through constants. It also offers the utility functions uncolor(),
colorstrip(), colorvalid(), and coloralias(), which have to be explicitly
imported to be used. 

%package tests
Summary:        Tests for %{name}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MIT AND FSFAP
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# Optional tests
%if %{with perl_Term_ANSIColor_enables_optional_test} && !%{defined perl_bootstrap}
Requires:       perl(IPC::System::Simple)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Term-ANSIColor-%{version}
chmod -c -x examples/*

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
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author/release tests
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/docs
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/style
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorlib}/Term*
%{_mandir}/man3/Term::ANSIColor*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.01-522
- Prepare for Oreon 11 (RP1)
