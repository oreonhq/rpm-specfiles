%global source0_hash 0b9c5cfdc5e215f94a8191c99d1325e74279d41320ac8e0fee910ea18b50bb1e
Name:           perl-ZMQ-LibZMQ4
Version:        0.01
Release:        32%{?dist}
Summary:        Libzmq 4.x wrapper for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ZMQ-LibZMQ4
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MOSCONI/ZMQ-LibZMQ4-%{version}.tar.gz
Patch0:         ZMQ-LibZMQ4-0.01-Fix-building-on-Perl-without-.-in-INC.patch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Alien::ZMQ)
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Install::AuthorTests)
BuildRequires:  perl(Module::Install::CheckLib)
BuildRequires:  perl(Module::Install::Makefile)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(Module::Install::XSUtil)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Proc::Guard)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(ZMQ::Constants)
BuildRequires:  perl(base)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
The ZMQ::LibZMQ4 module is a wrapper of the fourth version of ØMQ message
passing library for Perl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ZMQ-LibZMQ4-%{version}
%patch -P0 -p1
# Remove bundled modules, keep inc directory to skip xt tests
rm -r inc/*
sed -i -e '/%inc\//d' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
