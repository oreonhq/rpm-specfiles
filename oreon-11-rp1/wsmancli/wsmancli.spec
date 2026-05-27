%global source0_hash none

Name:           wsmancli
Version:        2.8.0
Release:        3%{?dist}
License:        BSD-3-Clause
Url:            http://www.openwsman.org/
# You can get this tarball here:
# https://github.com/Openwsman/wsmancli/archive/v%%{version}.tar.gz
Source:         wsmancli-%{version}.tar.gz
Source1:        COPYING
Source2:        README
Source3:        AUTHORS
BuildRequires: make
BuildRequires:  openwsman-devel >= 2.1.0 pkgconfig curl-devel
BuildRequires:  autoconf automake libtool
Requires:       openwsman curl
Patch0:         missing-pthread-symbols.patch
Summary:        WS-Management-Command line Interface

%description
Command line interface for managing 
systems using Web Services Management protocol.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q 
%autopatch -p1
cp -fp %SOURCE1 %SOURCE2 %SOURCE3 .;

%build
./bootstrap
%configure --disable-more-warnings 
make %{?_smp_flags}

%install
make DESTDIR=%{buildroot} install

%files
%{_bindir}/wsman
%{_bindir}/wseventmgr
%{_mandir}/man1/wsman*
%{_mandir}/man1/wseventmgr*
%doc COPYING README AUTHORS

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.0-3
- Import
