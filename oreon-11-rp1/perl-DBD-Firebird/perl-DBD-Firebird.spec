%global source0_hash 235b36b81d9036879ea64d7b1d2f5f81b0c297013d6dc0714c2563dabd0a0214
%{?perl_default_filter}
%global pkgname DBD-Firebird
Summary:        Firebird interface for perl
Name:           perl-DBD-Firebird
Version:        1.39
Release:        4%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/%{pkgname}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAM/%{pkgname}-%{version}.tar.gz
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libfbclient2-devel
BuildRequires:  libicu-devel
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBI::DBD)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::CheckDeps)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DBD::Firebird is a Perl module that works with the DBI module to provide
access to Firebird databases.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build
%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

rm -f t/embed-62-timeout.t
export AUTOMATED_TESTING=1
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
