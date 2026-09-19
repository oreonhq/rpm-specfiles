%global source0_hash 9b26135e908a3ae50173741d1a2536f4dc90d0cc942ed4c2a43c048d15cd3a7f

Name:           perl-TheSchwartz
Version:        1.18
Release:        4%{?dist}
Summary:        Reliable job queue
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TheSchwartz
Source0:        https://cpan.metacpan.org/authors/id/A/AK/AKIYM/TheSchwartz-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::ObjectDriver::BaseObject)
BuildRequires:  perl(Data::ObjectDriver::Driver::DBI)
BuildRequires:  perl(Data::ObjectDriver::Errors)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Gearman::Client)
BuildRequires:  perl(Gearman::Worker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(JSON::Any)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Term::Cap)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
TheSchwartz is a reliable job queue system. Your application can put jobs
into the system and your worker processes can pull jobs from the queue
atomically to perform. Failed jobs can be left in the queue to retry later.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TheSchwartz-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes doc README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/schwartzmon

%changelog
%autochangelog
