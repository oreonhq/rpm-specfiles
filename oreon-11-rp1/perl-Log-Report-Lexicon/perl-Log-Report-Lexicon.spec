%global source0_hash a07b5ee023680103a2d92a4a28167d3f210ec8516f8a5de0366433c4c53cd390
Name:           perl-Log-Report-Lexicon
Version:        1.15
Release:        1%{?dist}
Summary:        Translation component of Log::Report
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
SourceLicense:  (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-3.0-or-later AND LGPL-2.0-or-later
URL:            https://metacpan.org/dist/Log-Report-Lexicon
Source0:        http://www.cpan.org/authors/id/M/MA/MARKOV/Log-Report-Lexicon-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Log::Report) >= 1.4
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Log::Report|Test::More)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  glibc-langpack-tr
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::gettext)
BuildRequires:  perl(Log::Report)
BuildRequires:  perl(Log::Report::Translator)
BuildRequires:  perl(Log::Report::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This package contains all components of Log::Report which handle translations.

%package tests
Summary:        Tests for %{name}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-3.0-or-later AND LGPL-2.0-or-later
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Log::Report) >= 1.4
Requires:       perl(Test::More) >= 1.00
Requires:       glibc-langpack-tr
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Report-Lexicon-%{version}
# Remove Win32 specific files which do not work on Linux
rm lib/Log/Report/Win32Locale.*
perl -i -ne 'print $_ if m{^lib/Log/Report/Win32Locale.}' MANIFEST
# Correct shebangs
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
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' --
 '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Log-Report-Lexicon-tests -f %{oreon_filedir}/perl-Log-Report-Lexicon-tests.list

%changelog

%autochangelog
