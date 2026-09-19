%global source0_hash f591db9f9a8355c67fba94ae27e06e6339b800ca78c5250d75c7688c0bc33969

%global cpan_version 1.07

Name:           perl-Hash-Case
Version:        1.70.0
Release:        1%{?dist}
Summary:        Base class for hashes with key-casing requirements
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Hash-Case
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Hash-Case-%{cpan_version}.tar.gz
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
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::StdHash)
# Tests:
BuildRequires:  perl(Test::More) >= 0.47

%description
Hash::Case is the base class for various classes which tie special treatment
for the casing of keys. Be aware of the differences in implementation: Lower
and Upper are tied native hashes: these hashes have no need for hidden fields
or other assisting data structured. A case Preserve hash will actually create
three hashes.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Hash-Case-%{cpan_version}

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
%doc ChangeLog README
%dir %{perl_vendorlib}/Hash
%{perl_vendorlib}/Hash/Case*
%{_mandir}/man3/Hash*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
