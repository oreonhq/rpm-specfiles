%global source0_hash 14f79cb067a90922e9be554f8e4b39d3d69778ae4c8fff44f560f637fb6f2d1e
Name:           perl-Test-Fake-HTTPD
Version:        0.09
Release:        1%{?dist}
Summary:        Fake HTTP server module for testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Fake-HTTPD
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MASAKI/Test-Fake-HTTPD-%{version}.tar.gz
Patch0:         ssl-parameters-assignment.patch
BuildArch:      noarch
Requires:       perl(HTTP::Daemon::SSL)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Daemon::SSL)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Test::UseAllModules)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::Fake::HTTPD is a fake HTTP server module for testing.
Written by NAKAGAWA Masaki <masaki@cpan.org>.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Fake-HTTPD-%{version}
%patch -P0 -p0

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
