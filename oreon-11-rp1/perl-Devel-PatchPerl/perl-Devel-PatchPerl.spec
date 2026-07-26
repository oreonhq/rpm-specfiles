%global source0_hash 2426d27ab00f65ecded5cdc8f2c2889b01c199063ab4ab688fc8df39cdde9a0f

Name:           perl-Devel-PatchPerl
Version:        2.14
Release:        2%{?dist}
Summary:        Patch perl source a la Devel::PPPort's buildperl.pl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-PatchPerl
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Devel-PatchPerl-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(constant)
BuildRequires:  perl(File::pushd) >= 1.00
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(lib)
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::More)
# Test::Pod not used
# Test::Pod::Coverage not used
Requires:       patch
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(File::pushd) >= 1.00

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::pushd\\)$
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}

%description
Devel::PatchPerl is a modularization of the patching code contained in
Devel::PPPort's buildperl.pl.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-PatchPerl-%{version}
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
rm -rf %{buildroot}%{_libexecdir}/%{name}/t/author*t
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
%dir %{perl_vendorlib}/Devel
%{perl_vendorlib}/Devel/PatchPerl*
%{_bindir}/patchperl
%{_mandir}/man1/patchperl*
%{_mandir}/man3/Devel::PatchPerl*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
