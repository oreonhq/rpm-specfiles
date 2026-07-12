%global source0_hash 4cd8a39318a380466d081b98955fdead61789c5b08d223585b1ca56cfdaf4472

Name:           perl-Mojolicious
Version:        9.47
Release:        1%{?dist}
Summary:        A next generation web framework for Perl
License:        Artistic-2.0

URL:            https://metacpan.org/dist/Mojolicious
Source0:        http://cpan.metacpan.org/authors/id/S/SR/SRI/Mojolicious-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.16.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
# EV 4.0 not used at tests
BuildRequires:  perl(experimental)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Poll)
BuildRequires:  perl(IO::Socket::IP) >= 0.37
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(JSON::PP) >= 2.27103
BuildRequires:  perl(List::Util) >= 1.41
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(re)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local) >= 1.2
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(utf8)
# Optional run-time:
BuildRequires:  perl(Role::Tiny) >= 2.000001
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(lib)
# Test::Future::AsyncAwait::Awaitable not used
Suggests:       perl(Cpanel::JSON::XS) >= 4.09
Requires:       perl(experimental)
Requires:       perl(FindBin)
# Future::AsyncAwait 0.36 not yet packaged
Requires:       perl(IO::Socket::IP) >= 0.37
Suggests:       perl(IO::Socket::Socks) >= 0.64
Suggests:       perl(IO::Socket::SSL) >= 2.009
Requires:       perl(JSON::PP) >= 2.27103
# Net::DNS::Native 0.15 not yet packaged
Suggests:       perl(Role::Tiny) >= 2.000001
Requires:       perl(Time::Local) >= 1.2

%{?perl_default_filter}
# EV is just one supported reactor backend, Mojo can use others, and
# ithreads-based code actually cannot use EV:
# http://mojolicio.us/perldoc/Mojolicious/Guides/FAQ#What-does-the-error-EV-does-not-work-with-ithreads-mean
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}perl\\(VMS|perl\\(Win32|perl\\(EV
# Remove under-specified dependencies
%global __requires_exclude %{__requires_exclude}|^perl\\((IO::Socket::IP|JSON::PP|Time::Local)\\)$

%package -n perl-Test-Mojo
Summary:        Test::Mojo perl Module

Provides:       perl(Mojo::Base)
Provides:       perl(Mojo::JSON)
Provides:       perl(Mojolicious)
Provides:       perl(Mojo::Exception)
%description -n perl-Test-Mojo
%{summary}

%description
Back in the early days of the web there was this wonderful Perl library
called CGI, many people only learned Perl because of it. It was simple
enough to get started without knowing much about the language and powerful
enough to keep you going, learning by doing was much fun. While most of the
techniques used are outdated now, the idea behind it is not. Mojolicious is
a new attempt at implementing this idea using state of the art technology.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Mojolicious-%{version}
mv README.md lib/Mojolicious/

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes examples
%{_bindir}/mojo
%{_bindir}/hypnotoad
%{_bindir}/morbo
%{perl_vendorlib}/*
%exclude %{perl_vendorlib}/Test
%{_mandir}/man1/*
%{_mandir}/man3/*

%files -n perl-Test-Mojo
%{perl_vendorlib}/Test

%changelog
%autochangelog
