Name:           perl-inc-latest
Epoch:          2
Version:        0.500
Release:        32%{?dist}
Summary:        Use modules bundled in inc/ if they are newer than installed ones
License:        Apache-2.0
URL:            https://metacpan.org/release/inc-latest
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/inc-latest-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 daa905f363c6a748deb7c408473870563fcac79b9e3e95b26e130a4a8dc3c611
%global source0_file inc-latest-0.500.tar.gz
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
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
Requires:       perl(ExtUtils::Installed)
Conflicts:      perl-Module-Build < 2:0.42.10-4

%description
The inc::latest module helps bootstrap configure-time dependencies for CPAN
distributions. These dependencies get bundled into the inc directory within
a distribution and are used by Makefile.PL or Build.PL.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/inc-latest-0.500.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "daa905f363c6a748deb7c408473870563fcac79b9e3e95b26e130a4a8dc3c611" || { echo "oreon: Source0 SHA256 mismatch for inc-latest-0.500.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n inc-latest-%{version}
# Help generators to recognize Perl scripts
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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.500-32
- Prepare for Oreon 11 (RP1)
