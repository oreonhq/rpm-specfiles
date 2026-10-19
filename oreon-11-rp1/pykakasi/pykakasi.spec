%global source0_hash 38438dfde296b21bfa831b6afe8fe45d0c910efbbe7906fa149a43946586aa5c
%global __python /usr/bin/python3
Name:           pykakasi
Version:        2.3.0b1
Release:        1%{?dist}
Summary:        Lightweight converter from Japanese Kana-kanji sentences into Kana-Roman
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://codeberg.org/miurahr/pykakasi
Source0:        https://codeberg.org/miurahr/pykakasi/archive/v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 42
BuildRequires:  python3dist(setuptools-scm[toml]) >= 3.5.0
Requires:       python3-pykakasi = %{version}-%{release}
# /oreon:deps
%description

%prep

%autosetup -p1 -n %{name}
%py3_shebang_fix src/pykakasi/cli.py

%build

%pyproject_wheel
sphinx-build docs build/docs -b man -d man
ls -lR build/docs/
%install
%pyproject_install
chmod 0755 %{buildroot}/%{python_sitelib}/pykakasi/cli.py
mkdir -p %{buildroot}/%{_mandir}/man1
cp -a build/docs/pykakasi.1 %{buildroot}/%{_mandir}/man1/
%oreon_autofiles main

%check

%pytest -k 'not test_aozora'
%files

%changelog

%autochangelog
