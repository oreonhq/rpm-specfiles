%global source0_hash 56a1fc2f1f813e49026a0f284b9209a6b2824620993e7598c85b01c444ff0f64

Name:		perltidy
Version:	20260204
Release:	1%{?dist}
Summary:	Tool for indenting and re-formatting Perl scripts
License:	GPL-2.0-or-later
URL:		http://perltidy.sourceforge.net/
Source0:	https://cpan.metacpan.org/authors/id/S/SH/SHANCOCK/Perl-Tidy-20260204.tar.gz

BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Digest::MD5)
BuildRequires:	perl(Encode)
BuildRequires:	perl(English)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Pod::Simple::XHTML)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(utf8)
# Dependencies
Requires:	perl(File::Spec)
Requires:	perl(File::Temp)
Requires:	perl(HTML::Entities)
Requires:	perl(Pod::Simple::XHTML)
Provides:	perl-Perl-Tidy = %{version}-%{release}

%description
Perltidy is a Perl script that indents and re-formats Perl scripts to
make them easier to read. If you write Perl scripts, or spend much
time reading them, you will probably find it useful. The formatting
can be controlled with command line parameters. The default parameter
settings approximately follow the suggestions in the Perl Style Guide.
Perltidy can also output HTML of both POD and source code. Besides
re-formatting scripts, Perltidy can be a great help in tracking down
errors with missing or extra braces, parentheses, and square brackets
because it is very good at localizing errors.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Perl-Tidy-%{version}

# Don't need Windows batch file
rm examples/pt.bat

# Quieten complaints about missing files
sed -i -e '/^examples\/pt\.bat/d' MANIFEST

# Remove unwanted exec permissions
find examples/ lib/ -type f -perm /a+x -exec chmod -c -x {} \;

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYING
%doc BUGS.md CHANGES.md docs/ examples/ README.md SECURITY.md
%{_bindir}/perltidy
%{perl_vendorlib}/Perl/
%{_mandir}/man1/perltidy.1*
%{_mandir}/man3/Perl::Tidy.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 20260204-1
- Import
