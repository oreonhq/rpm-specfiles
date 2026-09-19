%global source0_hash 3aa9b31ddf6952284d9461a6a14642e29696c0e5d0eb861fbecf79fbcf62d4c2

Name:       perl-Best 
Version:    0.17
Release:    4%{?dist}
# inc:      GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:  MIT
SourceLicense:  (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MIT
License:    MIT 
Summary:    Fallbackable module loader 
Url:        https://metacpan.org/release/Best
Source:     https://cpan.metacpan.org/authors/id/G/GA/GAAL/Best-%{version}.tar.gz
# Remove unwanted build dependencies
Patch0:     Best-0.15-Remove-unwanted-dependencies.patch
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
# Carp not used
BuildRequires:  perl(constant)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Data::Dumper not used at tests
BuildRequires:  perl(overload)
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
Recommends:     perl(Data::Dumper)

%{?perl_default_filter}
# Hide private modules
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Load::Trace\\)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\((A::Module|AnAlternative|LastChance|Load::Trace|Loads::Ok|Version::Ok|Version::TooLow)\\)

%description
Often there are several possible providers of some functionality your
program needs, but you don't know which is available at the run site.
For example, one of the modules may be implemented with XS, or not in
the core Perl distribution and thus not necessarily installed. "Best"
attempts to load modules from a list, stopping at the first successful
load and failing only if no alternative was found.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Best-%{version}
# Unbundle inc::Module::Install
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Remove always skipped tests
rm t/pod-coverage.t
perl -i -ne 'print $_ unless m{^\Qt/pod-coverage.t\E}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/{boilerplate.t,pod.t}
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
%doc Changes README example
%{perl_vendorlib}/Best.pm
%{_mandir}/man3/Best.3*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
