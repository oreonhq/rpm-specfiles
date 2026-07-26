%global source0_hash 3b6000a01a237c23bccfdf6d20256ea5111ec74a826ae9e74f9f0e5bb5b2383f

%global pyname python-cloudflare
%global pypi_name cloudflare

Name:           python-%{pypi_name}
Version:        2.19.4
Release:        7%{?dist}
Summary:        Python wrapper for the Cloudflare Client API v4

License:        MIT
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source}
# upstream does not provide gpg signatures for 2.9.x releases anymore:
# https://github.com/cloudflare/python-cloudflare/issues/146
#Source1:        %%{pypi_source}.asc
# upstream confirmed release signing key via github:
#   https://github.com/cloudflare/python-cloudflare/issues/93
# gpg2 --recv-keys "D093 0FD2 2220 3ABF 557C  A485 6112 9109 56F6 F8B8"
# gpg2 --export --export-options export-minimal "D093 0FD2 2220 3ABF 557C  A485 6112 9109 56F6 F8B8" > gpgkey-D093_0FD2_2220_3ABF_557C__A485_6112_9109_56F6_F8B8.gpg
Source2:        gpgkey-D093_0FD2_2220_3ABF_557C__A485_6112_9109_56F6_F8B8.gpg

# TODO: Remove this once jsonlines is packaged
Patch0:         remove-jsonlines.patch

BuildArch:      noarch
BuildRequires:  python3-devel

# Used to verify OpenPGP signature
BuildRequires:  gnupg2
BuildRequires:  sed

%description
Python wrapper library for the Cloudflare Client API v4.

%package -n python3-%{pypi_name}

Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python wrapper library for the Cloudflare Client API v4.

This is the Python 3 version of the package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%%{gpgverify} --keyring='%%{SOURCE2}' --signature='%%{SOURCE1}' --data='%%{SOURCE0}'
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf *.egg-info
# Remove shebangs
sed -i -e '1!b' -e '\~^#!/usr/bin/env python~d' cli4/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files CloudFlare

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/cli4
%doc %attr(0644,root,root) %{_mandir}/man1/cli4.1*
%{python3_sitelib}/cli4
%exclude %{python3_sitelib}/examples

%changelog
%autochangelog
