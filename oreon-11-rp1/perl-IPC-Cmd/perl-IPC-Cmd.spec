%global source0_hash d110a0f60e35c65721454200f0d2f0f8965529a2add9649d1fa6f4f9eccb6430

# Use IPC::Run
%bcond_without perl_IPC_Cmd_enables_IPC_Run

Name:           perl-IPC-Cmd
# Epoch to compete with perl.spec
Epoch:          2
Version:        1.04
Release:        522%{?dist}
Summary:        Finding and running system commands made easy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IPC-Cmd
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/IPC-Cmd-%{version}.tar.gz
# Replace ExtUtils::MakeMaker dependency with ExtUtils::MM::Utils.
# This enables not to require perl-devel. Bug #1129443
Patch0:         IPC-Cmd-0.96-Replace-EU-MM-dependency-with-EU-MM-Utils.patch
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MM::Utils)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
%if %{with perl_IPC_Cmd_enables_IPC_Run} && !%{defined perl_bootstrap}
BuildRequires:  perl(IPC::Run) >= 0.55
%endif
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Load::Conditional) >= 0.66
BuildRequires:  perl(Params::Check) >= 0.20
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Tests:
# output.pl/IO::Handle not used
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Dependencies:
Requires:       perl(ExtUtils::MM::Utils)
Requires:       perl(FileHandle)
Requires:       perl(IO::Handle)
Requires:       perl(IO::Select)
Requires:       perl(IPC::Open3)
%if %{with perl_IPC_Cmd_enables_IPC_Run}
Suggests:       perl(IPC::Run) >= 0.55
%endif
Requires:       perl(Module::Load::Conditional) >= 0.66
Requires:       perl(Params::Check) >= 0.20
Requires:       perl(POSIX)
Requires:       perl(Socket)
Requires:       perl(Time::HiRes)

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Load::Conditional\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Check\\)$

%description
IPC::Cmd allows you to run commands platform independently, interactively
if desired, but have them still work.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n IPC-Cmd-%{version}
%patch -P0 -p1

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
%{_fixperms} %{buildroot}

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
%doc CHANGES README
%{perl_vendorlib}/IPC/
%{_mandir}/man3/IPC::Cmd.3*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.04-522
- Prepare for Oreon 11 (RP1)
