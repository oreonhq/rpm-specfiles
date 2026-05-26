Summary:	A tiny replacement for Module::Build
Name:		perl-Module-Build-Tiny
Version:	0.053
Release:	1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Module-Build-Tiny
Source0:	https://cpan.metacpan.org/authors/id/L/LE/LEONT/Module-Build-Tiny-0.053.tar.gz
# oreon url source checksums begin
%global source0_sha256 3726d622da6f655e88fdf89e4fd597709c44970b47de65082003e8d86b5e193a
%global source0_file Module-Build-Tiny-0.053.tar.gz
# oreon url source checksums end

BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
# Module
BuildRequires:	perl(CPAN::Meta)
BuildRequires:	perl(CPAN::Requirements::Dynamic)
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(ExtUtils::Config) >= 0.003
BuildRequires:	perl(ExtUtils::Helpers) >= 0.020
BuildRequires:	perl(ExtUtils::Install)
BuildRequires:	perl(ExtUtils::InstallPaths) >= 0.002
BuildRequires:	perl(ExtUtils::ParseXS)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Getopt::Long) >= 2.36
BuildRequires:	perl(JSON::PP) >= 2
BuildRequires:	perl(Pod::Man)
BuildRequires:	perl(TAP::Harness::Env)
# Test
BuildRequires:	perl(blib)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(IPC::Open2)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(XSLoader)
# Dependencies
Requires:	perl(CPAN::Requirements::Dynamic)
Requires:	perl(DynaLoader)
Requires:	perl(ExtUtils::CBuilder)
Requires:	perl(ExtUtils::ParseXS)
Requires:	perl(Pod::Man)
Requires:	perl(TAP::Harness::Env)

# ExtUtils::CBuilder in EL-8 has no dependency on gcc or c++ (#1547165)
# so pull them in ourselves
%if 0%{?el8}
BuildRequires:	gcc, gcc-c++
Requires:	gcc, gcc-c++
%endif

%description
Many Perl distributions use a Build.PL file instead of a Makefile.PL file to
drive distribution configuration, build, test and installation. Traditionally,
Build.PL uses Module::Build as the underlying build system. This module
provides a simple, lightweight, drop-in replacement.

Whereas Module::Build has over 6,700 lines of code; this module has less than
70, yet supports the features needed by most pure-Perl distributions.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Module-Build-Tiny-0.053.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3726d622da6f655e88fdf89e4fd597709c44970b47de65082003e8d86b5e193a" || { echo "oreon: Source0 SHA256 mismatch for Module-Build-Tiny-0.053.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Module-Build-Tiny-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test --verbose

%files
%license LICENSE
%doc Changes README Todo
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Build::Tiny.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.053-1
- Import
