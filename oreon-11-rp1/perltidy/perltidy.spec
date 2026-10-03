%global source0_hash 104e3e5ee5c84524d5e50324d664c7859b1ac422ab97a3e7a248985a4b4f7f64

Name:		perltidy
Version:	20260826
Release:	1%{?dist}
Summary:	Tool for indenting and re-formatting Perl scripts
License:	GPL-2.0-or-later
URL:		http://perltidy.sourceforge.net/
# upstream host unreachable; tarball from Fedora lookaside cache
Source0:        https://src.fedoraproject.org/repo/pkgs/perltidy/Perl-Tidy-20260826.tar.gz/sha512/e7124c84dec11bfdd4fba49c5332af98a947b7107d6e852e0e4b2425bc1384fa4c17a903470cada1b5dde17f63f90cbc332f0d97a094926935535e7833d57b2d/Perl-Tidy-20260826.tar.gz



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

Provides:       perl(Perl::Tidy)
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
