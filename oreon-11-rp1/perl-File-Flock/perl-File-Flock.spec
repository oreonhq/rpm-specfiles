%global source0_hash 5dc5d7890dbeb4f8261f1e47820492a238f56f38c793a8b453d06515f7f241d2

Name:           perl-File-Flock
Version:        2014.01
Release:        34%{?dist}
Summary:        File locking with flock
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/File-Flock
Source0:        https://cpan.metacpan.org/authors/id/M/MU/MUIR/modules/File-Flock-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Structure::Util)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Event) >= 0.812
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork)
Requires:       perl(IO::Event) >= 0.812

%{?perl_default_filter}

%description
Lock files using the flock() call. If the file to be locked does not exist,
then the file is created. If the file was created then it will be removed
when it is unlocked assuming it's still an empty file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-Flock-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset FLOCK_FORKING_USE
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
