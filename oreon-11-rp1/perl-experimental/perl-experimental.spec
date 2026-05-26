Name:           perl-experimental
Version:        0.036
Release:        3%{?dist}
Summary:        Experimental features made easy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/experimental
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/experimental-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 42612937c20f0c758547d0519bf535d7f378aa2a01fb20453b2a015a14d6720c
%global source0_file experimental-0.036.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# feature is highly recommended on perl >= 5.10
BuildRequires:  perl(feature)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Test::More) >= 0.89
# feature is highly recommended on perl >= 5.10
Requires:       perl(feature)

%description
This pragma provides an easy and convenient way to enable or disable
experimental features.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/experimental-0.036.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "42612937c20f0c758547d0519bf535d7f378aa2a01fb20453b2a015a14d6720c" || { echo "oreon: Source0 SHA256 mismatch for experimental-0.036.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n experimental-%{version}

# Help file to recognise the Perl scripts
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
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/experimental*
%{perl_vendorlib}/stable*
%{_mandir}/man3/experimental*
%{_mandir}/man3/stable*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.036-3
- Prepare for Oreon 11 (RP1)
