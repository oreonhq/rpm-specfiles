%global source0_hash 38e3294ae9ffd015625d7746a0803cc329de92fb0f0edae9a29cd8232cf458d3

Name:           perl-Command-Runner
Version:        0.201
Release:        3%{?dist}
Summary:        Run external commands and Perl code references
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Command-Runner
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKAJI/Command-Runner-%{version}.tar.gz
# Update Command::Runner::Quote to not load Win32::ShellQuote on
# non-MSWin32 systems
Patch0:         Command-Runner-0.100-Dont-load-Win32-ShellQuote.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Time::HiRes)
# Tests
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(String::ShellQuote)

%description
This module runs external commands and Perl code references.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Command-Runner-%{version}
%patch -P0 -p1
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
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
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/Command
%{_mandir}/man3/Command::Runner*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
