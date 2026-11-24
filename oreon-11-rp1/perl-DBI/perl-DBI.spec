# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ab5f2b9aef00951ed4598723d6131a00b03e68193478dd5e5f211015520a6ef0
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if %{defined perl_bootstrap} || 0%{?rhel} >= 7 || 0%{?oreon}
%bcond_with perl_DBI_enables_coro
%else
%bcond_without perl_DBI_enables_coro
%endif

%if 0%{?rhel} || 0%{?oreon}
%bcond_with perl_DBI_enables_Clone
%bcond_with perl_DBI_enables_DB_File
%bcond_with perl_DBI_enables_MLDBM
%else
%bcond_without perl_DBI_enables_Clone
%bcond_without perl_DBI_enables_DB_File
%bcond_without perl_DBI_enables_MLDBM
%endif
%if %{defined perl_bootstrap} || 0%{?rhel} || 0%{?oreon}
%bcond_with perl_DBI_enables_SQL_Statement
%else
%bcond_without perl_DBI_enables_SQL_Statement
%endif

Name:           perl-DBI
Version:        1.656
Release:        1%{?dist}
Summary:        A database access API for perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://dbi.perl.org/
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/DBI-%{version}.tgz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(strict)
BuildRequires:  sed
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
%if %{with perl_DBI_enables_coro}
%endif
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Module::Load) >= 0.22
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(threads)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
%if %{with perl_DBI_enables_Clone}
BuildRequires:  perl(Clone) >= 0.34
%endif
%if %{with perl_DBI_enables_DB_File}
BuildRequires:  perl(DB_File)
%endif
%if %{with perl_DBI_enables_MLDBM}
BuildRequires:  perl(MLDBM)
%endif
%if %{with perl_DBI_enables_SQL_Statement}
BuildRequires:  perl(SQL::Statement) >= 1.402
%endif
BuildRequires:  perl(blib)
BuildRequires:  perl(B)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple) >= 0.96
%if %{with perl_DBI_enables_Clone}
Suggests:       perl(Clone) >= 0.34
%endif
%if %{with perl_DBI_enables_DB_File}
Suggests:       perl(DB_File)
%endif
Requires:       perl(bytes)
Requires:       perl(FileHandle)
Requires:       perl(Math::BigInt)
%if %{with perl_DBI_enables_MLDBM}
Suggests:       perl(MLDBM)
%endif
%if %{with perl_DBI_enables_SQL_Statement}
Suggests:       perl(SQL::Statement) >= 1.402
%endif

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(RPC::\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(DBI::db\\)
%global __requires_exclude %{__requires_exclude}|^perl\\(DBI::st\\)

%description 
DBI is a database access Application Programming Interface (API) for
the Perl Language. The DBI API Specification defines a set of
functions, variables and conventions that provide a consistent
database interface independent of the actual database being used.

%if %{with perl_DBI_enables_coro}
%package Coro
Summary:        Asynchronous DBD::Gofer stream transport using Coro

%description Coro
This is an experimental asynchronous DBD::Gofer stream transport for DBI
implemented on top of Coro. The BIG WIN from using Coro is that it enables
the use of existing DBI frameworks like DBIx::Class.
%endif

%package tests
Summary:        Tests for %{name}
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%if %{with perl_DBI_enables_Clone}
Requires:       perl(Clone) >= 0.34
%endif
%if %{with perl_DBI_enables_DB_File}
Requires:       perl(DB_File)
%endif
%if %{with perl_DBI_enables_MLDBM}
Requires:       perl(MLDBM)
%endif
%if %{with perl_DBI_enables_SQL_Statement}
Requires:       perl(SQL::Statement) >= 1.402
%endif

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_sha256
%autosetup -p1 -n DBI-%{version}
for F in lib/DBD/Gofer.pm; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" > "${F}.utf8"
    touch -r "$F" "${F}.utf8"
    mv "${F}.utf8" "$F"
done
for F in dbixs_rev.pl ex/corogofer.pl; do
    perl -MExtUtils::MakeMaker -e "ExtUtils::MM_Unix->fixin(q{$F})"
done
chmod 0644 ex/*
chmod 0755 dbixs_rev.pl
%if %{without perl_DBI_enables_coro}
rm lib/DBD/Gofer/Transport/corostream.pm
perl -i -ne 'print $_ unless m{^lib/DBD/Gofer/Transport/corostream.pm}' MANIFEST

%endif
for F in lib/Bundle/DBI.pm lib/DBD/Proxy.pm lib/DBI/ProxyServer.pm \
        dbiproxy.PL t/80proxy.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
perl -pi -e 's/"dbiproxy\$ext_pl",//' Makefile.PL
for F in lib/DBI/W32ODBC.pm lib/Win32/DBIODBC.pm; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done

for F in t/*.t t/*.pl; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!.*perl\b}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} '%{buildroot}'/*

mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
perl -i -ne 'print $_ unless m{^use.*blib/}' %{buildroot}%{_libexecdir}/%{name}/t/1*.t
perl -pi -e 's/\-Mblib=\$getcwd\/blib//' %{buildroot}%{_libexecdir}/%{name}/t/85gofer.t
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

%check
make test

%files
%doc CONTRIBUTING.md README.md SECURITY.md ex/perl_dbi_nulls_test.pl ex/profile.pl
%{_bindir}/dbipro*
%{_bindir}/dbilogstrip
%{perl_vendorarch}/*.p*
%{perl_vendorarch}/DBD/
%if %{with perl_DBI_enables_coro}
%exclude %{perl_vendorarch}/DBD/Gofer/Transport/corostream.pm
%endif
%{perl_vendorarch}/DBI/
%{perl_vendorarch}/auto/DBI/
%{_mandir}/man1/dbi*.1*
%{_mandir}/man3/DBD*.3*
%{_mandir}/man3/DBI*.3*

%if %{with perl_DBI_enables_coro}
%files Coro
%doc ex/corogofer.pl
%{perl_vendorarch}/DBD/Gofer/Transport/corostream.pm
%endif

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
