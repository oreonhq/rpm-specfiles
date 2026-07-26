%global source0_hash 3b309ec091d099cdc1a1abac5e00ec5787f3426241503449658d5ea91dff871e

Name:           perl-perlindex
Version:        1.606
Release:        36%{?dist}
Summary:        Index and search the perl documentation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/perlindex
Source0:        https://cpan.metacpan.org/authors/id/U/UL/ULPFR/perlindex-%{version}.tar.gz
# CPAN RT#92170
Patch0:         perlindex-1.606-Remove-useless-interpreter-declaration-from-Text-Eng.patch
# Allow testing out-of-tree code, CPAN RT#155766, proposed to upstream
Patch1:         perlindex-1.606-Allow-testing-installed-code.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
# Run-time:
BuildRequires:  perl(AnyDBM_File)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(Getopt::Long)
# IO::Scalar is optional
BuildRequires:  perl(less)
# Pod::Text is optional
BuildRequires:  perl(Term::ReadKey)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
Requires:       perl(File::Find)

%description
Perlindex is a program to index and search the perl documentation. It provides
Text::English module implementing Porter stemming algorithm.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Cwd)
Requires:       perl(File::Spec)
Requires:       perl(File::Temp)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n perlindex-%{version}
chmod +x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Install tests
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a MANIFEST perlindex.PL README t $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cat > $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x $RPM_BUILD_ROOT%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc ChangeLog README
%{_bindir}/perlindex
%dir %{perl_vendorlib}/Text
%{perl_vendorlib}/Text/English.pm
%{_mandir}/man1/perlindex.*
%{_mandir}/man3/Text::English.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
