%global source6_hash 2631b5b39b6d1acc56de75235109b5af2dbb4b0ac5a127b6f06185977247fd4b
%global source0_hash ff59515375f1006dc5b6820734e553139be69c2abcd1c011dc81ea756c82cd85
Name:           natural-earth-map-data
Version:        5.1.2
Release:        1%{?dist}
Summary:        Free vector and raster map data at 1:10m, 1:50m, and 1:110m scales
License:        LicenseRef-Fedora-Public-Domain
URL:            https://www.naturalearthdata.com/
Source0:        110m_physical-%{version}.tar.xz
Source1:        110m_cultural-%{version}.tar.xz
Source2:        50m_physical-%{version}.tar.xz
Source3:        50m_cultural-%{version}.tar.xz
Source4:        10m_physical-%{version}.tar.xz
Source5:        10m_cultural-%{version}.tar.xz
Source6:        https://github.com/nvkelso/natural-earth-vector/raw/master/LICENSE.md
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%description

%package        110m
Summary:        Natural Earth map data - 110m resolution
%description    110m

This provides data at 1:110m resolution.

%package        50m
Summary:        Natural Earth map data - 50m resolution
%description    50m

This provides data at 1:50m resolution.

%package        10m
Summary:        Natural Earth map data - 10m resolution
%description    10m

This provides data at 1:10m resolution.

%package        all
Summary:        Natural Earth map data - all resolutions
Requires:       %{name}-110m
Requires:       %{name}-50m
Requires:       %{name}-10m
%description    all

This provides data at all resolutions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -T
for scale in 110m 50m 10m; do
    mkdir ${scale}
    for theme in physical cultural; do
        mkdir ${scale}/${theme}
    done
done
# 110m
tar -C 110m/physical -xf %SOURCE0
tar -C 110m/cultural -xf %SOURCE1
# 50m
tar -C 50m/physical -xf %SOURCE2
tar -C 50m/cultural -xf %SOURCE3
# 10m
tar -C 10m/physical -xf %SOURCE4
tar -C 10m/cultural -xf %SOURCE5
# One has to be different...
mv 10m/cultural/10m_cultural/* 10m/cultural
rmdir 10m/cultural/10m_cultural
cp -p %SOURCE6 .

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_pkgdocdir}
for theme in physical cultural; do
    mkdir -p %{buildroot}%{_datadir}/%{name}/${theme}
    for scale in 110m 50m 10m; do
        chmod -x ${scale}/${theme}/ne_${scale}_*
        cp -a ${scale}/${theme}/ne_${scale}_* %{buildroot}%{_datadir}/%{name}/${theme}
        for docfile in README.md CHANGELOG VERSION; do
            cp -a ${scale}/${theme}/${docfile} %{buildroot}%{_pkgdocdir}/${scale}-${theme}-${docfile}
        done
    done
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n natural-earth-map-data-110m -f %{oreon_filedir}/natural-earth-map-data-110m.list
%files -n natural-earth-map-data-50m -f %{oreon_filedir}/natural-earth-map-data-50m.list
%files -n natural-earth-map-data-10m -f %{oreon_filedir}/natural-earth-map-data-10m.list
%files -n natural-earth-map-data-all -f %{oreon_filedir}/natural-earth-map-data-all.list

%changelog

%autochangelog
