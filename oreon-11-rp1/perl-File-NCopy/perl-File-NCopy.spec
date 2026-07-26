%global source0_hash f983a7a85bbfc1fb5ad852c16c5aa5ccf2af3623e864c4a9090a986f94b38f65

Name:           perl-File-NCopy
Version:        0.36
Release:        49%{?dist}
Summary:        Copy files to directories, or a single file to another file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-NCopy
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/File-NCopy-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  %{__make}
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(vars)

BuildArch: noarch

%description
File::NCopy copies files to directories, or a single file to another
file. The functionality is very similar to cp.

Deprecated module. Use only if required by other module.
You can use File::Copy::Recursive instead.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-NCopy-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*

%changelog
%autochangelog
