%global source0_hash 41894e5b1d0ab53258fb67ddd6b2cecf418c6bc02033c42e8160cc658faad5b7
Name:		xgrep
Version:	0.08
Release:        1%{?dist}
Summary:        A grep-like utility for XML files
License:	GPL-2.0-or-later
URL:		http://www.wohlberg.net/public/software/xml/xgrep/
Source0:        http://www.wohlberg.net/public/software/xml/xgrep/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  imake
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  pcre-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
