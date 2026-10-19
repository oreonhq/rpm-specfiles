%global source0_hash e1ec4c0b8bac451490f60ddb21b6e4849db49febb681e1cb04737e2d2731e5ad
%global         _hardened_build 1
Name:           perl-Time-Moment
Version:        0.46
Release:        1%{?dist}
Summary:        Represents a date and time of day with an offset from UTC
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Callaway-BSD
URL:            https://metacpan.org/release/Time-Moment
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHANSEN/Time-Moment-%{version}.tar.gz
Provides:       bundled(c-dt)
Requires:       perl(Exporter)
Requires:       perl(XSLoader) >= 0.02
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(CBOR::XS)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MM_Unix)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Params::Coerce)
BuildRequires:  perl(Pod::Text)
BuildRequires:  perl(Sereal)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Number::Delta)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Time::Moment is an immutable object representing a date and time of day
with an offset from UTC in the ISO 8601 calendar system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Time-Moment-%{version}

%build

export CFLAGS="%{optflags} -Wl,-z,relro -Wl,-z,now"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,now -Wl,--as-needed"
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$CFLAGS"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*
chmod a-x -c eg/*.pl
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
