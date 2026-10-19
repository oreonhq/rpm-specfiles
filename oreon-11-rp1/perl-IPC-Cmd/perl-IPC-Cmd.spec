%global source0_hash d110a0f60e35c65721454200f0d2f0f8965529a2add9649d1fa6f4f9eccb6430
%bcond_without perl_IPC_Cmd_enables_IPC_Run
Name:           perl-IPC-Cmd
Epoch:          2
Version:        1.04
Release:        1%{?dist}
Summary:        Finding and running system commands made easy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IPC-Cmd
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/IPC-Cmd-%{version}.tar.gz
Patch0:         IPC-Cmd-0.96-Replace-EU-MM-dependency-with-EU-MM-Utils.patch
BuildArch:      noarch
%if %{with perl_IPC_Cmd_enables_IPC_Run} && !%{defined perl_bootstrap}
%endif
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
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Load::Conditional\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Params::Check\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MM::Utils)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Params::Check)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-IPC-Cmd-tests -f %{oreon_filedir}/perl-IPC-Cmd-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.04-522
- Prepare for Oreon 11 (RP1)
