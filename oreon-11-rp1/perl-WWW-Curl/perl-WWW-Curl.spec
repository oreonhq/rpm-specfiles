%global source0_hash 52ffab110e32348d775f241c973eb56f96b08eedbc110d77d257cdb0a24ab7ba
Name:           perl-WWW-Curl
Version:        4.17
Release:        1%{?dist}
Summary:        Perl extension interface for libcurl
License:        MIT
URL:            https://metacpan.org/release/WWW-Curl
Source0:        https://cpan.metacpan.org/authors/id/S/SZ/SZBALINT/WWW-Curl-%{version}.tar.gz
Patch0:         WWW-Curl-4.17-Skip-preprocessor-symbol-only-CURL_STRICTER.patch
Patch1:         WWW-Curl-4.17-define-CURL-as-void.patch
Patch2:         WWW-Curl-4.17-Adapt-to-changes-in-cURL-7.69.0.patch
Patch3:         WWW-Curl-4.17-Adapt-to-curl-7.87.0.patch
Patch4:         WWW-Curl-4.17-Work-around-a-macro-bug-in-curl-7.87.0.patch
Patch5:         WWW-Curl-4.17-add-back-CURLOPT_RESOLV-support.patch
Patch6:         WWW-Curl-4.17-BRC2259537.patch
Patch7:         WWW-Curl-4.17-BRC2354525.patch
%{?_with_network_tests:BuildRequires:  perl(lib) }
%{?perl_default_filter}
# oreon:deps
BuildRequires:  findutils
BuildRequires:  libcurl-devel
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
