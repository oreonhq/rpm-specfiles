%global source0_hash 12e07e9e3aca812f86100dea7eaf19db291eaab1e4ef4d764a5b8868452c2913

Name:           perl-Test2-Plugin-DBIProfile
%global cpan_version 0.002006
Version:        0.2.6
Release:        15%{?dist}
Summary:        Test2 plugin to enable and display DBI profiling
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test2-Plugin-DBIProfile
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Plugin-DBIProfile-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.9
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(DBI::Profile)
BuildRequires:  perl(Test2::API) >= 1.302165
BuildRequires:  perl(Test2::Util::Times) >= 0.000126
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::SQLite) >= 1.44
BuildRequires:  perl(DBI)
# Test2::Tools::Basic version from Test2::V0 in META
BuildRequires:  perl(Test2::Tools::Basic) >= 0.000124
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Defer)
BuildRequires:  perl(vars)
Requires:       perl(Test2::API) >= 1.302165
Requires:       perl(Test2::Util::Times) >= 0.000126
# Removed from perl-Test2-Harness-0.001083
Conflicts:      perl-Test2-Harness < 0.001083

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test2::API|Test2::Util::Times|Test2::Tools::Basic)\\)$

%description
This Test2 plugin enables DBI::Profile globally so that DBI profiling data is
collected. Once testing is complete an event will be produced which contains
and displays the profiling data.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(DBD::SQLite) >= 1.44
Requires:       perl(Test2::API) >= 1.302165
Requires:       perl(Test2::Plugin::DBIProfile)
# Test2::Tools::Basic version from Test2::V0 in META
Requires:       perl(Test2::Tools::Basic) >= 0.000124

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test2-Plugin-DBIProfile-%{cpan_version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
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
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
