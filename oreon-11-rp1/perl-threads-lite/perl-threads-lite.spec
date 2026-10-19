%global source0_hash fe021e7efa0dbb98f2b95f14ff17bbd6027019237ab7b939ea57e2a6e72cca57
Name:           perl-threads-lite
Version:        0.034
Release:        1%{?dist}
Summary:        Actor model threading for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/threads-lite
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/threads-lite-%{version}.tar.gz
Patch0:         threads-lite-0.034-Fix-building-in-ISO-C23.patch
ExcludeArch:    aarch64 ppc ppc64 ppc64le
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements threads for perl. One crucial difference with
threads.pm threads is that the threads are disconnected, except by message
queues. It thus facilitates a message passing style of multi-threading.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir threads-lite-%{version}
%oreon_prep
%build

perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
