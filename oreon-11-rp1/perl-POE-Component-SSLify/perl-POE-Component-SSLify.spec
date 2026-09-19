%global source0_hash 1db61c1da047c96de4972b529c72a90d806991f65fd79418951a312461dc185d

# Perform author and release tests
%bcond_with perl_POE_Component_SSLify_enables_extra_test

Name:           perl-POE-Component-SSLify
Version:        1.012
Release:        37%{?dist}
Summary:        Makes using SSL in the world of POE easy!
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POE-Component-SSLify
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/POE-Component-SSLify-%{version}.tar.gz
# Do not use SSLv3 in tests. It's not supported by Net-SSLeay-1.68 with
# OpenSSL-1.0.2a, bug #1222521, CPAN RT#104493
Patch0:         POE-Component-SSLify-1.012-Use-default-SSL-version-in-tests.patch
# Work around a SIGPIPE bug in TLSv1.3 server, bug #1622999, CPAN RT#126976
Patch1:         POE-Component-SSLify-1.012-Disable-sessions-tickets-with-OpenSSL-1.1.1.patch
# Adapt to OpenSSL 3, bug #2007254, CPAN RT#139684, proposed to the upstream
Patch2:         POE-Component-SSLify-1.012-Adapt-to-OpenSSL-3.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::Handle) >= 1.28
BuildRequires:  perl(Net::SSLeay) >= 1.36
BuildRequires:  perl(parent)
BuildRequires:  perl(POE) >= 1.267
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Task::Weaken) >= 1.03
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(POE::Component::Client::TCP)
BuildRequires:  perl(POE::Component::Server::TCP)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::More) >= 1.001002
%if %{with perl_POE_Component_SSLify_enables_extra_test}
# Extra tests
BuildRequires:  perl(POE::Filter::Stream)
# Optional tests:
# CPAN::Meta not usefull
BuildRequires:  perl(IO::Prompt::Tiny)
BuildRequires:  perl(Test::Apocalypse) >= 1.000
%endif
Requires:       perl(POE) >= 1.267
Requires:       perl(warnings)

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((IO::Handle|Net::SSLeay|POE)\\)$

%description
This component represents the standard way to do SSL in POE.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(blib)
Requires:       perl(IO::Handle) >= 1.28
Requires:       perl(Net::SSLeay) >= 1.36

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n POE-Component-SSLify-%{version}
%if !%{with perl_POE_Component_SSLify_enables_extra_test}
rm t/99_mire_test.t t/apocalypse.t t/simple_parallel_superbig.t t/simple_superbig.t
perl -i -ne 'print $_ unless m{^\Qt/99_mire_test.t\E}' MANIFEST
perl -i -ne 'print $_ unless m{^\Qt/apocalypse.t\E}' MANIFEST
perl -i -ne 'print $_ unless m{^\Qt/simple_parallel_superbig.t\E}' MANIFEST
perl -i -ne 'print $_ unless m{^\Qt/simple_superbig.t\E}' MANIFEST
%endif
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a mylib t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
%if %{with perl_POE_Component_SSLify_enables_extra_test}
export AUTOMATED_TESTING=1
%else
export AUTOMATED_TESTING=0
%endif
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
# Clean debuginfo generator pollution breaking MANIFEST test
rm -f *.list
# AUTOMATED_TESTING triggers author tests (t/simple_parallel_superbig.t) which
# fails. Upstream says: "thus is marked as TODO." CPAN RT#100549.
%if %{with perl_POE_Component_SSLify_enables_extra_test}
export AUTOMATED_TESTING=1
%else
export AUTOMATED_TESTING=0
%endif
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
