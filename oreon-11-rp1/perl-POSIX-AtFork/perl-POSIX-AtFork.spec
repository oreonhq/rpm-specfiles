%global source0_hash c2e2293a86d487144bc8f7ba08e7c4b76b11b0e4dfdc41809845d30efa07e60e

Name:           perl-POSIX-AtFork
Version:        0.04
Release:        22%{?dist}
Summary:        Hook registrations at fork(2)
# lib/POSIX/AtFork.pm:          GPL-1.0-or-later OR Artistic-1.0-Perl
# README:                       GPL-1.0-or-later OR Artistic-1.0-Perl
## Unbundled
# inc/Module/Install/XSUtil.pm: GPL-1.0-or-later OR Artistic-1.0-Perl
## Not used
# android/pthread-atfork.c:     BSD-2-Clause
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POSIX-AtFork
Source0:        https://cpan.metacpan.org/authors/id/N/NI/NIKOLAS/POSIX-AtFork-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::XSUtil)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader) >= 0.1
# Tests:
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::SharedFork)
Requires:       perl(XSLoader) >= 0.1

%{?perl_default_filter}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Test::More|XSLoader)\\)$

%description
This module is an interface to pthread_atfork(3), which registers handlers
called before and after fork(2).

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POSIX-AtFork-%{version}
# Remove bundled modules
rm -rf inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Remove unused sources
rm -rf android
perl -i -ne 'print $_ unless m{^android/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README
%dir %{perl_vendorarch}/auto/POSIX
%dir %{perl_vendorarch}/auto/POSIX/AtFork
%{perl_vendorarch}/auto/POSIX/AtFork/AtFork.so
%dir %{perl_vendorarch}/POSIX
%{perl_vendorarch}/POSIX/AtFork.pm
%{_mandir}/man3/POSIX::AtFork.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
