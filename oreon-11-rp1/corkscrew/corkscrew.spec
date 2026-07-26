%global source0_hash 0d0fcbb41cba4a81c4ab494459472086f377f9edb78a2e2238ed19b58956b0be

Summary:	Tool for tunneling SSH through HTTP proxies
Name:		corkscrew
Version:	2.0
Release:	42%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://freshmeat.sourceforge.net/projects/corkscrew
Source0:	http://www.agroman.net/corkscrew/%{name}-%{version}.tar.gz
Source1:	%{name}.1

Patch0:		%{name}-%{version}-from-debian.patch
Patch1:		%{name}-%{version}-typo.patch
Patch2:		%{name}-%{version}-configure-c99.patch

BuildRequires:	gcc
BuildRequires: make

%description
Corkscrew is a tool for tunneling SSH through HTTP proxies.

It has been tested with the following HTTP proxies :
 * Gauntlet
 * CacheFlow
 * JunkBuster
 * Apache mod_proxy

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%configure
%make_build

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
%make_install

# man page
install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc README
%doc TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
