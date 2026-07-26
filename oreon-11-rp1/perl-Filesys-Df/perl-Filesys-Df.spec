%global source0_hash fe89cbb427e0e05f1cd97c2dd6d3866ac6b21bc7a85734ede159bdc35479552a

Name:           perl-Filesys-Df
Version:        0.92
Release:        58%{?dist}
Summary:        Perl extension for filesystem disk space information
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Filesys-Df
Source0:        https://cpan.metacpan.org/modules/by-module/Filesys/Filesys-Df-%{version}.tar.gz
# Fix a test plan, CPAN RT#140742, proposed to the upstream
Patch0:         Filesys-Df-0.92-Fix-test-plan.patch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%description
This module provides a way to obtain filesystem disk space information.
This is a Unix only distribution. If you want to gather this information
for Unix and Windows, use Filesys::DfPortable. The only major benefit of
using Filesys::Df over Filesys::DfPortable, is that Filesys::Df supports
the use of open file handles as arguments.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Filesys-Df-%{version}
#readme is with dos EOL, convert it to unix
perl -i -pe 's/\r//' README
 
%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a test.pl %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . test.pl
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc Changes README
%dir %{perl_vendorarch}/auto/Filesys
%{perl_vendorarch}/auto/Filesys/Df
%dir %{perl_vendorarch}/Filesys
%{perl_vendorarch}/Filesys/Df.pm
%{_mandir}/man3/Filesys::Df.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
