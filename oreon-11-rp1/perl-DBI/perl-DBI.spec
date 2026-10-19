%global source0_hash 735a42a82e5a866b57869f8b92bf218f58c7fb62f75d6707a6345142d152762f
%bcond_without perl_DBI_enables_coro
%bcond_without perl_DBI_enables_Clone
%bcond_without perl_DBI_enables_DB_File
%bcond_without perl_DBI_enables_MLDBM
%bcond_without perl_DBI_enables_SQL_Statement
Name:           perl-DBI
Version:        1.655
Release:        1%{?dist}
Summary:        A database access API for perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://dbi.perl.org/
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/DBI-%{version}.tgz
%if %{with perl_DBI_enables_coro}
%endif
%if %{with perl_DBI_enables_Clone}
%endif
%if %{with perl_DBI_enables_DB_File}
%endif
%if %{with perl_DBI_enables_MLDBM}
%endif
%if %{with perl_DBI_enables_SQL_Statement}
%endif
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
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MLDBM)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(SQL::Statement)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(UNIVERSAL)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n DBI-%{version}
for F in lib/DBD/Gofer.pm; do
    iconv -f ISO-8859-1 -t UTF-8 < "$F" > "${F}.utf8"
    touch -r "$F" "${F}.utf8"
    mv "${F}.utf8" "$F"
done
# Fix shell bangs
for F in dbixs_rev.pl ex/corogofer.pl; do
    perl -MExtUtils::MakeMaker -e "ExtUtils::MM_Unix->fixin(q{$F})"
done
chmod 0644 ex/*
chmod 0755 dbixs_rev.pl
%if %{without perl_DBI_enables_coro}
rm lib/DBD/Gofer/Transport/corostream.pm
perl -i -ne 'print $_ unless m{^lib/DBD/Gofer/Transport/corostream.pm}' MANIFEST

%endif
# Remove RPC::Pl* reverse dependencies due to security concerns,
# CVE-2013-7284, bug #1051110
for F in lib/Bundle/DBI.pm lib/DBD/Proxy.pm lib/DBI/ProxyServer.pm \
        dbiproxy.PL t/80proxy.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done
perl -pi -e 's/"dbiproxy\$ext_pl",//' Makefile.PL
# Remove Win32 specific files to avoid unwanted dependencies
for F in lib/DBI/W32ODBC.pm lib/Win32/DBIODBC.pm; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
done

# Help generators to recognize Perl scripts
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-DBI-Coro -f %{oreon_filedir}/perl-DBI-Coro.list
%files -n perl-DBI-tests -f %{oreon_filedir}/perl-DBI-tests.list

%changelog

%autochangelog
