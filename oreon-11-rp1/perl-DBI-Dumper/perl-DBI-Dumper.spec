%global source0_hash 0cd21d1bad0fd84a176ef2fc923093cc85890513a6d2596493b07cec12b1fa76
Name:           perl-DBI-Dumper
Version:        2.01
Release:        62%{?dist}
Summary:        Dump data from a DBI datasource to file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBI-Dumper
Source0:        https://cpan.metacpan.org/authors/id/W/WS/WSMITH/DBI-Dumper-%{version}.tar.gz
Patch0:         DBI-Dumper-2.01-qw-does-not-produce-parentheses.patch
%{?perl_default_filter}
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}perl\\(Parse::RecDescent::DBI::Dumper::Grammar\\)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Dumps data from a select statement into an output file. dbidumper tries
to mirror the functionality and behavior of sql*loader. The control
file syntax is similar, and DBI::Dumper utilizes a subset of the
sql*loader options.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBI-Dumper-%{version}
%patch -P0 -p1

# include some licensing information from the rt.cpan.org bug, as it's
# not yet included in the package proper
cat << \EOF > COPYING.fedora
DBI::Dumper is under the same terms as perl itself, namely the GPL or 
Artistic licenses.  For more information, please see:

  http://rt.cpan.org/Public/Bug/Display.html?id=27269

From the bug:

Subject: RE: [rt.cpan.org #27269] DBI::Dumper license?
Date:    Thu, 24 May 2007 10:58:37 -0500
To:      <bug-DBI-Dumper[...]rt.cpan.org>
From:   "Smith Warren - wasmit" <Warren.Smith[...]acxiom.com>

The license for DBI::Dumper is the same as perl. I will update the
POD with the next release to include this information.

EOF

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
rm -rf %{buildroot}${PWD}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
