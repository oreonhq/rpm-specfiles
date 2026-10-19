%global source0_hash bdccba1fa8e4c1cf3189c5e5a3529a6693a648aa5282b597538c7aaddce6d9c9
Name:           perl-CDDB_get
Version:        2.28
Release:        1%{?dist}
Summary:        Read the CDDB entry for an audio CD in your drive
License:        GPL-2.0-only
URL:            https://metacpan.org/release/CDDB_get
Source0:        https://cpan.metacpan.org/authors/id/F/FO/FONKIE/CDDB_get-%{version}.tar.gz
Patch0:         CDDB_get-2.28-Do-not-include-current-directory.patch
Patch1:         CDDB_get-2.28-cddb.pl-is-not-a-library.patch
BuildArch:      noarch
Requires:       perl(DBI)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::More)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module/script gets the CDDB data for an audio CD. You need a CD-ROM drive
and an active Internet connection in order to do that.

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir CDDB_get-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} "$RPM_BUILD_ROOT"/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I .
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-CDDB_get-tests -f %{oreon_filedir}/perl-CDDB_get-tests.list

%changelog

%autochangelog
