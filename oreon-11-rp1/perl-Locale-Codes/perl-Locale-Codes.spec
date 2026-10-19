%global source0_hash 5ebbb252bb296e6a2ce4cf544ee378919252c4b7e4ffecd9afd67a5735b57749
Name:           perl-Locale-Codes
Version:        3.91
Release:        1%{?dist}
Summary:        Distribution of modules to handle locale codes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Locale-Codes
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBECK/Locale-Codes-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(deprecate)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Locale::Codes::Country_Retired\\)|^perl\\(Locale::Codes::LangFam_Retired\\)|^perl\\(Locale::Codes::Script_Retired\\)|^perl\\(Locale::Codes::LangExt_Codes\\)|^perl\\(Locale::Codes::LangFam_Codes\\)|^perl\\(Locale::Codes::Script_Codes\\)|^perl\\(Locale::Codes::Language_Codes\\)|^perl\\(Locale::Codes::LangExt_Retired\\)|^perl\\(Locale::Codes::Currency_Codes\\)|^perl\\(Locale::Codes::LangVar_Retired\\)|^perl\\(Locale::Codes::Language_Retired\\)|^perl\\(Locale::Codes::Country_Codes\\)|^perl\\(Locale::Codes::LangVar_Codes\\)|^perl\\(Locale::Codes::Currency_Retired\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(do_tests\\.pl\\)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Test::Inter\\)$
Provides:       perl(Locale::Country)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Inter)
BuildRequires:  perl(constant)
BuildRequires:  perl(deprecate)
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Locale-Codes is a distribution containing a set of modules. The modules
each deal with different types of codes which identify parts of the locale
including languages, countries, currency, etc.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Inter) >= 1.09
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Locale-Codes-%{version}
chmod -x examples/*
chmod +x t/*.pl
# Delete release tests
rm t/_*
perl -i -lne 'print $_ unless m{\At/_}' MANIFEST
# Delete unused files
rm t/runtests t/runtests.bat
perl -i -lne 'print $_ unless m{\At/runtests}' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -j $(getconf _NPROCESSORS_ONLN)
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Locale-Codes-tests -f %{oreon_filedir}/perl-Locale-Codes-tests.list

%changelog

%autochangelog
