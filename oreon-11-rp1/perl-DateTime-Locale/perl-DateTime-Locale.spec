%global source0_hash fda10fd3ee85f9ce73f46e4ccfe764243978c3ac377e3097597058101b935d9f
Name:           perl-DateTime-Locale
Version:        1.46
Release:        1%{?dist}
Summary:        Localization support for DateTime.pm
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND Unicode-DFS-2015
URL:            https://metacpan.org/release/DateTime-Locale
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Locale-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Dist::CheckConflicts) >= 0.02
Conflicts:      perl-DateTime <= 1:0.7000-3.fc16
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Dist::CheckConflicts\\)$
Provides:       perl(DateTime::Locale)
Provides:       perl(DateTime::Locale::Base)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Check)
BuildRequires:  perl(CPAN::Meta::Prereqs)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::ValidationCompiler)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test2::Plugin::NoWarnings)
BuildRequires:  perl(Test2::Plugin::UTF8)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::File::ShareDir::Dist)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DateTime::Locale is primarily a factory for the various locale sub-classes.
It also provides some functions for getting information on all the
available locales.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-Locale-%{version}

# Help file to recognise the Perl scripts
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
%files -n perl-DateTime-Locale-tests -f %{oreon_filedir}/perl-DateTime-Locale-tests.list

%changelog

%autochangelog
