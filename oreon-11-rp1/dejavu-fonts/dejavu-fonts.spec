# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fa9ca4d13871dd122f61258a80d01751d603b4d3ee14095d65453b4e846e17d7
%global fontdir %{_fontbasedir}/dejavu

Name: dejavu-fonts
Version: 2.37
Release: 1%{?dist}
Summary: DejaVu variable and monospaced font families
License: Bitstream-Vera
URL: https://dejavu-fonts.github.io/
Source0: https://github.com/dejavu-fonts/dejavu-fonts/releases/download/version_2_37/dejavu-fonts-ttf-%{version}.tar.bz2
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: fonts-srpm-macros
BuildRequires: libxml2
Requires: fontconfig

%description
The DejaVu fonts are based on the Bitstream Vera fonts and provide a wider
range of characters while keeping the original look.

%prep
%oreon_sha256
%autosetup -n dejavu-fonts-ttf-%{version}

%build

%install
install -d %{buildroot}%{fontdir}
install -p -m 0644 ttf/*.ttf %{buildroot}%{fontdir}
install -d %{buildroot}%{_fontconfig_templatedir}
install -d %{buildroot}%{_fontconfig_confdir}
for conf in fontconfig/*.conf; do
  name=$(basename "$conf")
  install -p -m 0644 "$conf" "%{buildroot}%{_fontconfig_templatedir}/$name"
  ln -s "%{_fontconfig_templatedir}/$name" "%{buildroot}%{_fontconfig_confdir}/$name"
done

%check
test "$(ls %{buildroot}%{fontdir}/*.ttf | wc -l)" -ge 20
for conf in %{buildroot}%{_fontconfig_templatedir}/*dejavu*.conf; do
  xmllint --noout --nonet "$conf"
done

%files
%license LICENSE
%doc AUTHORS NEWS README.md
%dir %{fontdir}
%{fontdir}/*.ttf
%{_fontconfig_templatedir}/*dejavu*.conf
%{_fontconfig_confdir}/*dejavu*.conf

%changelog
%autochangelog
