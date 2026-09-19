%global source0_hash 5986aaaf5128d9c0f01b25a4d620d180c06fc9b9cee125cdd409a2826c13d7b9

Name:           perl-File-Edit-Portable
Version:        1.26
Release:        10%{?dist}
Summary:        Read and write files while keeping the original line-endings intact
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Edit-Portable

Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEVEB/File-Edit-Portable-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POSIX)

# Testing
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Tempdir)
BuildRequires:  perl(Mock::Sub) >= 1.06
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::CheckManifest)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08

%description
The default behavior of perl is to read and write files using the
Operating System's (OS) default record separator (line ending). If you open
a file on an OS where the record separators are that of another OS, things
can and do break.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Edit-Portable-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test AUTHOR_TESTING=1

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
