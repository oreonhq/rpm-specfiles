Name:           perl-Sub-Info
Version:        0.002
Release:        28%{?dist}
Summary:        Tool for inspecting Perl subroutines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sub-Info
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Sub-Info-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 ea3056d696bdeff21a99d340d5570887d39a8cc47bff23adfc82df6758cdd0ea
%global source0_file Sub-Info-0.002.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Importer) >= 0.024
# Tests:
BuildRequires:  perl(Test2::Tools::Tiny) >= 1.302072
Requires:       perl(Importer) >= 0.024

%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Importer\\)$

%description
This allows to inspect Perl subroutines.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Sub-Info-0.002.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ea3056d696bdeff21a99d340d5570887d39a8cc47bff23adfc82df6758cdd0ea" || { echo "oreon: Source0 SHA256 mismatch for Sub-Info-0.002.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Sub-Info-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.002-28
- Prepare for Oreon 11 (RP1)
