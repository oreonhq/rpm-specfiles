# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 02aa2e7d42072ceee280743aba0167f412b026d4e725407d36ce1c56a3a8ffc0
%global source1_hash 2d4eb074c1b81db8195046829f6a7dc710a7177102660a3ae47b2d18cdd2cfad
%global source2_hash 3a34c9b61500f4a7500994d93e9efe749396da91d1abbbb6a07618a23080b1d8
%global source3_hash 391c14688021ed40b50a22c99130648e3e000835c97bdbf104f0ed867f610fda
%global source4_hash c57f1c31771289c6f2afd490ba972e239d80889cd6063265cfd90e4f3fa1c3ad
%global debug_package %{nil}

Name:           python-rpm-macros
Version:        3.15
Release:        1%{?dist}
Summary:        The common Python RPM macros
License:        MIT AND PSF-2.0
URL:            https://www.python.org/
BuildArch:      noarch
Source0:        macros.python
Source1:        macros.python3
Source2:        macros.pybytecompile
Source3:        https://github.com/fedora-python/pathfix/raw/v1.0.0/pathfix.py
Source4:        import_all_modules.py

Requires:       python-srpm-macros
BuildRequires:  oreon-rpm-macros

%description
This package contains the unversioned Python RPM macros, that most
implementations should rely on.

You should not need to install this package manually as the various
python?-devel packages require it. So install a python-devel package instead.

%package -n python3-rpm-macros
Summary:        RPM macros for building Python 3 packages
Requires:       python-rpm-macros = %{version}-%{release}
Requires:       python-srpm-macros

%description -n python3-rpm-macros
RPM macros for building Python 3 packages.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
echo '%{source4_hash}  %{SOURCE4}' | sha256sum -c -
%setup -c -T
cp -p %{sources} .

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmconfigdir}/oreon
install -m 644 macros.python macros.pybytecompile %{buildroot}%{_rpmmacrodir}/
install -m 644 macros.python3 %{buildroot}%{_rpmmacrodir}/
install -m 644 pathfix.py import_all_modules.py %{buildroot}%{_rpmconfigdir}/oreon/

%check
grep -E '^#[^%%]*%%[^%%]' %{buildroot}%{_rpmmacrodir}/macros.* && exit 1 || true

%files
%{_rpmmacrodir}/macros.python
%{_rpmmacrodir}/macros.pybytecompile
%{_rpmconfigdir}/oreon/pathfix.py
%{_rpmconfigdir}/oreon/import_all_modules.py

%files -n python3-rpm-macros
%{_rpmmacrodir}/macros.python3
