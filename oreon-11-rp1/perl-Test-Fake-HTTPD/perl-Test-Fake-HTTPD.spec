%global source0_hash 14f79cb067a90922e9be554f8e4b39d3d69778ae4c8fff44f560f637fb6f2d1e

Name:           perl-Test-Fake-HTTPD
Version:        0.09
Release:        17%{?dist}
Summary:        Fake HTTP server module for testing
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Fake-HTTPD

Source0:        https://cpan.metacpan.org/authors/id/M/MA/MASAKI/Test-Fake-HTTPD-%{version}.tar.gz

# Adds SSL key and certification assignment
Patch0:         ssl-parameters-assignment.patch

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)

# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Daemon::SSL)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(Scalar::Util) >= 1.14
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(warnings)

# Testing
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::SharedFork) >= 0.29
BuildRequires:  perl(Test::UseAllModules)

Requires:       perl(HTTP::Daemon::SSL)

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

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
