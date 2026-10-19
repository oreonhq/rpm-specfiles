%global source0_hash d6e8f4b55ebd38e0bb45e44392e3fa27dc1fde16abc5d1ff53e157e19a5755be
Name:           perl-File-Share
Version:        0.27
Release:        1%{?dist}
Summary:        Extend File::ShareDir to local libraries
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Share
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/File-Share-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::ShareDir) >= 1.03
Requires:       perl(warnings)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::ShareDir\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is a drop-in replacement for File::ShareDir. It supports the
dist_dir and dist_file functions, except these functions have been enhanced
to understand when the developer's local ./share/ directory should be used.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Share-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
