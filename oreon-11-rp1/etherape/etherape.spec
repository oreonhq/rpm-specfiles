%global source0_hash e94c5502b40a7b228c0aca6d31afdec9010bc7fd101ba648a6269c1015e7206b
Name:           etherape
Version:        0.9.22
Release:        1%{?dist}
Summary:        Graphical network monitor for Unix
License:        GPL-2.0-or-later
URL:            http://etherape.sourceforge.net/
Source0:        http://downloads.sourceforge.net/sourceforge/etherape/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnome-doc-utils
BuildRequires:  goocanvas2-devel
BuildRequires:  itstool
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  popt-devel
# /oreon:deps
%description
EtherApe is a graphical network monitor modeled after etherman. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

export CFLAGS="$CFLAGS -std=gnu17"
%configure
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/etherape.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
