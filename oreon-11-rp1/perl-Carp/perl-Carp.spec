%global source0_hash f5273b4e1a6d51b22996c48cb3a3cbc72fd456c4038f5c20b127e2d4bcbcebd9

%global base_version 1.50
Name:           perl-Carp
Version:        1.54
Release:        521%{?dist}
Summary:        Alternative warn and die for modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Carp
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/Carp-%{base_version}.tar.gz
# Unbundled from perl 5.34.0
Patch0:         Carp-1.50-Upgrade-to-1.52.patch
# Unbundled from perl 5.37.11
Patch1:         Carp-1.52-Upgrade-to-1.54.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(warnings)
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(Exporter)
# Tests:
BuildRequires:  perl(B)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
# IPC::Open3  >= 1.0103 in reality, but the provides is 2-digit number only
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More) >= 0.47

# Do not export private DB module stub
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DB\\)
# Filter versioned tests require IPC::Open3 >= 1.0103, because provides is
# 2-digit number only
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(IPC::Open3\\)

%description
The Carp routines are useful in your own modules because they act like
die() or warn(), but with a message which is more likely to be useful to a
user of your module. In the case of cluck, confess, and longmess that
context is a summary of every call in the call-stack. For a shorter message
you can use carp or croak which report the error as being from where your
module was called. There is no guarantee that that is where the error was,
but it is a good educated guess.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl(IPC::Open3)
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Carp-%{base_version}
%patch -P0 -p1
%patch -P1 -p1

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.54-521
- Prepare for Oreon 11 (RP1)
