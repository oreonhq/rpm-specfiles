%global source0_hash e75687284bfe03b0e46bf9dc5306e65eed680708ec83e4a00fe29608b8fdcc91

Name:           perl-Log-Contextual
Version:        0.009001
Release:        5%{?dist}
Summary:        Simple logging interface with a contextual log
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Contextual
Source0:        https://cpan.metacpan.org/modules/by-module/Log/Log-Contextual-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(Moo) >= 1.003000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Scalar::Util)
# Optional run-time:
BuildRequires:  perl(Log::Log4perl) >= 1.29
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
Requires:       perl(Moo) >= 1.003000

# Filter under-specified depenedencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)\\s*$

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{__requires_exclude}|^perl\\(BaseLogger\\)\\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(DefaultImportLogger\\)\\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(My::Module.*\\)\\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(TestExporter\\)\\s*$
%global __requires_exclude %{__requires_exclude}|^perl\\(TestRouter\\)\\s*$

%description
This module is a simple interface to extensible logging. It is bundled with
a really basic logger, Log::Contextual::SimpleLogger, but in general you
should use a real logger instead of that. For something more serious but
not overly complicated, try Log::Dispatchouli.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Log::Log4perl) >= 1.29

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Log-Contextual-%{version}
# Help generators to recognize Perl scripts
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

# Install tests - copy tests to tmp
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
cp -a t %{buildroot}/%{_libexecdir}/%{name}
cat > %{buildroot}/%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Log/Contextual*
%{_mandir}/man3/Log::Contextual*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
