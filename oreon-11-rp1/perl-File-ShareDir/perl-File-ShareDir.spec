%global source0_hash 3bb2a20ba35df958dc0a4f2306fc05d903d8b8c4de3c8beefce17739d281c958
%bcond_without perl_File_ShareDir_enables_optional_deps
Name:           perl-File-ShareDir
Version:        1.118
Release:        1%{?dist}
Summary:        Locate per-dist and per-module shared files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-ShareDir
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-ShareDir-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_File_ShareDir_enables_optional_deps}
%endif
Requires:       perl(Class::Inspector) >= 1.12
%if %{with perl_File_ShareDir_enables_optional_deps}
Recommends:     perl(List::MoreUtils) >= 0.428
Recommends:     perl(Params::Util) >= 1.07
%endif
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude}|perl\\(Class::Inspector\\)$
Provides:       perl(File::ShareDir)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The intent of File::ShareDir is to provide a companion to Class::Inspector
and File::HomeDir, modules that take a process that is well-known by
advanced Perl developers but gets a little tricky, and make it more
available to the larger Perl community.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n File-ShareDir-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
chmod 644 share/sample.txt
chmod 644 share/subdir/sample.txt
rm -rf %{buildroot}/blib/lib/auto/share/dist/File-ShareDir/
rm -rf %{buildroot}/blib/lib/auto/share/module/File-ShareDir/test_file.txt
%oreon_autofiles main

%check

make test AUTOMATED_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.118-15
- Prepare for Oreon 11 (RP1)
