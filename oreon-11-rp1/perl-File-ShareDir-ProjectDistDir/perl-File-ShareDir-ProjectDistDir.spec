%global source0_hash 3d09756ea828e96bae5a3a435dce07387dc0223895af7861f6a5e75bdf42e8db

Name:           perl-File-ShareDir-ProjectDistDir
Version:        1.000009
Release:        26%{?dist}
Summary:        Simple set-and-forget using of a '/share' directory in your projects root
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-ShareDir-ProjectDistDir
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/File-ShareDir-ProjectDistDir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter >= 0:5.006
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(Path::FindDev)
BuildRequires:  perl(Path::IsDev)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(utf8)
# Tests
BuildRequires:  perl(Capture::Tiny) >= 0.12
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)
Requires:       perl(Path::Class::Dir)
Requires:       perl(Path::Tiny)

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
