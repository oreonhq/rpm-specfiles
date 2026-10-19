%global source0_hash e3203a5d3e5d4c634374e229acdbbe03fea41e8ccdef6a594a3ea50a50d29705
Name:           xml2
Version:        0.5
Release:        33%{?dist}
Summary:        XML/Unix Processing Tools
License:        GPL-2.0-or-later
URL:            http://dan.egnor.name/xml2/
Source0:        http://download.ofb.net/gale/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  symlinks
# /oreon:deps
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
symlinks -c %{buildroot}%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
