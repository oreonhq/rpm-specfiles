%global source0_hash e1e2212efac068d62bc5e7a8104c4f1aeb97027f58cf37e4a8e589f9ea37eb9b

Name:           perl-Dist-Zilla-Plugin-Test-Compile
Version:        2.059
Release:        2%{?dist}
Summary:        Common tests to check syntax of your modules, only using core modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Dist-Zilla-Plugin-Test-Compile
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Dist-Zilla-Plugin-Test-Compile-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Data::Section) >= 0.004
BuildRequires:  perl(Dist::Zilla::Dist::Builder)
# XXX: BuildRequires:  perl(Dist::Zilla::File::InMemory)
BuildRequires:  perl(Dist::Zilla::Role::FileFinderUser)
BuildRequires:  perl(Dist::Zilla::Role::FileGatherer)
BuildRequires:  perl(Dist::Zilla::Role::FileMunger)
BuildRequires:  perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:  perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Sub::Exporter::ForMethods)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(File::pushd) >= 1.004
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::CoreList) >= 2.77
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Perl::PrereqScanner) >= 1.016
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::DZil)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings) >= 0.009
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
Requires:       perl(Dist::Zilla) >= 4.300039
Requires:       perl(Dist::Zilla::File::InMemory)
Requires:       perl(Dist::Zilla::Role::FileFinderUser)
Requires:       perl(Dist::Zilla::Role::FileGatherer)
Requires:       perl(Dist::Zilla::Role::FileMunger)
Requires:       perl(Dist::Zilla::Role::PrereqSource)
Requires:       perl(Dist::Zilla::Role::TextTemplate)

%description
This is a Dist::Zilla plugin that runs at the gather files stage, providing
a test file (configurable, defaulting to t/00-compile.t).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       make
Requires:       perl-Test-Harness
Requires:       perl(blib)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dist-Zilla-Plugin-Test-Compile-%{version}
# Help generators to recognize Perl scripts
for F in $(find t/ -name '*.t'); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
# File for 00-compile.t test
cp -a examples %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm -f %{buildroot}%{_libexecdir}/%{name}/t/00-report-*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENCE
%doc Changes AUTHOR_PLEDGE CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
