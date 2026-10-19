%global source0_hash 3d09756ea828e96bae5a3a435dce07387dc0223895af7861f6a5e75bdf42e8db
Name:           perl-File-ShareDir-ProjectDistDir
Version:        1.000009
Release:        1%{?dist}
Summary:        Simple set-and-forget using of a '/share' directory in your projects root
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-ShareDir-ProjectDistDir
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/File-ShareDir-ProjectDistDir-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(Path::Class::Dir)
Requires:       perl(Path::Tiny)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Path::FindDev)
BuildRequires:  perl(Path::IsDev)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Simple set-and-forget using of a '/share' directory in your projects root

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-ShareDir-ProjectDistDir-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
