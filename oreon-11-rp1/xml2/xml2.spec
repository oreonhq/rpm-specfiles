%global source0_hash e3203a5d3e5d4c634374e229acdbbe03fea41e8ccdef6a594a3ea50a50d29705

Name:           xml2
Version:        0.5
Release:        33%{?dist}
Summary:        XML/Unix Processing Tools
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://dan.egnor.name/xml2/
Source0:        http://download.ofb.net/gale/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  symlinks

%description
These tools are used to convert XML and HTML to and from a
line-oriented format more amenable to processing by classic Unix
pipeline processing tools, like grep, sed, awk, cut, shell scripts,
and so forth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# cleanup symlinks
symlinks -c %{buildroot}%{_bindir}

%files
%{_bindir}/2csv
%{_bindir}/2html
%{_bindir}/2xml
%{_bindir}/csv2
%{_bindir}/xml2
%{_bindir}/html2
%if 0%{?_licensedir:1}
%license COPYING
%else
%doc COPYING
%endif # licensedir

%changelog
%autochangelog
