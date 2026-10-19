%global source0_hash a4cccc34bb3f53acf0ba78c9fc61af8d156d109d1c10487ba5988a55077d1f70
Name:           perl-Authen-SASL-SASLprep
Version:        1.100
Release:        29%{?dist}
Summary:        Stringprep profile for user names and passwords (RFC 4013)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Authen-SASL-SASLprep
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/Authen-SASL-SASLprep-%{version}.tar.gz
Patch0:         Authen-SASL-SASLprep-1.01-Recode-README-to-UTF-8.patch
BuildArch:      noarch
Requires:       perl(Unicode::Stringprep) >= 1
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Unicode::Stringprep\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Unicode::Stringprep)
BuildRequires:  perl(Unicode::Stringprep::Mapping)
BuildRequires:  perl(Unicode::Stringprep::Prohibited)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module implements the SASLprep specification, which describes how to
prepare Unicode strings representing user names and passwords for comparison.
SASLprep is a profile of the stringprep algorithm.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Authen-SASL-SASLprep-%{version}
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/{10pod,11pod_cover}.t 
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Authen-SASL-SASLprep-tests -f %{oreon_filedir}/perl-Authen-SASL-SASLprep-tests.list

%changelog

%autochangelog
