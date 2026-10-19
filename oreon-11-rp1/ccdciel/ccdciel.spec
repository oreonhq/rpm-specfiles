%global source0_hash 7db5ee6fe5c9e817d5797f7c12d90ba1cf873b17cb8670937cd36579621f29dd
%global gittag v0.9.93
Name:           ccdciel
%if "%{?gittag}"
Version:        0.9.97
%else
Version:        0.9.79^%{date}%{shortcommit}
%endif
Release:        1%{?dist}
Summary:        CCD capture software
License:        GPL-3.0-or-later
URL:            http://www.ap-i.net/ccdciel/
%if "%{?gittag}"
Source0:        https://github.com/pchev/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
%else
Source0:        https://github.com/pchev/%{name}/archive/%{gittag}/%{name}-%{version}.tar.gz
%endif
Patch100:       ccdciel-0.9.90_no-strip.patch
ExclusiveArch:  %{fpc_arches}
ExcludeArch:    %{ix86}
Requires:       libpasastro%{?_isa}
Requires:       libpasraw%{?_isa}
Recommends:     astrometry, astrometry-tycho2
Recommends:     libindi
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  fpc
BuildRequires:  fpc-src
BuildRequires:  lazarus-lcl-nogui
BuildRequires:  lazarus-lcl-qt5
BuildRequires:  lazarus-tools
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  qt5pas-devel
# /oreon:deps
%description
CCDciel is a free CCD capture software intended for the amateur astronomer. 
It include all the features required to perform digital imaging 
CCD observation of celestial objects.
Using the standard drivers protocol INDI and ASCOM it can connect and control 
the CCD camera, the focuser, the filter wheel and the telescope mount.
It tightly integrates with Skychart to provide telescope control while
Indistarter can be used to control INDI server drivers

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation for %{name}.

%prep

%if "%{?gittag}"
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

# Make sure we don't use bundled libraries
rm -rf library/*

%build

./configure lazarus=%{_libdir}/lazarus prefix=%{_prefix}
make fpcopts="-O1 -gw3 -fPIC"
%install
make install PREFIX=%{buildroot}%{_prefix}
cp -p doc/doc_%{name}_en.pdf %{buildroot}%{_pkgdocdir}
%oreon_autofiles ccdciel-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/net.ap_i.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/net.ap_i.%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n ccdciel-doc -f %{oreon_filedir}/ccdciel-doc.list

%changelog

%autochangelog
