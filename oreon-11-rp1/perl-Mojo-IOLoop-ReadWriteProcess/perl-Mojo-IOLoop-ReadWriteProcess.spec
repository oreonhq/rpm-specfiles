%global source0_hash 4624d1780eec223228872c4f13ae55d1a8979def0c52decda6b18503706898b8

Name:           perl-Mojo-IOLoop-ReadWriteProcess
Version:        1.1.0
Release:        3%{?dist}
Summary:        Execute external programs or internal code blocks as separate process
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Mojo-IOLoop-ReadWriteProcess/
Source0:        https://cpan.metacpan.org/authors/id/O/OK/OKURZ/Mojo-IOLoop-ReadWriteProcess-%{version}.tar.gz

BuildArch:      noarch
# Build requirements
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run requirements
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::SysV)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Collection)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::IOLoop::Stream)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
# Test requirements
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(lib)
BuildRequires:  perl(utf8)
# needed for /usr/bin/pgrep
BuildRequires:  procps-ng

Requires:       perl(Mojo::EventEmitter)

%{?perl_default_filter}

%description
Mojo::IOLoop::ReadWriteProcess is yet another process manager.
It executes external programs or internal code blocks as separate process

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n Mojo-IOLoop-ReadWriteProcess-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Mojo*
%{_mandir}/man3/Mojo*

%changelog
%autochangelog
