%global source0_hash 3bdde6010784607903eae5376e13a2bf04ca021a59c5e9fff7ecb9cd461350c1

Summary:       Converting bibTeX file to HTML
Name:          bib2html
Version:       1.2.1
Release:       44%{?dist}
License:       GPL-1.0-or-later
URL:           http://www.litech.org/~wkiri/bib2html/
Source0:       http://www.litech.org/~wkiri/bib2html/bib2html-%{version}.tar.gz
Patch0:        bib2html-configure-c99.patch
Patch1:        bib2html-c99.patch
BuildRequires: gcc
BuildRequires: flex
BuildRequires: make
%description
bib2html is a utility for converting a bibTeX file into HTML
format. It will recognize the 'url' field in the bibTeX entries and
make appropriate links in the HTML output to the URL location.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Avoid re-running flex and bison after patching the sources and
# generated files.
touch -r bib2html.l bib2html.c
touch -r bib2html.tab.y bib2html.tab.c

chmod 0644 ChangeLog NEWS README Docs/bib2html.html

%build

%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%license COPYING
%doc COPYING README AUTHORS NEWS ChangeLog Docs/bib2html.html
%{_bindir}/bib2html

%changelog
%autochangelog
