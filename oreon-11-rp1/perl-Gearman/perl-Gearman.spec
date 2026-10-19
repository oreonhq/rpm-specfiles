%global source0_hash 7fb87634a5fac5c40ec221489e227b9e7b2e5f0897edada07e5a597ecb4053ec
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-Gearman
Version:        2.004.015
Release:        26%{?dist}
Summary:        Perl interface for Gearman distributed job system
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://danga.com/gearman/
Source0:        https://cpan.metacpan.org/authors/id/P/PA/PALIK/Gearman-%{version}.tar.gz
BuildArch:      noarch
%if !%{defined perl_bootstrap}
%endif
Requires:       perl(version) >= 0.77
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(version\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Net::EmptyPort)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(Proc::Guard)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(String::CRC32)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Test::Timer)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(fields)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-Gearman-Server
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Gearman provides a generic application framework to farm out work to other
machines or processes that are better suited to do the work. It allows you
to do work in parallel, to load balance processing, and to call functions
between languages. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Gearman-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset AUTHOR_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
