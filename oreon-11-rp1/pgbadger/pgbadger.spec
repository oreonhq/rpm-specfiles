%global source0_hash 9658ff222ed7b387d3cb76c3e3d90d1862b885c13b26aa9ff652e133f5d018f1

Name:           pgbadger
Version:        13.1
Release:        %autorelease
Summary:        PostgreSQL log analyzer with fully detailed reports and graphs

# List of all licenses - each with an example of a file that uses it
# PostgreSQL: pgbadger
# MIT: resources/jqplot
# Artistic-2.0: pgbadger
# OFL-1.1: resources/fontawesome.css
# CC-BY-3.0: /resources/jqplot.canvasTextRenderer.js
# GPL-2.0-only: resources/jqplot.*
License:        PostgreSQL AND MIT AND Artistic-2.0 AND OFL-1.1 AND CC-BY-3.0 AND GPL-2.0-only
URL:            https://github.com/darold/%{name}
Source:         https://github.com/darold/%{name}/archive/refs/tags/v%{version}.tar.gz

# Update Makefile.PL to not ignore command line arguments
Patch0:         %{name}-13.0-Update-Makefile.patch

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(constant)
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
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Text::CSV)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

# podchecker
BuildRequires:  perl-Pod-Checker
# pod2markdown
BuildRequires:  perl-Pod-Markdown

Requires:       perl(Text::CSV_XS)

%description
PgBadger is a PostgreSQL log analyzer built for speed providing fully 
detailed reports based on your PostgreSQL log files. It's a small 
standalone Perl script that outperforms any other PostgreSQL log analyzer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/%{_bindir}/pgbadger

%check
make test

%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1p.*

%changelog
%autochangelog
