# Perform optional tests
%bcond perl_IPC_Run_enables_optional_test %{undefined rhel}

Name:           perl-IPC-Run
Version:        20250809.0
Release:        2%{?dist}
Summary:        Perl module for interacting with child processes
# the rest:                     GPL+ or Artistic
# The Win32* modules are not part of the binary RPM package
# lib/IPC/Run/Win32Helper.pm:   GPLv2 or Artistic
# lib/IPC/Run/Win32Pump.pm:     GPLv2 or Artistic
# lib/IPC/Run/Win32IO.pm:       GPLv2 or Artistic
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IPC-Run
Source0:        https://cpan.metacpan.org/authors/id/N/NJ/NJM/IPC-Run-20250809.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 b1e85a30405786ed8378b68dd57159315ad7ddc0a55e432aa9eeca6166ca53fe
%global source0_file IPC-Run-20250809.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  sed
# IO::Pty not needed strictly for build script
# Run-time:
# base not used on Linux
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pty) >= 1.08
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
# Socket not used on Linux
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
# Text::ParseWords not used on Linux
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Win32::Process not used on Linux
# Win32API::File not used on Linux
# Tests:
# B not used on Linux
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Tty)
BuildRequires:  perl(Test::More) >= 0.47
%if %{with perl_IPC_Run_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Readonly)
%endif
# Dependencies
Requires:       perl(Data::Dumper)
Requires:       perl(File::Basename)
Requires:       perl(IO::Pty) >= 1.08

%description
IPC::Run allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed.

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/IPC-Run-20250809.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b1e85a30405786ed8378b68dd57159315ad7ddc0a55e432aa9eeca6166ca53fe" || { echo "oreon: Source0 SHA256 mismatch for IPC-Run-20250809.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n IPC-Run-%{version}

# Remove Windows-only features that could add unnecessary dependencies
rm -f lib/IPC/Run/Win32*
sed -i -e '/^lib\/IPC\/Run\/Win32.*/d' MANIFEST
rm -f t/win32_*
sed -i -e '/^t\/win32_.*/d' MANIFEST

# Handle optional tests
%if !%{with perl_IPC_Run_enables_optional_test}
rm t/readonly.t
sed -i -e '/^t/readonly\.t/d' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changelog eg/ README.md
%{perl_vendorlib}/IPC/
%{_mandir}/man3/IPC::Run.3*
%{_mandir}/man3/IPC::Run::Debug.3*
%{_mandir}/man3/IPC::Run::IO.3*
%{_mandir}/man3/IPC::Run::Timer.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20250809.0-2
- Prepare for Oreon 11 (RP1)
