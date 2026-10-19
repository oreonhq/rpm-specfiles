%global source0_hash 79a8ccd3682b639cd589e3c05f8339e07cc82ddd9ef2a0db778a10ad467d5f6c
Name:           perl-Module-CoreList
Epoch:          1
Version:        5.20260924
Release:        1%{?dist}
Summary:        What modules are shipped with versions of perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-CoreList
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Module-CoreList-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(List::Util)
Requires:       perl(version) >= 0.88
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(version\\)$
Provides:       perl(Module::CoreList)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Module::CoreList provides information on which core and dual-life modules
are shipped with each version of perl.

%package tools
Summary:        Tool for listing modules shipped with perl
Requires:       perl(feature)
Requires:       perl(version) >= 0.88
Requires:       perl-Module-CoreList = %{epoch}:%{version}-%{release}
Conflicts:      perl-Module-CoreList < 1:5.20140914
%description tools
This package provides a corelist(1) tool which can be used to query what
modules were shipped with given perl version.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-tools = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}-%{version}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-CoreList-%{version}

# Help file to recognise the Perl scripts and normalize shebangs
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
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
rm -f %{buildroot}/%{_libexecdir}/%{name}/t/pod.t
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
unset PERL_CORE
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}/%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset PERL_CORE
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Module-CoreList-tools -f %{oreon_filedir}/perl-Module-CoreList-tools.list
%files -n perl-Module-CoreList-tests -f %{oreon_filedir}/perl-Module-CoreList-tests.list

%changelog

%autochangelog
