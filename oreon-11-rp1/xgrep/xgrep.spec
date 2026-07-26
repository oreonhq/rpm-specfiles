%global source0_hash d788b9df192fbbb3f301e022a551e55e2822358cb32fd34059b270ce6671649a

Name:		xgrep
Version:	0.08
Release:	26%{?dist}
Summary:	A grep-like utility for XML files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.wohlberg.net/public/software/xml/xgrep/
Source0:	http://www.wohlberg.net/public/software/xml/xgrep/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	libxml2-devel, pcre-devel, imake

%description
XGrep provides facilities for searching content in XML files.  The
search is specified either as an XPath via the -x flag, or a custom
syntax including extended regular expressions via the -s flag.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make depend
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%doc README GPL ChangeLog NEWS
%{_bindir}/*
%{_mandir}/*/*

%changelog
%autochangelog
