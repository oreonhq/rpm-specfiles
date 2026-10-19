%global source0_hash b57d80ca6d821c6949ca48b27467d45aba7a9c77346562306facca781a003e44
Name:           perl-HTTP-Date
Version:        6.08
Release:        1%{?dist}
Summary:        Date conversion routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Date
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-Date-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Time::Local) >= 1.28
Requires:       perl(Time::Zone)
Conflicts:      perl-libwww-perl < 6
Suggests:       perl(JSON::PP) >= 2.27300
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Time::Local\\)$
Provides:       perl(HTTP::Date)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Time::Zone)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides functions that deal the date formats used by the HTTP
protocol (and then some more). Only the first two functions, time2str() and
str2time(), are exported by default.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n HTTP-Date-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/00-*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING PERL_COMPILE_TEST_DEBUG
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-HTTP-Date-tests -f %{oreon_filedir}/perl-HTTP-Date-tests.list

%changelog

%autochangelog
