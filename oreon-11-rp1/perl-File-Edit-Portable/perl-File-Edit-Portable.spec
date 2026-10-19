%global source0_hash 5986aaaf5128d9c0f01b25a4d620d180c06fc9b9cee125cdd409a2826c13d7b9
Name:           perl-File-Edit-Portable
Version:        1.26
Release:        1%{?dist}
Summary:        Read and write files while keeping the original line-endings intact
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/File-Edit-Portable
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEVEB/File-Edit-Portable-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Tempdir)
BuildRequires:  perl(Mock::Sub)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::CheckManifest)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test AUTHOR_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
