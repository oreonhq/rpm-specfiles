%global source0_hash fe021e7efa0dbb98f2b95f14ff17bbd6027019237ab7b939ea57e2a6e72cca57

Name:           perl-threads-lite
Version:        0.034
Release:        40%{?dist}
Summary:        Actor model threading for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/threads-lite
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/threads-lite-%{version}.tar.gz
# Adapt to GCC 15, bug #2341042, in upstream after 0.034,
# <https://github.com/Leont/threads-lite/pull/3>
Patch0:         threads-lite-0.034-Fix-building-in-ISO-C23.patch
# Tests halt on these platforms, bug #719874, CPAN RT#69354
ExcludeArch:    aarch64 ppc ppc64 ppc64le
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental) >= 0.003
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(feature)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable) >= 2.05
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)

%{?perl_default_filter}

%description
This module implements threads for perl. One crucial difference with
threads.pm threads is that the threads are disconnected, except by message
queues. It thus facilitates a message passing style of multi-threading.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n threads-lite-%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes examples README
%dir %{perl_vendorarch}/auto/threads
%{perl_vendorarch}/auto/threads/lite
%dir %{perl_vendorarch}/threads
%{perl_vendorarch}/threads/lite
%{perl_vendorarch}/threads/lite.pm
%{_mandir}/man3/threads::lite.*
%{_mandir}/man3/threads::lite::*

%changelog
%autochangelog
