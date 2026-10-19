%global source0_hash 2bfe771173c38b69eeb089504e3f76511b8e45e6a9e6dac3e616e400ea67bcf0
Name:           perl-Test-Pod-LinkCheck
Version:        0.008
Release:        1%{?dist}
Summary:        Tests POD for invalid links
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Pod-LinkCheck
Source0:        https://cpan.metacpan.org/authors/id/A/AP/APOCAL/Test-Pod-LinkCheck-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(App::PodLinkCheck::ParseSections)
Requires:       perl(Capture::Tiny)
Requires:       perl(Config)
Requires:       perl(File::Spec)
Requires:       perl(Pod::Find)
Provides:       perl(Test::Pod::LinkCheck)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(App::PodLinkCheck::ParseLinks)
BuildRequires:  perl(App::PodLinkCheck::ParseSections)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Pod::Find)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm %{buildroot}%{_libexecdir}/%{name}/t/00-compile.t
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
unset AUTHOR_TESTING
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

unset AUTHOR_TESTING
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Pod-LinkCheck-tests -f %{oreon_filedir}/perl-Test-Pod-LinkCheck-tests.list

%changelog

%autochangelog
