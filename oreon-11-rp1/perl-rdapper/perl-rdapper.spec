%global source0_hash c4daf62b95b8bbbb7c3a04cda3b02624de4da8abbe15d8b7f02c2bac15640414
%bcond_with perl_rdapper_enables_online_test
Name:           perl-rdapper
Version:        1.24
Release:        1%{?dist}
Summary:        Simple console-based RDAP client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/App-rdapper
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBROWN/App-rdapper-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_rdapper_enables_online_test}
%endif
Requires:       perl(List::Util) >= 1.33
Requires:       perl(LWP::Protocol::https)
Recommends:     perl(PPI)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(List::Util\\)$
# oreon:deps
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::Maketext::Gettext)
BuildRequires:  perl(Net::ASN)
BuildRequires:  perl(Net::DNS::Domain)
BuildRequires:  perl(Net::IDN::PP)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(Net::RDAP)
BuildRequires:  perl(Net::RDAP::EPPStatusMap)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::Size)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(common::sense)
BuildRequires:  perl(constant)
BuildRequires:  perl(locale)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
"rdapper" is a simple RDAP client. It uses Net::RDAP to retrieve data about
internet resources (domain names, IP addresses, and autonomous systems) and
outputs the information in a human-readable format.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n App-rdapper-%{version}
# Remove pregenerated files
rm locale/*/LC_MESSAGES/*.mo
# Remove disabled tests
%if %{without perl_rdapper_enables_online_test}
rm t/02.test.t
perl -i -ne 'print $_ unless m{\A\Qt/02.test.t\E}' MANIFEST
%endif

%build

./mkmo.sh
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
rm %{buildroot}%{perl_vendorlib}/auto/share/module/App-rdapper/rdapper.pot
rm %{buildroot}%{perl_vendorlib}/auto/share/module/App-rdapper/*/LC_MESSAGES/*.po
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset RDAPPER_LOCALE_DIR
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset RDAPPER_LOCALE_DIR
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%define l10n_dir() %lang(%1) %{perl_vendorlib}/auto/share/module/App-rdapper/%1
%files -f %{oreon_filedir}/main.list
%files -n perl-rdapper-tests -f %{oreon_filedir}/perl-rdapper-tests.list

%changelog

%autochangelog
