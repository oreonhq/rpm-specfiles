%global source0_hash c11dedd4548f478e4e7142b4162bf74ac9d0e67d71f2afc673d709a3ecdcd74d

Name:           perl-File-Type-WebImages
Version:        1.01
Release:        43%{?dist}
Summary:        Determine web image file types using magic
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Type-WebImages
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKSTOS/File-Type-WebImages-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)

%description
mime_type() can use either a filename, or file contents, to determine the
type of a file. The process involves looking the data at the beginning of
the file, sometimes called "magic numbers".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Type-WebImages-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
