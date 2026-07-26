%global source0_hash 6ea3682cd6ecb91a772d7c233366f1a51258253997a208d1451deda56487a5ca

# Run optional test
%bcond_without perl_BibTeX_Parser_enables_optional_test

Name:           perl-BibTeX-Parser
Version:        1.93
Release:        2%{?dist}
Summary:        Pure Perl BibTeX parser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/BibTeX-Parser
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BORISV/BibTeX-Parser-%{version}.tar.gz
# Remove a strayed debugging output, CPAN RT#134350, proposed to the upstream
Patch0:         BibTeX-Parser-1.03-Remove-a-debugging-output-from-BibTeX-Parser-Entry-t.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# A bump of LaTeX::ToUnicode minimal version to 0.55 seems abitrary and
# unnecessary
%global latex_to_unicode_min_ver 0.11
BuildRequires:  perl(LaTeX::ToUnicode) >= %{latex_to_unicode_min_ver}
BuildRequires:  perl(overload)
# Tests:
BuildRequires:  perl(constant)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
%if %{with perl_BibTeX_Parser_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
Requires:       perl(LaTeX::ToUnicode) >= %{latex_to_unicode_min_ver}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((LaTeX::ToUnicode|Test::More)\\)$

%description
This is a BibTeX parser written in Perl.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.88

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n BibTeX-Parser-%{version}
# Remove skipped tests
for F in t/08-parse_large.t t/release-pod-*.t \
%if %{without perl_BibTeX_Parser_enables_optional_test}
t/pod.t t/pod-coverage.t \
%endif
; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
# Correct the permissions
chmod a+x t/*.t

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
%if %{with perl_BibTeX_Parser_enables_optional_test}
# POD tests enumarate ./blib files
rm %{buildroot}%{_libexecdir}/%{name}/t/pod.t \
    %{buildroot}%{_libexecdir}/%{name}/t/pod-coverage.t
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
%doc Changes README
%dir %{perl_vendorlib}/BibTeX
%{perl_vendorlib}/BibTeX/Parser
%{perl_vendorlib}/BibTeX/Parser.pm
%{_mandir}/man3/BibTeX::Parser.*
%{_mandir}/man3/BibTeX::Parser::*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
