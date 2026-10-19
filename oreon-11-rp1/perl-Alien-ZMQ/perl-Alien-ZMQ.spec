%global source0_hash 033bab2fad4112b1a39400ae1e04e21f9633cdf060af2272fa4b6b9f258b1fef
Name:           perl-Alien-ZMQ
Version:        0.06
Release:        1%{?dist}
Summary:        Find and install libzmq library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-ZMQ
Source0:        https://cpan.metacpan.org/authors/id/C/CC/CCM/Alien-ZMQ-%{version}.tar.gz
Patch0:         Alien-ZMQ-0.06-Remove-useless-shellbang.patch
Patch1:         Alien-ZMQ-0.06-Load-less-modules-if-libzmq-is-available.patch
BuildArch:      noarch
Requires:       zeromq-devel
# oreon:deps
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(String::ShellQuote)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  zeromq-devel
# /oreon:deps
%description
Upon installation, the target system is guaranteed for the present of libzmq.
In short, Perl modules that need libzmq can depend on Alien::ZMQ module to
make sure that it is available.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Alien-ZMQ-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

unset RELEASE_TESTING
./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
