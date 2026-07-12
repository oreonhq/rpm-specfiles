%global source0_hash 77f997b74953dbdf63a750fcff4338d1bfacd89100e1fb27c3473f0a222a9a0c

Name:           perl-IO-Async
Version:        0.805
Release:        1%{?dist}
Summary:        A collection of modules that implement asynchronous filehandle IO

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Async
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Async-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::IO::ImplBase)
BuildRequires:  perl(Future::Utils) >= 0.18
BuildRequires:  perl(Heap::Elem)
BuildRequires:  perl(Heap::Fibonacci)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Poll)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Metrics::Any)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Sereal::Decoder)
BuildRequires:  perl(Sereal::Encoder)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Struct::Dumb)
BuildRequires:  perl(Test2::IPC)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Future::IO)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Future::IO::Impl)
BuildRequires:  perl(Test::MemoryGrowth)
BuildRequires:  perl(Test::Metrics::Any)
BuildRequires:  perl(lib)
Requires:       perl(threads)
# All five are optional but preferred
Requires:       perl(Heap::Elem)
Requires:       perl(Heap::Fibonacci)
Requires:       perl(IO::Socket::IP)
Requires:       perl(Sereal::Decoder)
Requires:       perl(Sereal::Encoder)

%{?perl_default_filter}

Provides:       perl(IO::Async)
Provides:       perl(IO::Async::Loop)
%description
A collection of modules that implement asynchronous filehandle IO

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n IO-Async-%{version}


%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build


%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test


%files
%doc Changes examples
%{perl_vendorlib}/Future/IO/Impl/IOAsync.pm
%{perl_vendorlib}/IO*
%{_mandir}/man3/Future::IO::Impl::IOAsync.3pm.gz
%{_mandir}/man3/IO*.3*


%changelog
%autochangelog
