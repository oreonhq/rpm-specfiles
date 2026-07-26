%global source0_hash 5974e2128c799d4c95772719d5bbb2040e52adec1a20c75e2587b91aacbf3499

Name:           perl-Module-Install-TestTarget
Version:        0.19
Release:        39%{?dist}
Summary:        Assembles custom test targets for make
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Install-TestTarget
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAICRON/Module-Install-TestTarget-%{version}.tar.gz
# Adjust tests to ExtUtils-MakeMaker-6.07, bug #1259401, CPAN RT#106843
Patch0:         Module-Install-TestTarget-0.19-Adapt-to-ExtUtils-MakeMaker-6.07.patch
# Restore compatibility with Perl 5.26.0, CPAN RT#102922
Patch1:         Module-Install-TestTarget-0.19-Fix-escaping-literal-curly-brackets-in-regexpes.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Install) >= 1.00
BuildRequires:  perl(Module::Install::Base)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(warnings)
# Optional tests:
BuildRequires:  perl(Module::Install::ExtraTests)
Requires:       perl(Module::Install) >= 1.00
Requires:       perl(B::Deparse)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
# Remove private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(t::Util\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(t::Util\\)

%description
Module::Install::TestTarget creates make test variations with code
snippets. This helps module developers to test their distributions with
various conditions.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(inc::Module::Install)
Requires:       perl(Module::Install::ExtraTests)
Requires:       perl(Test::More) >= 0.96

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Module-Install-TestTarget-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -r -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%dir %{perl_vendorlib}/Module
%dir %{perl_vendorlib}/Module/Install
%{perl_vendorlib}/Module/Install/TestTarget.pm
%{_mandir}/man3/Module::Install::TestTarget.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
