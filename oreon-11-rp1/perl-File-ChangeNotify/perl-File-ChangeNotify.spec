%global source0_hash 192bdb1ce76266c6a694a8e962d039e3adeeb829b6ac1e23f5057f2b506392bd

Name:           perl-File-ChangeNotify
Summary:        Watch for changes to files, cross-platform style
Version:        0.31
Release:        21%{?dist}
License:        Artistic-2.0
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/File-ChangeNotify-%{version}.tar.gz 
URL:            https://metacpan.org/release/File-ChangeNotify
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
# XXX: BuildRequires:  perl(IO::KQueue)
BuildRequires:  perl(Linux::Inotify2) >= 1.2
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.006
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Standard)
# Tests only
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test2::V0)
# Optional tests only
BuildRequires:  perl(Test::Without::Module)

%description
Watch for changes to files, easily, cleanly, and across different platforms.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n File-ChangeNotify-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.md
%exclude %{perl_vendorlib}/File/ChangeNotify/Watcher/KQueue.pm
%{perl_vendorlib}/*
%exclude %{_mandir}/man3/File::ChangeNotify::Watcher::KQueue.3pm*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
