%global source0_hash bcb4d8c2d280c8034b82591cc0b9eb67a004f90ce9aa05979fc6071307acb195

# Use File::Which for locating the pager executables
%bcond_without perl_IO_Pager_enables_File_Which
# Use Text::Wrap for wrapping the long lines
%bcond_without perl_IO_Pager_enables_wrap

Name:           perl-IO-Pager
Version:        2.10
Release:        15%{?dist}
Summary:        Select a pager and pipe text to it if destination is a TTY
# The license is something home-made or "the same terms as Perl itself".
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Pager
Source0:        https://cpan.metacpan.org/authors/id/J/JP/JPIERCE/IO-Pager-%{version}.tgz
# Do not use /usr/local/bin for executing perl
Patch0:         IO-Pager-1.02-perl-is-in-usr-bin.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.8
# B not used at tests
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
# Data::Dumper not used at tests
BuildRequires:  perl(Env)
BuildRequires:  perl(File::Spec)
# Getopt::Long not used at tests
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(overload)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(SelectSaver)
BuildRequires:  perl(strict)
BuildRequires:  perl(Symbol)
# Term::Cap not used at tests
# Term::ReadKey not used at tests
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(warnings)
# Optional run-time:
%if %{with perl_IO_Pager_enables_File_Which}
BuildRequires:  perl(File::Which)
%endif
# POSIX not used at tests
# Text::Wrap not used at tests
# Win32::Console::ANSI not used on Linux
# Tests:
BuildRequires:  perl(bignum)
BuildRequires:  perl(blib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
# Optional tests:
# PerlIO::Util not used
Requires:       perl(Data::Dumper)
%if %{with perl_IO_Pager_enables_File_Which}
Recommends:     perl(File::Which)
%endif
Requires:       perl(IO::Handle)
Recommends:     perl(POSIX)
%if %{with perl_IO_Pager_enables_wrap}
Recommends:     perl(Text::Wrap)
%endif

%description
IO::Pager is used to locate an available pager and programmatically decide
whether or not to pipe a file handle's output to the pager.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n IO-Pager-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
# Deduplicate tp script
rm $RPM_BUILD_ROOT%{perl_vendorlib}/IO/Pager/tp
ln -s %{_bindir}/tp $RPM_BUILD_ROOT%{perl_vendorlib}/IO/Pager/tp

%check
unset TPOPT
make test

%files
%doc CHANGES README TODO
%{_bindir}/tp
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
