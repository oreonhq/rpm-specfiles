%global source0_hash d7e688b5f0bd5d38e5bb306f16f904aac93112df8eda098fefef1c810bba6f85

Name:           perl-Proc-ProcessTable
Version:        0.636
Release:        9%{?dist}
Summary:        Perl extension to access the Unix process table
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Proc-ProcessTable
Source0:        https://cpan.metacpan.org/modules/by-module/Proc/Proc-ProcessTable-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
BuildRequires:  procps-ng
# Dependencies
Requires:       perl(File::Temp)
Requires:       perl(Storable)

# Avoid provides for private objects
%{?perl_default_filter}

Provides:       perl(Proc::ProcessTable)
%description
Perl interface to the Unix process table.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Proc-ProcessTable-%{version}

chmod -c 644 contrib/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README README.linux contrib/pswait
%{perl_vendorarch}/auto/Proc/
%{perl_vendorarch}/Proc/
%{_mandir}/man3/Proc::ProcessTable.3*
%{_mandir}/man3/Proc::Killall.3*
%{_mandir}/man3/Proc::Killfam.3*
%{_mandir}/man3/Proc::ProcessTable::Process.3*

%changelog
%autochangelog
