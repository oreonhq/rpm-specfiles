%global source0_hash d6a326a8b1ffb19495dea4ff5a09ef138bf3562ab1b069d3fb7efbc77b9f6aca
%bcond perl_IPC_Run_enables_optional_test %{undefined rhel}
Name:           perl-IPC-Run
Version:        20260402.0
Release:        1%{?dist}
Summary:        Perl module for interacting with child processes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IPC-Run
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/IPC-Run-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_IPC_Run_enables_optional_test}
%endif
Requires:       perl(Data::Dumper)
Requires:       perl(File::Basename)
Requires:       perl(IO::Pty) >= 1.08
Provides:       perl(IPC::Run)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pty)
BuildRequires:  perl(IO::Tty)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
IPC::Run allows you run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are
both supported and may be mixed.

Various redirection operators reminiscent of those seen on common Unix
and DOS command lines are provided.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
