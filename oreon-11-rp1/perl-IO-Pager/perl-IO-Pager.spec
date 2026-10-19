%global source0_hash bcb4d8c2d280c8034b82591cc0b9eb67a004f90ce9aa05979fc6071307acb195
%bcond_without perl_IO_Pager_enables_File_Which
%bcond_without perl_IO_Pager_enables_wrap
Name:           perl-IO-Pager
Version:        2.10
Release:        15%{?dist}
Summary:        Select a pager and pipe text to it if destination is a TTY
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Pager
Source0:        https://cpan.metacpan.org/authors/id/J/JP/JPIERCE/IO-Pager-%{version}.tgz
Patch0:         IO-Pager-1.02-perl-is-in-usr-bin.patch
BuildArch:      noarch
%if %{with perl_IO_Pager_enables_File_Which}
%endif
Requires:       perl(Data::Dumper)
%if %{with perl_IO_Pager_enables_File_Which}
Recommends:     perl(File::Which)
%endif
Requires:       perl(IO::Handle)
Recommends:     perl(POSIX)
%if %{with perl_IO_Pager_enables_wrap}
Recommends:     perl(Text::Wrap)
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(PerlIO)
BuildRequires:  perl(SelectSaver)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(base)
BuildRequires:  perl(bignum)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
rm $RPM_BUILD_ROOT%{perl_vendorlib}/IO/Pager/tp
ln -s %{_bindir}/tp $RPM_BUILD_ROOT%{perl_vendorlib}/IO/Pager/tp
%oreon_autofiles main

%check

unset TPOPT
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
