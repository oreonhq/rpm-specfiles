%global source0_hash 4ba70088566a92f846f1bc41bd841a2ca2cefd4805be4f8bd5029c3be91269f8

Name:           perl-Parse-Gitignore
Version:        1.0
Release:        4%{?dist}
Summary:        Parse a .gitignore file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parse-Gitignore

Source0:        https://cpan.metacpan.org/authors/id/B/BK/BKB/Parse-Gitignore-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Slurper) >= 0.010
BuildRequires:  perl(File::Spec) >= 3.40

# Testing
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More) >= 0.88

Requires:       perl(File::Spec) >= 3.40

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}perl\\(File::Spec\\)$

%description
Parse a .gitignore file and check whether a file matches it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parse-Gitignore-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
