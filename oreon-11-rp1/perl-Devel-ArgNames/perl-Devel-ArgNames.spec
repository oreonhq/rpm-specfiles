%global source0_hash 59cc9e6b77af9b4b1a24bbe858d700d0909282b26dfb7f7963adb8bca3edce98

Name:           perl-Devel-ArgNames
Version:        0.03
Release:        36%{?dist}
Summary:        Figure out the names of variables passed into subroutines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-ArgNames
Source0:        https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/Devel-ArgNames-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(ok)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This Perl module provides a function which returns the names associated
with the variables found on @_.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Devel::ArgNames)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-ArgNames-%{version}

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
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%dir %{perl_vendorlib}/Devel
%{perl_vendorlib}/Devel/ArgNames.pm
%{_mandir}/man3/Devel::ArgNames.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
