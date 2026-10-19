%global source0_hash 0757f1c609981c3e4c48a0c9b7b5058ac15c4da546b70afc19e66325583cd779
%global instdir %{_libdir}
%global baseinstdir %{instdir}/libreoffice
%global sdkinstdir %{baseinstdir}/sdk
Name:          openoffice.org-diafilter
Version:       1.7.6
Release:        1%{?dist}
Summary:        DIA diagram shape importer and gallery extension for LibreOffice
License:       GPL-3.0-or-later AND LGPL-3.0-or-later
URL:           http://fedorahosted.org/openoffice.org-diafilter
Source0:        https://github.com/caolanm/diafilter/archive/%{version}.tar.gz
Requires:      libreoffice-draw%{?_isa}
Patch0: fixbuild.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  dia
BuildRequires:  gcc-c++
BuildRequires:  libreoffice-sdk
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)
BuildRequires:  zip
# /oreon:deps
%description
This package contains an importer component for LibreOffice to enable importing
the "dia" diagram and shape formats. A gallery of the standard set of "dia"
shapes are made available from Gallery for convenience.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir diafilter-%{version}
%oreon_prep
%build

. %{sdkinstdir}/setsdkenv_unix.sh
DIA_SHAPES_DIR=%{_datadir}/dia/shapes make %{?_smp_mflags} OPT_FLAGS="$RPM_OPT_FLAGS"
%install
install -d -m 755 $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/diafilter.oxt $RPM_BUILD_ROOT/%{_datadir}/applications
unzip -q build/diafilter.oxt -d $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/diafilter.oxt
install -p -m 644 openoffice.org-diafilter.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/openoffice.org-diafilter.desktop
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/appdata
install -p -m 644 openoffice.org-diafilter.metainfo.xml $RPM_BUILD_ROOT/%{_datadir}/appdata
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
