%global source0_hash 34f5e0c161c08f65dc0d070ba2ff4c315ed21c4b7e0faa32a46862d0dc1b8f55

%global libname btchip
%global srcname %{libname}-python

Name:     python-%{libname}
Version:  0.1.32
Release:  21%{?dist}
Summary:  Python communication library for Ledger Hardware Wallet products

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:  Apache-2.0
URL:      https://github.com/LedgerHQ/btchip-python
Source0:  %{pypi_source}
Source1:  https://raw.githubusercontent.com/LedgerHQ/udev-rules/765b7fdf57b20fd9326cedf48ee52e905024ab4f/20-hw1.rules
Source2:  https://raw.githubusercontent.com/LedgerHQ/btchip-python/3a941ed1a257a8ad519a473e361cda16fb4f36fd/LICENSE

BuildArch:     noarch
BuildRequires: systemd

%global _description %{expand:
btchip-python is a python API for communicating primarily with the
Ledger HW.1 hardware bitcoin wallet. This library also adds compatibility
to Electrum in order to use the "Nano", "Nano S", and other Ledger-based
hardware wallets.}

%description %_description

%package -n python3-%{libname}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: python3-hidapi hidapi >= 0.7.99
Requires: python3-mnemonic python-%{libname}-common

%description -n python3-%{libname} %_description

%package -n python-%{libname}-common
Summary: udev rules for Ledger devices

%description -n python-%{libname}-common
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
rm -rf btchip_python.egg-info
cp %{SOURCE2} .

# Adjust version contstraint to comply with PEP-440
# https://peps.python.org/pep-0440/
# This makes package compatible with python-packaging>=22.0.0
sed -i 's/1.6.12-4build1/1.6.12/' setup.py

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_udevrulesdir}
install -m644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/20-ledger.rules

%check
# Tests try to contact PyPi

%files -n python3-%{libname}
%license LICENSE
%doc README.md
%{python3_sitelib}/btchip_python-*.egg-info/
%{python3_sitelib}/btchip/

%files -n python-%{libname}-common
%{_udevrulesdir}/20-ledger.rules

%changelog
%autochangelog
