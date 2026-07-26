%global source0_hash f2fdb5fb29615c77c2743e1cb3d9314353a6e87b10c37d238d91ae1c6feae086

Name:           python-gnupg
Version:        0.5.4
Release:        %autorelease
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://gnupg.readthedocs.io/
Source0:        https://github.com/vsajip/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/vsajip/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
# From keys.openpgp.org based on fingerprinted listed in setup.cfg
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/CA749061914EAC138E66EADB9147B477339A9B86
# Add missing pyproject.toml and tox.ini (taken from github.com/vsajip/python-gnupg)
Source3:        https://raw.githubusercontent.com/vsajip/python-gnupg/refs/tags/%{version}/tox.ini
Source4:        https://raw.githubusercontent.com/vsajip/python-gnupg/refs/tags/%{version}/pyproject.toml
BuildArch:      noarch

%description
GnuPG bindings for python. This uses the gpg command.

%package -n     python3-gnupg
Summary:        A wrapper for the Gnu Privacy Guard (GPG or GnuPG)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gnupg2
Requires:       gnupg
%{?python_provide:%python_provide python3-gnupg}

%description -n python3-gnupg
GnuPG bindings for python. This uses the gpg command.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}
cp %{SOURCE3} %{SOURCE4} .

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gnupg

%check
%tox

%files -n python3-gnupg -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
