%global source0_hash 1790e90e69f03f3192f78baeb35521adf6b8b04e2a7374a0d72c407fe18325a4

Name:           perl-Unix-Groups-FFI
Version:        1.000
Release:        20%{?dist}
Summary:        Interface to Unix group system calls
# LICENSE:      Artistic-2.0
## Not in any binary packge
# CONTRIBUTING.md:  CC0-1.0 AND Artistic-2.0
License:        Artistic-2.0
URL:            https://metacpan.org/release/Unix-Groups-FFI
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Unix-Groups-FFI-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(FFI::Platypus) >= 1.00
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.88
# Optional tests:
# CPAN::Meta not helpful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(Exporter) >= 5.57
Requires:       perl(FFI::Platypus) >= 1.00

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Exporter|FFI::Platypus|Test::More)\\)$

%description
This Perl module provides an FFI interface to several system calls related to
Unix groups, including getgroups(2), setgroups(2), getgrouplist(3), and
initgroups(3).

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

%setup -q -n Unix-Groups-FFI-%{version}
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
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
# CONTRIBUTING.md is not helpful (not related to this code)
%doc Changes README
%dir %{perl_vendorlib}/Unix
%dir %{perl_vendorlib}/Unix/Groups
%{perl_vendorlib}/Unix/Groups/FFI.pm
%{_mandir}/man3/Unix::Groups::FFI.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
