%global source0_hash 3726d622da6f655e88fdf89e4fd597709c44970b47de65082003e8d86b5e193a
Summary:        A tiny replacement for Module::Build
Name:		perl-Module-Build-Tiny
Version:	0.053
Release:        1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Module-Build-Tiny
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-Build-Tiny-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(CPAN::Requirements::Dynamic)
Requires:	perl(DynaLoader)
Requires:	perl(ExtUtils::CBuilder)
Requires:	perl(ExtUtils::ParseXS)
Requires:	perl(Pod::Man)
Requires:	perl(TAP::Harness::Env)
%if 0%{?el8}
Requires:	gcc, gcc-c++
%endif
Provides:       perl(Module::Build::Tiny)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Requirements::Dynamic)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::Config)
BuildRequires:  perl(ExtUtils::Helpers)
BuildRequires:  perl(ExtUtils::Install)
BuildRequires:  perl(ExtUtils::InstallPaths)
BuildRequires:  perl(ExtUtils::ParseXS)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(TAP::Harness::Env)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(blib)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Many Perl distributions use a Build.PL file instead of a Makefile.PL file to
drive distribution configuration, build, test and installation. Traditionally,
Build.PL uses Module::Build as the underlying build system. This module
provides a simple, lightweight, drop-in replacement.

Whereas Module::Build has over 6,700 lines of code; this module has less than
70, yet supports the features needed by most pure-Perl distributions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Build-Tiny-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test --verbose
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.053-1
- Import
