%global source0_hash ec325d64241580ed136660f1d27cecd874b663431ac3abdb2d28e1ac6f4811e4

%global vmoddir %{_libdir}/varnish/vmods

Name:           vmod-querystring
Version:        2.0.3
Release:        12%{?dist}
Summary:        QueryString module for Varnish Cache
URL:            https://github.com/dridi/libvmod-querystring
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later

Source:         %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  python
BuildRequires:  varnish >= 6
BuildRequires:  pkgconfig(varnishapi) >= 6

Requires:       varnish >= 6

%description
The purpose of this module is to give you a fine-grained control over a URL's
query-string in Varnish Cache. It's possible to remove the query-string, clean
it, sort its parameters or filter it to only keep a subset of them.

This can greatly improve your hit ratio and efficiency with Varnish, because
by default two URLs with the same path but different query-strings are also
different. This is what the RFCs mandate but probably not what you usually
want for your web site or application.

A query-string is just a character string starting after a question mark in a
URL. But in a web context, it is usually a structured key/values store encoded
with the `application/x-www-form-urlencoded' media type. This module deals
with this kind of query-strings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure CFLAGS="%{optflags}"
%make_build

%install
%make_install
rm %{buildroot}%{vmoddir}/*.la

%check
%make_build check

%files
%license LICENSE
%{_mandir}/man?/*
%{_docdir}/*
%{vmoddir}/*.so

%changelog
%autochangelog
