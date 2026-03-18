# Run optional tests
%bcond_without perl_Lexical_SealRequireHints_enables_optional_test

Name:           perl-Lexical-SealRequireHints
Version:        0.012
Release:        12%{?dist}
Summary:        Prevent leakage of lexical hints
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lexical-SealRequireHints
Source0:        https://cpan.metacpan.org/modules/by-module/Lexical/Lexical-SealRequireHints-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.15
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More) >= 0.41
BuildRequires:  perl(XSLoader)
%if %{with perl_Lexical_SealRequireHints_enables_optional_test}
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Thread::Semaphore)
BuildRequires:  perl(threads)
BuildRequires:  perl(threads::shared)
%endif
# Dependencies
Conflicts:      perl(B:Hooks::OP::Check) < 0.19

%{?perl_default_filter}

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(t::.*\\)

%description
This module works around two historical bugs in Perl's handling of the %%^H
(lexical hints) variable. One bug causes lexical state in one file to leak
into another that is required/used from it. This bug [perl #68590], was
present from Perl 5.6 up to Perl 5.10, fixed in Perl 5.11.0. The second bug
causes lexical state (normally a blank %%^H once the first bug is fixed) to
leak outwards from utf8.pm, if it is automatically loaded during Unicode
regular expression matching, into whatever source is compiling at the time
of the regexp match. This bug [perl #73174], was present from Perl 5.8.7
up to Perl 5.11.5, fixed in Perl 5.12.0.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Lexical-SealRequireHints-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor --optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} -c $RPM_BUILD_ROOT

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
./Build test

%files
%doc Changes README
%{perl_vendorarch}/auto/Lexical/
%{perl_vendorarch}/Lexical/
%{_mandir}/man3/Lexical::SealRequireHints.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.012-12
- Prepare for Oreon 11 (RP1)
