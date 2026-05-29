%global source0_hash 8df87a10c14c8e909c5b47c5701e4b8187d519e5251e87c80709b02bb33efdd7

Name:           perl-local-lib
Version:        2.000029
Release:        11%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Create and use a local lib/ for perl modules
Url:            https://metacpan.org/release/local-lib
Source:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/local-lib-2.000029.tar.gz
Source10:       perl-homedir.sh
Source11:       perl-homedir.csh
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(CPAN)
BuildRequires:  perl(CPAN::HandleConfig)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.00
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)
Requires:       perl(Carp::Heavy)
Requires:       perl(File::Basename)
Requires:       perl(File::Glob)
Requires:       perl(File::Spec)

# Filter modules bundled for tests
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(ENVDumper\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(TempDir\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(Carp::Foo\\)

%description
This module provides a quick, convenient way of bootstrapping a user-
local Perl module library located within the user's home directory. It
also constructs and prints out for the user the list of environment
variables using the syntax appropriate for the user's current shell (as
specified by the 'SHELL' environment variable), suitable for directly
adding to one's shell configuration file.

More generally, local::lib allows for the bootstrapping and usage of a
directory containing Perl modules outside of Perl's '@INC'. This makes
it easier to ship an application with an app-specific copy of a Perl module,
or collection of modules. Useful in cases like when an upstream maintainer
hasn't applied a patch to a module of theirs that you need for your
application.

%package -n perl-homedir
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Per-user Perl local::lib setup
Requires:   %{name} = %{version}-%{release}
Requires:   sed

%description -n perl-homedir
perl-homedir configures the system to automatically create a ~/perl5
directory in each user's $HOME on user login.  This allows each user to
install CPAN packages via the CPAN to their $HOME, with no additional
configuration or privileges, and without installing them system-wide.

If you want your users to be able to install and use their own Perl modules,
install this package.

%package tests
Summary:    Tests for %{name}
Requires:   %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:   perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n local-lib-%{version}

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
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -pm0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/profile.d/
install -pm0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/profile.d/

# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -r -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files -n perl-homedir
%{_sysconfdir}/profile.d/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.000029-11
- Prepare for Oreon 11 (RP1)
