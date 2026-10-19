%global source0_hash f81d766c3f728057be0e8fbe249c4e123dcf9a557ae300cd80187791acdae2db
Name:           perl-Log-Report-Template
Version:        1.04
Release:        1%{?dist}
Summary:        Template Toolkit with translations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Log-Report-Template
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/Log-Report-Template-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Log::Report) >= 1.42
Requires:       perl(String::Print) >= 0.91
Requires:       perl(Template) >= 2.26
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Log::Report|String::Print|Template|Test::More)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Log::Report)
BuildRequires:  perl(Log::Report::Domain)
BuildRequires:  perl(Log::Report::Extract)
BuildRequires:  perl(Log::Report::Lexicon::POT)
BuildRequires:  perl(Log::Report::Message)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(String::Print)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Filters)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module extends Template, which is the core of Template Toolkit. The main
addition is support for translations via the translation framework offered by
Log::Report.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       coreutils
Requires:       perl-Test-Harness
Requires:       perl(Log::Report) >= 1.42
Requires:       perl(Test::More) >= 1
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Report-Template-%{version}
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
set -e
DIR=$(mktemp -d)
cp -a %{_libexecdir}/%{name}/* "$DIR"
pushd "$DIR"
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -r "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Log-Report-Template-tests -f %{oreon_filedir}/perl-Log-Report-Template-tests.list

%changelog

%autochangelog
