%global source0_hash 033bab2fad4112b1a39400ae1e04e21f9633cdf060af2272fa4b6b9f258b1fef

Name:           perl-Alien-ZMQ
Version:        0.06
Release:        30%{?dist}
Summary:        Find and install libzmq library
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Alien-ZMQ
Source0:        https://cpan.metacpan.org/authors/id/C/CC/CCM/Alien-ZMQ-%{version}.tar.gz
# Tests do not need shellbang
Patch0:         Alien-ZMQ-0.06-Remove-useless-shellbang.patch
# Do not load modules unnecessary if libzmq is available
# <https://github.com/chazmcgarvey/p5-Alien-ZMQ/issues/4>
Patch1:         Alien-ZMQ-0.06-Load-less-modules-if-libzmq-is-available.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# Archive::Tar 1.00 not used
BuildRequires:  perl(base)
BuildRequires:  perl(Cwd)
# Digest::SHA not used
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.280205
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec::Functions)
# IPC::Run not used
BuildRequires:  perl(lib)
# LWP::Simple not used
BuildRequires:  perl(Module::Build) >= 0.40
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  zeromq-devel
# Run-time:
BuildRequires:  perl(String::ShellQuote)
# Tests:
# English not used
BuildRequires:  perl(Test::More)
# Pod::Coverage::TrustPod not used
# Test::Perl::Critic not used
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
Requires:       zeromq-devel

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

%check
unset RELEASE_TESTING
./Build test

%files
%license LICENSE
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
