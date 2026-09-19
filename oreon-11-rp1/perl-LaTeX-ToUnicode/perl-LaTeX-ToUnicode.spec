%global source0_hash 06d6865edd63409da2cb3d58a57a2486154cc97c74b94b957e7c29ea0b8d394e

Name:           perl-LaTeX-ToUnicode
Version:        1.93
Release:        2%{?dist}
Summary:        Convert LaTeX commands to Unicode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LaTeX-ToUnicode
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BORISV/LaTeX-ToUnicode-%{version}.tar.gz
# Remove an unhelpful dependency on texlive-kpathsea,
# not suitable for an upstream
Patch0:         LaTeX-ToUnicode-0.53-Do-not-add-bogus-paths-to-INC.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
# File::Spec not used at tests
# Getopt::Long not used at tests
BuildRequires:  perl(utf8)
# Tests:
BuildRequires:  perl(Test::More)

%description
This Perl module provides a method to convert LaTeX-style markups for accents
etc. into their Unicode equivalents. It translates commands for special
characters or accents into their Unicode equivalents and removes
formatting commands.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n LaTeX-ToUnicode-%{version}
# Remove always skipped tests
for F in t/release-pod-coverage.t t/release-pod-syntax.t t/release-synopsis.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
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
%doc Changes README
%dir %{perl_vendorlib}/LaTeX
%{perl_vendorlib}/LaTeX/ToUnicode
%{perl_vendorlib}/LaTeX/ToUnicode.pm
%{_bindir}/ltx2unitxt
%{_mandir}/man3/LaTeX::ToUnicode.*
%{_mandir}/man3/LaTeX::ToUnicode::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
