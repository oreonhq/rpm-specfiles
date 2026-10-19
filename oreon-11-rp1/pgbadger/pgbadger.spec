%global source0_hash 94074714bb4928c69c9e977da02d50e197a9d428fa3f235f25c103ef3c7d9a9d
Name:           pgbadger
Version:        13.2
Release:        1%{?dist}
Summary:        PostgreSQL log analyzer with fully detailed reports and graphs
License:        PostgreSQL AND MIT AND Artistic-2.0 AND OFL-1.1 AND CC-BY-3.0 AND GPL-2.0-only
URL:            https://github.com/darold/%{name}
Source0:        https://github.com/darold/%{name}/archive/refs/tags/v%{version}.tar.gz
Patch0:         %{name}-13.0-Update-Makefile.patch
BuildArch:      noarch
Requires:       perl(Text::CSV_XS)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-Pod-Checker
BuildRequires:  perl-Pod-Markdown
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
PgBadger is a PostgreSQL log analyzer built for speed providing fully 
detailed reports based on your PostgreSQL log files. It's a small 
standalone Perl script that outperforms any other PostgreSQL log analyzer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} %{buildroot}/%{_bindir}/pgbadger
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
