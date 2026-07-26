%global source0_hash 9278f9ef668850d913d98fa4c0d7e7d667cff3503391f4a4eae73a246f2e7916

Name:           perl-PerlIO-via-Timeout
Version:        0.32
Release:        31%{?dist}
Summary:        PerlIO layer that adds read & write timeout to a handle
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PerlIO-via-Timeout
Source0:        https://cpan.metacpan.org/modules/by-module/PerlIO/PerlIO-via-Timeout-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Build::Tiny) >= 0.039
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::TCP)
# Dependencies
Requires:       perl(Exporter) >= 5.57

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Exporter\\)$

%description
This package implements a PerlIO layer, that adds read / write timeout.
This can be useful to avoid blocking while accessing a handle (file,
socket, ...), and fail after some time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PerlIO-via-Timeout-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README README.pod
%{perl_vendorlib}/PerlIO/
%{_mandir}/man3/PerlIO::via::Timeout.3*

%changelog
%autochangelog
