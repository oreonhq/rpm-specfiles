%global source0_hash c047e5bfac1bb05ff31b207f2b2510fcaca4f11e134a915db046248b01f4e5e5

Name:           perl-File-FindLib
Version:        0.001004
Release:        33%{?dist}
Summary:        Find and use a file/directory from a directory above your script file
License:        Unlicense
URL:            https://metacpan.org/release/File-FindLib
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-FindLib-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(blib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(lib)

%description
File::FindLib starts in the directory where your script (or library) is
located and looks for the file or directory whose name you pass in. If it
isn't found, then FindLib looks in the parent directory and continues
moving up parent directories until it finds it or until there is not
another parent directory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-FindLib-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
