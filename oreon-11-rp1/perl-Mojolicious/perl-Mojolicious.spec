%global source0_hash 4cd8a39318a380466d081b98955fdead61789c5b08d223585b1ca56cfdaf4472
Name:           perl-Mojolicious
Version:        9.47
Release:        1%{?dist}
Summary:        A next generation web framework for Perl
License:        Artistic-2.0
URL:            https://metacpan.org/dist/Mojolicious
Source0:        http://cpan.metacpan.org/authors/id/S/SR/SRI/Mojolicious-%{version}.tar.gz
BuildArch:      noarch
Suggests:       perl(Cpanel::JSON::XS) >= 4.09
Requires:       perl(experimental)
Requires:       perl(FindBin)
Requires:       perl(IO::Socket::IP) >= 0.37
Suggests:       perl(IO::Socket::Socks) >= 0.64
Suggests:       perl(IO::Socket::SSL) >= 2.009
Requires:       perl(JSON::PP) >= 2.27103
Suggests:       perl(Role::Tiny) >= 2.000001
Requires:       perl(Time::Local) >= 1.2
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}perl\\(VMS|perl\\(Win32|perl\\(EV
%global __requires_exclude %{__requires_exclude}|^perl\\((IO::Socket::IP|JSON::PP|Time::Local)\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Hash::Util::FieldHash)
BuildRequires:  perl(IO::Compress::Gzip)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Poll)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(integer)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles perl-Test-Mojo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Mojo -f %{oreon_filedir}/perl-Test-Mojo.list

%changelog

%autochangelog
