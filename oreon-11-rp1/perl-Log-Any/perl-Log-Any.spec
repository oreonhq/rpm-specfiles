%global source0_hash 1fa8a6121dce297406f67adbcb4d92db01e9dd85781cb6ef710dc333bb9cfd56

Name:           perl-Log-Any
Version:        1.720
Release:        1%{?dist}
Summary:        Bringing loggers and listeners together
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Log-Any
Source0:        https://cpan.metacpan.org/authors/id/P/PR/PREACTION/Log-Any-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(B)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Unix::Syslog)
# Tests only
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mojo::Exception)
BuildRequires:  perl(Moose::Exception)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Throwable::Error)
Requires:       perl(B)
Requires:       perl(Data::Dumper)

# Log::Any::Adapter* merged into Log::Any in 1.00
Obsoletes:      perl-Log-Any-Adapter < 0.11-7
Provides:       perl-Log-Any-Adapter = %{version}-%{release}%{?dist}

Provides:       perl(Log::Any)
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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Log/
%{_mandir}/man3/Log::Any*.3pm*

%changelog
%autochangelog
