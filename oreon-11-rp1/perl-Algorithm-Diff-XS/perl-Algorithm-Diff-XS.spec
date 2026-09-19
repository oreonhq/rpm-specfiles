%global source0_hash cea89b47e1f70fa78f55f3c405491ce36d3effd9980f5c5491edffa31aa77153

Name:           perl-Algorithm-Diff-XS
Version:        0.04
Release:        35%{?dist}
Summary:        Algorithm::Diff with XS core loop
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Algorithm-Diff-XS
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/Algorithm-Diff-XS-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Install::Can)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Algorithm::Diff) >= 1.19
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests only
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test)
Requires:       perl(Algorithm::Diff) >= 1.19
Requires:       perl(XSLoader)

%global __requires_exclude ^perl\\(Algorithm::Diff\\)$

%description
Drop-in replacement to Algorithm::Diff, but "compact_diff" and "LCSidx"
will run much faster for large data sets.

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

%setup -q -n Algorithm-Diff-XS-%{version}
# Unbundle inc::Module::Install
rm -rf ./inc
perl -i -ne 'print $_ unless m{\Ainc/}' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="%{optflags}"
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
%doc Changes README
%dir %{perl_vendorarch}/auto/Algorithm
%dir %{perl_vendorarch}/auto/Algorithm/Diff
%{perl_vendorarch}/auto/Algorithm/Diff/XS
%dir %{perl_vendorarch}/Algorithm
%dir %{perl_vendorarch}/Algorithm/Diff
%{perl_vendorarch}/Algorithm/Diff/XS.pm
%{_mandir}/man3/Algorithm::Diff::XS.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
