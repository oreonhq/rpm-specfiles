%global source0_hash 943fb1f7dfd8692b999e08fcb1b3f206f9514c2313bd8bbbd0624f5015e7e707
Name:           python-snakemake-storage-plugin-xrootd
Version:        1.2.0
Release:        1%{?dist}
Summary:        Snakemake storage plugin for xrootd storage
License:        MIT
URL:            https://github.com/snakemake/snakemake-storage-plugin-xrootd
Source0:        https://github.com/snakemake/snakemake-storage-plugin-xrootd/archive/v%{version}/snakemake-storage-plugin-xrootd-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
A Snakemake storage plugin for handling input and output via XRootD.}
# oreon:deps
BuildRequires:  python3dist(pytest)
BuildRequires:  snakemake
BuildRequires:  xrootd-server
# /oreon:deps
%description %{common_description}

%package -n python3-snakemake-storage-plugin-xrootd
Summary:        Snakemake storage plugin for xrootd storage
%description -n python3-snakemake-storage-plugin-xrootd %{common_description}

%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%prep
%oreon_prep
%install
%pyproject_install
%oreon_autofiles python3-snakemake-storage-plugin-xrootd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v -k "${k-}" tests/tests.py
%files -f %{oreon_filedir}/main.list
%files -n python3-snakemake-storage-plugin-xrootd -f %{oreon_filedir}/python3-snakemake-storage-plugin-xrootd.list

%changelog

%autochangelog
