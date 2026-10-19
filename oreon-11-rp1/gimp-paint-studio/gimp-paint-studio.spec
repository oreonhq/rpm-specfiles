%global source0_hash e0a4b568446ec2218784cde0055bd9517a1d1025681e02aa649f1d11b2f60e8e
Name:			gimp-paint-studio
Version:		2.0
Release:        1%{?dist}
Summary:        A collection of tool option presets and brushes for GIMP
License:		CC-BY-SA-3.0 AND GPL-2.0-only
URL:			https://code.google.com/p/gps-%{name}/
Source0:        https://gps-%{name}.googlecode.com/files/GPS_2_0.tar.gz
Source1:		%{name}.metainfo.xml
Patch0:                 gps-2.0-rateRange.patch
Patch1:                 gps-2.0-replaceBlends.patch
BuildArch:              noarch
Requires:               gimp >= 2.10
# oreon:deps
BuildRequires:  fdupes
# /oreon:deps
%description
GIMP Paint Studio(GPS) is a collection of brushes and accompanying tool
presets. Tool presets are a simply saved tool options, highly useful feature of
the GIMP. The goal of GPS is to provide an adequate working environment for
graphic designers and artists to begin to paint and feel comfortable with GIMP
from their first use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{_datadir}/gimp/3.0
rm -rf %{_builddir}/%{name}-%{version}/patterns/GPS-Pat/*.xcf
fdupes -rdN %{_builddir}/%{name}-%{version}/patterns/GPS-Pat/
cp -pr %{_builddir}/%{name}-%{version}/brushes \
                %{_builddir}/%{name}-%{version}/dynamics \
                %{_builddir}/%{name}-%{version}/gradients \
                %{_builddir}/%{name}-%{version}/splashes\
                %{_builddir}/%{name}-%{version}/palettes \
                %{_builddir}/%{name}-%{version}/patterns \
                %{_builddir}/%{name}-%{version}/tool-presets \
                %{buildroot}%{_datadir}/gimp/3.0
install -Dm 0644 -p %{SOURCE1} \
                %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
