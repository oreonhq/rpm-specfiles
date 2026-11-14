# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e0d9b7f11885fdfdc4987f06b2aa0565ad2a4af52b22e5ebf79e1a98abd0ae2f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global fontdir %{_fontbasedir}/urw-base35

Name:           urw-base35-fonts
Version:        20200910
Release:        1%{?dist}
Summary:        Core Font Set containing 35 freely distributable fonts
License:        AGPL-3.0-only WITH PS-or-PDF-font-exception-20170817
URL:            https://github.com/ArtifexSoftware/urw-base35-fonts
Source0:        https://github.com/ArtifexSoftware/urw-base35-fonts/archive/%{version}/urw-base35-fonts-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  fonts-srpm-macros
BuildRequires:  libxml2
BuildRequires:  oreon-rpm-macros

Requires:       fontconfig

%description
The (URW)++ Core Font Set Level 2 contains 35 freely distributable fonts that
are metric compatible with the standard PostScript fonts. The fonts are
provided in Type 1, OpenType and TrueType formats together with their AFM
metrics, and are used by Ghostscript as its default fonts.

%prep
%oreon_sha256
%autosetup

%build

%install
install -d %{buildroot}%{fontdir}
install -p -m 0644 fonts/*.t1 fonts/*.afm fonts/*.otf fonts/*.ttf %{buildroot}%{fontdir}

install -d %{buildroot}%{_fontconfig_templatedir}
install -d %{buildroot}%{_fontconfig_confdir}
for conf in fontconfig/*.conf; do
  name=$(basename "$conf")
  install -p -m 0644 "$conf" "%{buildroot}%{_fontconfig_templatedir}/61-$name"
  ln -s "%{_fontconfig_templatedir}/61-$name" "%{buildroot}%{_fontconfig_confdir}/61-$name"
done

install -d %{buildroot}%{_metainfodir}
install -p -m 0644 appstream/*.metainfo.xml %{buildroot}%{_metainfodir}

%check
test "$(ls %{buildroot}%{fontdir}/*.t1 | wc -l)" -eq 35
test "$(ls %{buildroot}%{fontdir}/*.afm | wc -l)" -eq 35
for conf in %{buildroot}%{_fontconfig_templatedir}/61-urw-*.conf; do
  xmllint --noout --nonet "$conf"
done

%files
%license LICENSE COPYING
%doc README.md
%dir %{fontdir}
%{fontdir}/*.t1
%{fontdir}/*.afm
%{fontdir}/*.otf
%{fontdir}/*.ttf
%{_fontconfig_templatedir}/61-urw-*.conf
%{_fontconfig_confdir}/61-urw-*.conf
%{_metainfodir}/de.urwpp.*.metainfo.xml

%changelog
%autochangelog
