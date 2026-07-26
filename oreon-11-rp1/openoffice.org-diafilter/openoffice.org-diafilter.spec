%global source0_hash 0757f1c609981c3e4c48a0c9b7b5058ac15c4da546b70afc19e66325583cd779

%global instdir %{_libdir}
%global baseinstdir %{instdir}/libreoffice
%global sdkinstdir %{baseinstdir}/sdk

Name:          openoffice.org-diafilter
Version:       1.7.6
Release:       24%{?dist}
Summary:       DIA diagram shape importer and gallery extension for LibreOffice
License:       GPL-3.0-or-later AND LGPL-3.0-or-later
URL:           http://fedorahosted.org/openoffice.org-diafilter
Source:        https://github.com/caolanm/diafilter/archive/%{version}.tar.gz

BuildRequires: make
BuildRequires: libreoffice-sdk, boost-devel, dia, pkgconfig(zlib), zip, gcc-c++
Requires:      libreoffice-draw%{?_isa}

%if 0%{?fedora} >= 37
# Fedora 37 dropped java for i686, so libreoffice-sdk isn't there either
ExclusiveArch: %{java_arches}
%endif

Patch0: fixbuild.patch

%description
This package contains an importer component for LibreOffice to enable importing
the "dia" diagram and shape formats. A gallery of the standard set of "dia"
shapes are made available from Gallery for convenience.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n diafilter-%{version} -p1

%build
. %{sdkinstdir}/setsdkenv_unix.sh
DIA_SHAPES_DIR=%{_datadir}/dia/shapes make %{?_smp_mflags} OPT_FLAGS="$RPM_OPT_FLAGS"

%install
install -d -m 755 $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/diafilter.oxt $RPM_BUILD_ROOT/%{_datadir}/applications
unzip -q build/diafilter.oxt -d $RPM_BUILD_ROOT%{baseinstdir}/share/extensions/diafilter.oxt
install -p -m 644 openoffice.org-diafilter.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/openoffice.org-diafilter.desktop
install -d -m 755 $RPM_BUILD_ROOT/%{_datadir}/appdata
install -p -m 644 openoffice.org-diafilter.metainfo.xml $RPM_BUILD_ROOT/%{_datadir}/appdata

%files
%{baseinstdir}/share/extensions/diafilter.oxt
%{_datadir}/appdata/%{name}.metainfo.xml
%{_datadir}/applications/openoffice.org-diafilter.desktop
%doc README NEWS TODO
%license gpl-3.0.txt lgpl-3.0.txt

%changelog
%autochangelog
