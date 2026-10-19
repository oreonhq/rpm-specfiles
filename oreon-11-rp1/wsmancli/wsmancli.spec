%global source0_hash dae475b4545dd2f17d101d5af94a98f5e08db829d1528fdcc2eec7c1ff12d789
Name:           wsmancli
Version:        2.8.0
Release:        1%{?dist}
License:        BSD-3-Clause
Url:            http://www.openwsman.org/
Source0:        https://github.com/Openwsman/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        COPYING
Source2:        README
Source3:        AUTHORS
Requires:       openwsman curl
Patch0:         missing-pthread-symbols.patch
Summary:        WS-Management-Command line Interface
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openwsman-devel
BuildRequires:  pkgconfig
# /oreon:deps
%description
Command line interface for managing 
systems using Web Services Management protocol.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q 
%autopatch -p1
cp -fp %SOURCE1 %SOURCE2 %SOURCE3 .;

%build

./bootstrap
%configure --disable-more-warnings 
make %{?_smp_flags}
%install
make DESTDIR=%{buildroot} install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.0-3
- Import
