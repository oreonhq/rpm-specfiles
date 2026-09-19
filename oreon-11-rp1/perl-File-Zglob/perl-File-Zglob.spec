%global source0_hash 1cb1edde20ac094ef003794bafef2c7624169cf8402c7367d9b7460f6c0e669b

Name:           perl-File-Zglob
Version:        0.11
Release:        29%{?dist}
Summary:        Provide extended Unix glob
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Zglob
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/File-Zglob-%{version}.tar.gz
Patch0:         File-Zglob-0.11-Disable-author-tests.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(utf8)
Requires:       perl(Data::Dumper)

%description
Provides a traditional Unix glob(3) functionality; returns a list of
pathnames that match the given pattern.

File::Zglob provides extended glob. It supports C<< **/*.pm >> form.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Zglob-%{version}
%patch -P0 -p1

# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

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
