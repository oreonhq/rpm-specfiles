%global source0_hash 9b8fe695f4798ded8d91bdfc437f1eb18a6026722d557f969531bcb20bf44ec1
%global srcname mechanize
%global sum Stateful programmatic web browsing
Name:           python-mechanize
Version:        0.4.10
Release:        1%{?dist}
Summary:        Stateful programmatic web browsing
License:        LicenseRef-Callaway-BSD OR ZPL-2.1
URL:            https://github.com/python-mechanize/
Source0:        https://github.com/python-mechanize/mechanize/archive/v%{version}.tar.gz
Patch:          https://github.com/python-mechanize/mechanize/commit/0c1cd4b65697dee4e4192902c9a2965d94700502.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-html5lib
BuildRequires:  python3-twisted
BuildRequires:  python3-zope-interface
# /oreon:deps
%description
Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

The library is layered: mechanize.Browser (stateful web browser),
mechanize.UserAgent (configurable URL opener), plus urllib2 handlers.

Features include: ftp:, http: and file: URL schemes, browser history,
high-level hyperlink and HTML form support, HTTP cookies, HTTP-EQUIV and
Refresh, Referer [sic] header, robots.txt, redirections, proxies, and
Basic and Digest HTTP authentication.  mechanize's response objects are
(lazily-) .seek()able and still work after .close().

Much of the code originally derived from Perl code by Gisle Aas
(libwww-perl), Johnny Lee (MSIE Cookie support) and last but not least
Andy Lester (WWW::Mechanize).  urllib2 was written by Jeremy Hylton.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
%description -n python3-%{srcname}
Stateful programmatic web browsing, after Andy Lester's Perl module
WWW::Mechanize.

The library is layered: mechanize.Browser (stateful web browser),
mechanize.UserAgent (configurable URL opener), plus urllib2 handlers.

Features include: ftp:, http: and file: URL schemes, browser history,
high-level hyperlink and HTML form support, HTTP cookies, HTTP-EQUIV and
Refresh, Referer [sic] header, robots.txt, redirections, proxies, and
Basic and Digest HTTP authentication.  mechanize's response objects are
(lazily-) .seek()able and still work after .close().

Much of the code originally derived from Perl code by Gisle Aas
(libwww-perl), Johnny Lee (MSIE Cookie support) and last but not least
Andy Lester (WWW::Mechanize).  urllib2 was written by Jeremy Hylton.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p 1
chmod -x examples/forms/{echo.cgi,example.py,simple.py}
# Workaround for https://github.com/rpm-software-management/rpm/issues/2532:
rm -rf SPECPARTS

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

chmod +x examples/forms/{echo.cgi,example.py,simple.py}
python3 run_tests.py
chmod -x examples/forms/{echo.cgi,example.py,simple.py}
%files -f %{oreon_filedir}/main.list
%files -n python3-mechanize -f %{oreon_filedir}/python3-mechanize.list

%changelog

%autochangelog
