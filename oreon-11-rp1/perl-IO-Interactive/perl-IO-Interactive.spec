%global source0_hash 30aaa346a0f664f837750b1b9b3b511e78c7779296fb8f3be31aae5b73f7efb7

# Perform optional tests
%bcond_without perl_IO_Interactive_enables_optional_test

Name:           perl-IO-Interactive
Version:        1.027
Release:        3%{?dist}
Summary:        Utilities for interactive I/O
# lib/IO/Interactive.pm:    GPL-1.0-or-later OR Artistic-1.0-Perl
# LICENSE:                  (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Artistic-2.0
# license_clarification:    Artistic-2.0 (brian d foy's explanation)
# README.pod:               "see LICENSE file and the modules files"
# IO-Ineractive-1.021 added the ambiguous LICENSE file. Because there are
# still files only referring to Perl, but not referring to Artistic-2.0,
# I keep the (GPL-1.0-or-later OR Artistic-1.0-Perl) part in the License tag.
# <https://github.com/briandfoy/io-interactive/issues/2>
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Artistic-2.0
URL:            https://metacpan.org/release/IO-Interactive
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/IO-Interactive-%{version}.tar.gz
Source1:        license_clarification
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
# Test::Manifest not used
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::Handle)
# Tests:
BuildRequires:  perl(Test::More) >= 1
%if %{with perl_IO_Interactive_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
Requires:       perl(Carp)

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$

%description
This module provides utility subroutines that make it easier to develop
interactive applications.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 1

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Interactive-%{version}
install -m 0644 %{SOURCE1} .
%if !%{with perl_IO_Interactive_enables_optional_test}
rm t/pod*
perl -i -ne 'print $_ unless m{^t/pod}' MANIFEST
%endif
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_IO_Interactive_enables_optional_test}
rm %{buildroot}%{_libexecdir}/%{name}/t/pod*
%endif
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
%doc Changes examples license_clarification README.pod SECURITY.md
%dir %{perl_vendorlib}/IO
%{perl_vendorlib}/IO/Interactive.pm
%{_mandir}/man3/IO::Interactive.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
