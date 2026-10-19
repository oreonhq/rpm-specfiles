%global source0_hash 1fa8a6121dce297406f67adbcb4d92db01e9dd85781cb6ef710dc333bb9cfd56
Name:           perl-Log-Any
Version:        1.720
Release:        1%{?dist}
Summary:        Bringing loggers and listeners together
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Any
Source0:        https://cpan.metacpan.org/authors/id/P/PR/PREACTION/Log-Any-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(B)
Requires:       perl(Data::Dumper)
Obsoletes:      perl-Log-Any-Adapter < 0.11-7
Provides:       perl-Log-Any-Adapter = %{version}-%{release}%{?dist}
Provides:       perl(Log::Any)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mojo::Exception)
BuildRequires:  perl(Moose::Exception)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Throwable::Error)
BuildRequires:  perl(Unix::Syslog)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Log::Any allows CPAN modules to safely and efficiently log messages, while
letting the application choose (or decline to choose) a logging mechanism
such as Log::Dispatch or Log::Log4perl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Log-Any-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
