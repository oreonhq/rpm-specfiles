%global source0_hash 11c606056fd62bd44e079f7bef06c459aa589ee85cdedbfa0cc325ea357c8e79

Name:           perl-Test-Pod-No404s
Version:        0.02
Release:        41%{?dist}
Summary:        Checks POD for HTTP 404 links
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Pod-No404s
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/Test-Pod-No404s-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
# ExtUtils::MakeMaker not needed
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-Time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Simple::Text)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(URI::Find)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88
# Inject correct provide, bug #1160263
Provides:       perl(Test::Pod::No404s) = %{version}

# Filter bogus provide, bug #1160263
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Test::Pod::No404s\\) = 404$

Provides:       perl(Test::Pod::No404s)
%description
This module looks for any HTTP(S) links in your POD and verifies that they
will not return a 404. It uses LWP::UserAgent for the heavy lifting, and
simply lets you know if it failed to retrieve the document. More specifically,
it uses $response->is_error as the "test".

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(lib)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Pod-No404s-%{version}
rm t/apocalypse.t
perl -i -ne 'print $_ unless m{\At/apocalypse\.t\b}' MANIFEST
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install "--destdir=%{buildroot}" --create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc AUTHOR_PLEDGE Changes CommitLog examples README
%dir %{perl_vendorlib}/Test
%dir %{perl_vendorlib}/Test/Pod
%{perl_vendorlib}/Test/Pod/No404s.pm
%{_mandir}/man3/Test::Pod::No404s.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
