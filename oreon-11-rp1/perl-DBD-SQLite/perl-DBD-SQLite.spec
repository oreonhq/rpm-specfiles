%global source0_hash efbad7794bafaa4e7476c07445a33bbfe1040e380baa3395a02635eebe3859d5
%bcond_without perl_DBD_SQLite_enables_optional_test
Name:           perl-DBD-SQLite
Version:        1.78
Release:        2%{?dist}
Summary:        SQLite DBI Driver
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/DBD-SQLite
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/DBD-SQLite-%{version}.tar.gz
Patch0:         perl-DBD-SQLite-bz543982.patch
Patch1:         DBD-SQLite-1.62-Remove-bundled-source-extentions.patch
Patch2:         DBD-SQLite-1.64-Unbundle-Test-FailWarnings.patch
%if %{with perl_DBD_SQLite_enables_optional_test}
%endif
%{?perl_default_filter}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{_libexecdir}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(SQLiteTest\\)
Provides:       perl(DBD::SQLite)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBI::DBD)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Unicode::UCD)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sqlite-devel
# /oreon:deps
%description
SQLite is a public domain, file-based, relational database engine that you can
find at <https://www.sqlite.org/>. This package provides a Perl DBI driver for
SQLite.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DBD-SQLite-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
# Remove bundled sqlite libraries (BZ#1059154)
# System libraries will be used
rm sqlite*
perl -i -ne 'print $_ unless m{^sqlite}' MANIFEST
# Remove bundled modules
rm -rf inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
# Handle optional tests
%if !%{with perl_DBD_SQLite_enables_optional_test}
rm t/virtual_table/21_perldata_charinfo.t
perl -i -ne 'print $_ unless m{^t/virtual_table/21_perldata_charinfo\.t}' MANIFEST
%endif

# Help generators to recognize Perl scripts
for F in `find t -name *.t`; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build

CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build} OPTIMIZE="%{optflags}"
%install
%{make_install}
find %{buildroot} -type f  -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test
%files -f %{oreon_filedir}/main.list
%files -n perl-DBD-SQLite-tests -f %{oreon_filedir}/perl-DBD-SQLite-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.78-2
- Prepare for Oreon 11 (RP1)
