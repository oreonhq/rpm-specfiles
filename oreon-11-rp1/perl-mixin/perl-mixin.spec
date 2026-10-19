%global source0_hash 88b6d7ea4dc3764ab11c1f08f1fe47b9b84ddeea0d4209b86b2e5831fb9902f9
Name:           perl-mixin
Version:        0.09
Release:        4%{?dist}
Summary:        Mixin inheritance, an alternative to multiple inheritance
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/mixin
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/mixin-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(base)
Requires:       perl(Carp)
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(Dog::
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Mixin inheritance is an alternative to the usual multiple-inheritance and
solves the problem of knowing which parent will be called. It also solves a
number of tricky problems like diamond inheritance.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(UNIVERSAL)
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mixin-%{version}
# Remove bundled modules
rm -r t/lib/Test
perl -i -ne 'print $_ unless m{\At/lib/Test/}' MANIFEST
# Correct permissions
chmod a+x t/*.t

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-mixin-tests -f %{oreon_filedir}/perl-mixin-tests.list

%changelog

%autochangelog
