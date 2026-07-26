%global source0_hash a124611236dd87e2402219a040e3011d55dd55ee7d3b55234fb67e94c33378c8

Name:           perl-Tie-Hash-MultiValue
Version:        1.07
Release:        4%{?dist}
Summary:        Store multiple values per key
# LICENSE:      "Perl itself, GPL-2.0-or-later OR Artistic-1.0-Perl", CPAN RT#125581
# lib/Tie/Hash/MultiValue.pm:  "same terms as Perl, see LICENSE"
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/Tie-Hash-MultiValue
Source0:        https://cpan.metacpan.org/authors/id/M/MC/MCMAHON/Tie-Hash-MultiValue-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(Tie::Hash) >= 1
BuildRequires:  perl(vars)
# Tests:
# Test::More version from Test::Simple in META
BuildRequires:  perl(Test::More) >= 0.44
Requires:       perl(Tie::Hash) >= 1

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Test::More|Tie::Hash)\\)$

%description
Tie::Hash::MultiValue Perl module allows you to have hashes which store their
values in anonymous arrays, appending any new value to the already-existing
ones.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# Test::More version from Test::Simple in META
Requires:       perl(Test::More) >= 0.44

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tie-Hash-MultiValue-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} "$RPM_BUILD_ROOT"/*
# Install tests
mkdir -p "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
cp -a t "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}
cat > "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x "$RPM_BUILD_ROOT"%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README Todo
%dir %{perl_vendorlib}/Tie
%dir %{perl_vendorlib}/Tie/Hash
%{perl_vendorlib}/Tie/Hash/MultiValue.pm
%{_mandir}/man3/Tie::Hash::MultiValue.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
