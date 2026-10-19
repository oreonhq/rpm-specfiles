%global source0_hash 3298b3dd95605bdda0c5fce5594c9bedde6aa63d89b216d5c83c6c092b6d375a
Name:           R-fontBitstreamVera
Version:        %R_rpm_version 0.1.1
Release:        1%{?dist}
Summary:        Fonts with 'Bitstream Vera Fonts' License
License:        Bitstream-Vera
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=fontBitstreamVera&version=%{version}#/fontBitstreamVera_%{version}.tar.gz
BuildArch:      noarch
Requires:       bitstream-vera-fonts-all
# oreon:deps
BuildRequires:  R-devel
BuildRequires:  bitstream-vera-fonts-all
# /oreon:deps
%description
Provides fonts licensed under the 'Bitstream Vera Fonts' license for the
'fontquiver' package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
# Ensure we are replacing fonts by the same system fonts later.
grep ttf fontBitstreamVera/MD5 | grep -v 'Mo\|Se' | sed -e 's!*inst!/usr/share!' -e 's!-fonts!-sans-fonts!' | md5sum -c
grep ttf fontBitstreamVera/MD5 | grep 'Mo' | sed -e 's!*inst!/usr/share!' -e 's!-fonts!-sans-mono-fonts!' | md5sum -c
grep ttf fontBitstreamVera/MD5 | grep 'Se' | sed -e 's!*inst!/usr/share!' -e 's!-fonts!-serif-fonts!' | md5sum -c
# We don't provide woffs.
rm fontBitstreamVera/inst/fonts/bitstream-vera-fonts/*.woff
sed -i -e '/woff/d' fontBitstreamVera/MD5
# Remove bunfled Bitstream files that are not important for this package.
rm fontBitstreamVera/inst/fonts/{bitstream-vera-VERSION,Makefile}
rm fontBitstreamVera/inst/fonts/bitstream-vera-fonts/{*.TXT,local.conf}
sed -i -e '/Makefile/d' -e '/VERSION/d' -e '/TXT/d' -e '/local.conf/d' fontBitstreamVera/MD5

%build

%install
%R_install
for f in Vera VeraBd VeraIt VeraBI; do
    rm %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
    ln -s /usr/share/fonts/bitstream-vera-sans-fonts/$f.ttf %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
done
for f in VeraMono VeraMoBd VeraMoIt VeraMoBI; do
    rm %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
    ln -s /usr/share/fonts/bitstream-vera-sans-mono-fonts/$f.ttf %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
done
for f in VeraSe VeraSeBd; do
    rm %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
    ln -s /usr/share/fonts/bitstream-vera-serif-fonts/$f.ttf %{buildroot}%{_R_libdir}/fontBitstreamVera/fonts/bitstream-vera-fonts/$f.ttf
done
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
