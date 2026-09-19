%global source0_hash be4a2594ef1a7577e773135add940179c6a324e07e12bcfdc463cb49119a2cb9

Name:           perl-File-SearchPath
Version:        0.07
Release:        32%{?dist}
Summary:        Search for a file in an environment variable path
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://metacpan.org/release/File-SearchPath
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJENNESS/File-SearchPath-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Env::Path)
BuildRequires:  perl(File::Spec) >= 0.8
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(Env::Path)
Requires:       perl(File::Spec) >= 0.8

%description
This module provides the ability to search a path-like environment variable
for a file (that does not necessarily have to be an executable).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-SearchPath-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc ChangeLog README
%{perl_vendorlib}/File*
%{_mandir}/man3/File*

%changelog
%autochangelog
