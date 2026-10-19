%global source0_hash 7687d62f98a6afe6c906514e552cd7c764b3d59dc2ddc659fad616cd5b7531c6
Name:           perl-AtteanX-Compatibility-Trine
Version:        0.002
Release:        1%{?dist}
Summary:        Compatibility layer between RDF::Trine and Attean
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/AtteanX-Compatibility-Trine
Source0:        https://cpan.metacpan.org/authors/id/K/KJ/KJETILK/AtteanX-Compatibility-Trine-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Attean) >= 0.019
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Attean|Test::More)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Attean)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a compatibility layer between RDF::Trine and Attean Perl modules. For
now, only certain methods of RDF::Trine nodes are supported.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::More) >= 0.96
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n AtteanX-Compatibility-Trine-%{version}
chmod a+x t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
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
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-AtteanX-Compatibility-Trine-tests -f %{oreon_filedir}/perl-AtteanX-Compatibility-Trine-tests.list

%changelog

%autochangelog
