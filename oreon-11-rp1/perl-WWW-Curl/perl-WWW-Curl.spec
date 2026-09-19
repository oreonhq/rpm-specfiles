%global source0_hash 52ffab110e32348d775f241c973eb56f96b08eedbc110d77d257cdb0a24ab7ba

Name:           perl-WWW-Curl
Version:        4.17
Release:        45%{?dist}
Summary:        Perl extension interface for libcurl
License:        MIT
URL:            https://metacpan.org/release/WWW-Curl
Source0:        https://cpan.metacpan.org/authors/id/S/SZ/SZBALINT/WWW-Curl-%{version}.tar.gz
Patch0:         WWW-Curl-4.17-Skip-preprocessor-symbol-only-CURL_STRICTER.patch
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=941915
Patch1:         WWW-Curl-4.17-define-CURL-as-void.patch
# Adapt to changes in cURL 7.69.0, bug #1812910, CPAN RT#132197
Patch2:         WWW-Curl-4.17-Adapt-to-changes-in-cURL-7.69.0.patch
# Adapt to changes in cURL 7.87.0, bug #2160057, CPAN RT#145992
Patch3:         WWW-Curl-4.17-Adapt-to-curl-7.87.0.patch
# Workound a bug in cURL 7.87.0, bug #2160057, CPAN RT#145992
Patch4:         WWW-Curl-4.17-Work-around-a-macro-bug-in-curl-7.87.0.patch
# Workound a bug in WWW::CURL 4.17, bug #2245689, GH #9
Patch5:         WWW-Curl-4.17-add-back-CURLOPT_RESOLV-support.patch
# Adapt to new version of gcc, bug #2259537
Patch6:         WWW-Curl-4.17-BRC2259537.patch
# Adapt to curl 8.13
Patch7:         WWW-Curl-4.17-BRC2354525.patch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Temp)
%{?_with_network_tests:BuildRequires:  perl(lib) }
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
# Test::Pod is optional
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
BuildRequires:  libcurl-devel

%{?perl_default_filter}

%description
WWW::Curl is a Perl extension interface for libcurl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n WWW-Curl-%{version}
rm -rf inc && sed -i -e '/^inc\//d' MANIFEST

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# These tests require network, use "--with network_tests" to execute them
%{?!_with_network_tests: rm t/01basic.t }
%{?!_with_network_tests: rm t/02callbacks.t }
%{?!_with_network_tests: rm t/04abort-test.t }
%{?!_with_network_tests: rm t/05progress.t }
%{?!_with_network_tests: rm t/08ssl.t }
%{?!_with_network_tests: rm t/09times.t }
%{?!_with_network_tests: rm t/14duphandle.t }
%{?!_with_network_tests: rm t/15duphandle-callback.t }
%{?!_with_network_tests: rm t/18twinhandles.t }
%{?!_with_network_tests: rm t/19multi.t }
%{?!_with_network_tests: rm t/21write-to-scalar.t }
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/WWW*
%{_mandir}/man3/*

%changelog
%autochangelog
