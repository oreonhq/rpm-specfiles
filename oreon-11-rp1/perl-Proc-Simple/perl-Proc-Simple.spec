%global source0_hash 4c8f0a924b19ad78a13da73fe0fb306d32a7b9d10a332c523087fc83a209a8c4

Name:           perl-Proc-Simple
Version:        1.32
Release:        29%{?dist}
Summary:        Launch and control background processes
# README:           GPL-1.0-or-later OR Artistic-1.0-Perl
# Simple.pm:        GPL-1.0-or-later OR Artistic-1.0-Perl
## Not in any binary package
# .licensizer.yml:  GPL-1.0-or-later OR Artistic-1.0-Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Proc-Simple
Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHILLI/Proc-Simple-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.3
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
Requires:       perl(Time::HiRes)

%description
The Proc::Simple module provides objects mimicking real-life processes from
a user's point of view. Either external programs or Perl subroutines can be
launched and controlled as processes in the background.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Proc-Simple-%{version}
# Correct file modes
chmod -x eg/*.pl
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# t/sh-c.t writes into CWD
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes README eg
%dir %{perl_vendorlib}/Proc
%{perl_vendorlib}/Proc/Simple.pm
%{_mandir}/man3/Proc::Simple.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
