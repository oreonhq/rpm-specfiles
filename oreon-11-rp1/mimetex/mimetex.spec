%global source0_hash 97ed9bb0d5c778b706b00a530bc6b134d27879ca9823cf339abcc808b7627f38

Name:           mimetex
Version:        1.74
Release:        29%{?dist}
Summary:        Easily embed LaTeX math in web pages
License:        GPL-2.0-or-later
URL:            http://www.forkosh.com/mimetex.html
Source0:        http://www.forkosh.com/%{name}.zip
Requires:       webserver

BuildRequires:  gcc
%description
MimeTeX lets you easily embed LaTeX math in your html pages. It parses a LaTeX
math expression and immediately emits the corresponding gif image, rather than
the usual TeX dvi. And mimeTeX is an entirely separate little program that
doesn't use TeX or its fonts in any way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build
gcc %{optflags} -std=gnu17 -DAA mimetex.c gifsave.c -lm -o mimetex.cgi

%install
install -pDm755 mimetex.cgi %{buildroot}%{_localstatedir}/www/cgi-bin/%{name}.cgi
install -pDm644 mimetex.html %{buildroot}%{_localstatedir}/www/html/%{name}.html

%files
%doc COPYING README
%{_localstatedir}/www/cgi-bin/%{name}.cgi
%{_localstatedir}/www/html/%{name}.html

%changelog
%autochangelog
