%global source0_hash 024e827bbc882f5cb10eb511006fe8f87ef0340eb05b7d99079a0705391e8561
%bcond do_tests 0
%bcond debug_tests 0
%bcond network_tests 0
Name:           perl-WWW-Mechanize-Chrome
Version:        0.75
Release:        1%{?dist}
Summary:        Automate the Chrome browser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/WWW-Mechanize-Chrome
Source0:        WWW-Mechanize-Chrome-%{version}-nocopyright.tar.gz
Source1:        WWW-Mechanize-Chrome-generate-tarball.sh
BuildArch:      noarch
%if %{with do_tests}
%endif
Requires:       perl(Cwd)
Requires:       perl(HTTP::Cookies)
Requires:       perl(Imager)
Requires:       perl(Log::Log4perl)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Future)
BuildRequires:  perl(Future::HTTP)
BuildRequires:  perl(HTML::Selector::XPath)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Image::Info)
BuildRequires:  perl(Imager)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::Role::EventEmitter)
BuildRequires:  perl(Net::Async::WebSocket::Client)
BuildRequires:  perl(Object::Import)
BuildRequires:  perl(PerlX::Maybe)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::HTTP::LocalServer)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(URI::ws)
BuildRequires:  perl(WWW::Mechanize::Link)
BuildRequires:  perl(experimental)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Like WWW::Mechanize, this module automates web browsing with a Perl object.
Fetching and rendering of web pages is delegated to the Chrome (or
Chromium) browser by starting an instance of the browser and controlling it
with Chrome DevTools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Mechanize-Chrome-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%if %{without do_tests}
exit 0
%endif
export CHROME_BIN=%{_bindir}/chromium-browser
unset \
    DISPLAY \
    WWW_MECHANIZE_CHROME_ARGS \
    WWW_MECHANIZE_CHROME_TRANSPORT \
    WWW_MECHANIZE_CHROME_CONNECTION_STYLE \
    TEST_LOG_LEVEL \
    TEST_WWW_MECHANIZE_CHROME_INSTANCE \
    TEST_WWW_MECHANIZE_CHROME_VERSIONS
%if %{with debug_tests}
export TEST_LOG_LEVEL=debug
%endif
%if %{without network_tests}
for tst in \
    t/50-mech-content-nonhtml.t \
    t/62-networkstatus.t \
    ; do
        echo 'use Test::More skip_all => "no network access"' > $tst
done
%endif
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
