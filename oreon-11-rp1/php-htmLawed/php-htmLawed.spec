%global source0_hash fa1f809ac99ddc48fbdddad2b2775ec53dfe728ad459f98f39d27d75205abaf6
%global libname    htmLawed
%global libversion 1242
Name:           php-%{libname}
Version:        1.2.4.2
Release:        1%{?dist}
Summary:        PHP code to purify and filter HTML
License:        LGPL-3.0-only AND GPL-2.0-or-later
URL:            http://www.bioinformatics.org/phplabware/internal_utilities/htmLawed/
Source0:        http://www.bioinformatics.org/phplabware/downloads/%{libname}%{libversion}.zip
BuildArch:      noarch
Requires:       php-ctype
Requires:       php-pcre
# oreon:deps

# /oreon:deps
%description
PHP code to purify and filter HTML

* make HTML markup in text secure and standard-compliant
* process text for use in HTML, XHTML or XML documents
* restrict HTML elements, attributes or URL protocols
  using black or white-lists
* balance tags, check element nesting, transform deprecated
  attributes and tags, make relative URLs absolute, etc.
* fast, highly customizable, well-documented
* single, 48 kb file
* simple HTML Tidy alternative
* free and licensed under LGPL v3 and GPL v2+
* use to filter, secure and sanitize HTML in blog comments or
  forum posts, generate XML-compatible feed items from web-page
  excerpts, convert HTML to XHTML, pretty-print HTML, scrape
  web-pages, reduce spam, remove XSS code, etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

chmod -x *

%build

%install
install -d %{buildroot}%{_datadir}/php/%{libname}
install -pm 0644 %{libname}.php %{buildroot}%{_datadir}/php/%{libname}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
