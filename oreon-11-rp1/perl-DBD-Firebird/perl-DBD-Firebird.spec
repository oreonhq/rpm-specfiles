%global source0_hash 235b36b81d9036879ea64d7b1d2f5f81b0c297013d6dc0714c2563dabd0a0214

# Filter the Perl extension module
%{?perl_default_filter}

%global pkgname DBD-Firebird

Summary:        Firebird interface for perl
Name:           perl-DBD-Firebird
Version:        1.39
Release:        4%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{pkgname}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAM/%{pkgname}-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  libfbclient2-devel >= 2.5.1
BuildRequires:  libicu-devel
BuildRequires:  gcc
%if 0%{?rhel} == 8
# https://github.com/mariuz/perl-dbd-firebird/issues/58
BuildRequires:  gcc-toolset-12
%endif
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI) >= 1.43
BuildRequires:  perl(DBI::DBD)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::BigFloat) >= 1.55
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::CheckDeps) >= 0.007
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
DBD::Firebird is a Perl module that works with the DBI module to provide
access to Firebird databases.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build
%if 0%{?rhel} == 8
. /opt/rh/gcc-toolset-12/enable
%endif

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*

%check
# Test for ib_set_tx_param() seems to be buggy (thus disable for now)
rm -f t/embed-62-timeout.t

# Disable thread-based test of ib_wait_event, as this test cannot be
# guaranteed to succeed with overloaded host, see:
# - https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=719582
# - https://bugzilla.redhat.com/show_bug.cgi?id=1228642
# - https://bugzilla.redhat.com/show_bug.cgi?id=1161469
export AUTOMATED_TESTING=1

# Full test coverage requires a live Firebird database (see the README file)
make test

%files
%doc Changes README
%{perl_vendorarch}/DBD/
%{perl_vendorarch}/auto/DBD/
%{_mandir}/man3/*.3*

%changelog
%autochangelog
