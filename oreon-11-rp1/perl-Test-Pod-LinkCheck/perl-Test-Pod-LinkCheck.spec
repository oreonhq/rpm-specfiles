%global source0_hash 2bfe771173c38b69eeb089504e3f76511b8e45e6a9e6dac3e616e400ea67bcf0

Name:           perl-Test-Pod-LinkCheck
Version:        0.008
Release:        40%{?dist}
Summary:        Tests POD for invalid links
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Pod-LinkCheck
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/Test-Pod-LinkCheck-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
# ExtUtils::MakeMaker not used
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(App::PodLinkCheck::ParseLinks) >= 4
BuildRequires:  perl(App::PodLinkCheck::ParseSections)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moose) >= 1.01
BuildRequires:  perl(Moose::Util::TypeConstraints) >= 1.01
BuildRequires:  perl(parent)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Test::Builder) >= 0.94
BuildRequires:  perl(Test::Pod) >= 1.44
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Tester)
# Optional tests:
# Test::Apocalypse skips all tests as release tests, do not use it. It is also
# in build cycle with this package.
Requires:       perl(App::PodLinkCheck::ParseSections)
Requires:       perl(Capture::Tiny)
Requires:       perl(Config)
Requires:       perl(File::Spec)
Requires:       perl(Pod::Find)

Provides:       perl(Test::Pod::LinkCheck)
%description
This module looks for any links in your POD and verifies that they point to
a valid resource. It uses the Pod::Simple parser to analyze the pod files
and look at their links. In a nutshell, it looks for L<Foo> links and makes
sure that Foo exists. It also recognizes section links, L</SYNOPSIS> for
example. Also, manual pages are resolved and checked.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
# blib not used from the installed tests

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Pod-LinkCheck-%{version}
# Test::Apocalypse skips all tests as release tests, do not use it.
rm t/apocalypse.t
perl -i -ne 'print $_ unless m{^t/apocalypse\.t}' MANIFEST
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove tests which requires symlinked modules. Symlinks would pollute RPM
# dependencies.
rm %{buildroot}%{_libexecdir}/%{name}/t/00-compile.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc AUTHOR_PLEDGE Changes CommitLog examples README
%dir %{perl_vendorlib}/Test
%dir %{perl_vendorlib}/Test/Pod
%{perl_vendorlib}/Test/Pod/LinkCheck.pm
%{_mandir}/man3/Test::Pod::LinkCheck.*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
