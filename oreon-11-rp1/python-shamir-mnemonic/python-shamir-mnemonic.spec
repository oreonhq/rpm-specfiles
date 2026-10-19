%global source0_hash bc04886a1ddfe2a64d8a3ec51abf0f664d98d5b557cc7e78a8ad2d10a1d87438
Name:    python-shamir-mnemonic
Version: 0.3.0
Release:        1%{?dist}
Summary:        Reference implementation of SLIP-0039: Shamir’s Secret-Sharing for Mnemonic Codes
License: MIT
URL:     https://github.com/trezor/python-shamir-mnemonic
Source0:        https://files.pythonhosted.org/packages/source/s/shamir_mnemonic/shamir_mnemonic-%{version}.tar.gz
BuildArch:     noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-shamir-mnemonic = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-shamir-mnemonic
Summary:        Reference implementation of SLIP-0039: Shamir’s Secret-Sharing for Mnemonic Codes
%description -n python3-shamir-mnemonic

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir shamir_mnemonic-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-shamir-mnemonic usr/lib/python3*/site-packages/shamir_mnemonic* usr/lib64/python3*/site-packages/shamir_mnemonic* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/shamir_mnemonic* usr/lib64/python3*/site-packages/shamir_mnemonic* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-shamir-mnemonic -f %{oreon_filedir}/python3-shamir-mnemonic.list

%changelog

%autochangelog
