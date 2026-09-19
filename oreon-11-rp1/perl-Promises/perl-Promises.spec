%global source0_hash 57a184ff4cdb078509c48077343b0b6646aaa27ed0ab83ceb32fa2a2aa6cd140

Name:           perl-Promises
Version:        1.05
Release:        3%{?dist}
Summary:        Implementation of Promises in Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Promises
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/Promises-%{version}.tar.gz
BuildArch:      noarch
# Fix numbering of line in test when shebang is added
Patch0:         Promises-1.05-Fix-numbering-of-line-in-test.patch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(AE)
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(EV)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::Timer::Countdown)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(parent)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Attribute)
BuildRequires:  perl(Sub::Exporter)
# Tests
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Async)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.89
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Warn)
Requires:       perl(Data::Dumper)
Requires:       perl(Module::Runtime)

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(AsyncUtil\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(NoEV\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Promises::Test.*\\)

%description
This module is an implementation of the "Promise/A+" pattern for
asynchronous programming. Promises are meant to be a way to better deal
with the resulting callback spaghetti that can often result in
asynchronous programs.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Promises-%{version}
perl -MConfig -pi -e 's|^#!.*perl|$Config{startperl}|' ./example/*.pl

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
%{_fixperms} $RPM_BUILD_ROOT/*

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes example README.md
%{perl_vendorlib}/Promises*
%{_mandir}/man3/Promises*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
