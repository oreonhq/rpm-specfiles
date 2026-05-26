# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 a83e8e28f416d9a3f70afee8a37cb0ac1515cbf941c677e9f1f97b643bffedab
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           perl-Config-Perl-V
Version:        0.39
Release:        1%{?dist}
Summary:        Structured data retrieval of perl -V output
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-Perl-V
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/Config-Perl-V-%{version}.tgz
# Correct example
Patch0:         Config-Perl-V-0.24-Remove-invalid-shellbang.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(warnings)
# Optional run-time:
BuildRequires:  perl(Digest::MD5)
# Tests:
BuildRequires:  perl(Test::More)
%if !%{defined perl_bootstrap}
# Building core modules must not require non-core modules when bootstrapping
BuildRequires:  perl(Test::NoWarnings)
%endif
Suggests:       perl(Digest::MD5)
Conflicts:      perl < 4:5.22.0-347

%description
The command "perl -V" will return you an excerpt from the %%Config::Config
hash combined with the output of "perl -V" that is not stored inside the hash,
but only available to the perl binary itself. This package provides Perl
module that will return you the output of "perl -V" in a structure.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if !%{defined perl_bootstrap}
Requires:       perl(Digest::MD5)
Requires:       perl(Test::NoWarnings)
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_verify_sources
%setup -q -n Config-Perl-V-%{version}
%patch -P0 -p1
chmod -x examples/*

for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
# Building core modules must not require non-core modules when bootstrapping
make test PERL_CORE=%{defined perl_bootstrap}

%files
%doc Changelog CONTRIBUTING.md examples README
%dir %{perl_vendorlib}/Config
%{perl_vendorlib}/Config/Perl
%{_mandir}/man3/Config::Perl::V*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.39-1
- Prepare for Oreon 11 (RP1)
