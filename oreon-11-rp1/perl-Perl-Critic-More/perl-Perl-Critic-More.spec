%global source0_hash 69e2acff61b7bead745721991e2b83c88624ae8239d4371a785a3ce2d967187b

Name:           perl-Perl-Critic-More
Version:        1.003
Release:        34%{?dist}
Summary:        Supplemental policies for Perl::Critic
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-More
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THALJEF/Perl-Critic-More-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
# Devel::NYTProf not used
BuildRequires:  perl(English)
# File::Which not used
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(lib)
# Run-time:
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Perl::Critic) >= 1.098
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Perl::MinimumVersion) >= 0.14
BuildRequires:  perl(Readonly) >= 1.03
# Tests:
BuildRequires:  perl(Perl::Critic::Config)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Perl::Critic::Violation)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
# Optional test:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Perl::Critic) >= 1.098
Requires:       perl(Perl::MinimumVersion) >= 0.14
Requires:       perl(Readonly) >= 1.03

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Readonly\\)$

%description
This is a collection of Perl::Critic policies that are not included in the
Perl::Critic core for a variety of reasons.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(ExtUtils::Manifest)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-More-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm %{buildroot}%{_libexecdir}/%{name}/t/98*
rm %{buildroot}%{_libexecdir}/%{name}/t/99*
# MANIFEST file is used in test
cp -a MANIFEST %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README TODO.pod
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
