%global source2_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source1_hash 8151a3d1d2bc656fef397d9a4e9e85f58873ca7a775fdfee36fcf555660d4f6f
%global source0_hash 34f5e0c161c08f65dc0d070ba2ff4c315ed21c4b7e0faa32a46862d0dc1b8f55
%global libname btchip
%global srcname %{libname}-python
Name:     python-%{libname}
Version:  0.1.32
Release:        21%{?dist}
Summary:        Python communication library for Ledger Hardware Wallet products
License:  Apache-2.0
URL:      https://github.com/LedgerHQ/btchip-python
Source0:        https://files.pythonhosted.org/packages/source/p/python-btchip/python-btchip-%{version}.tar.gz
Source1:  https://raw.githubusercontent.com/LedgerHQ/udev-rules/765b7fdf57b20fd9326cedf48ee52e905024ab4f/20-hw1.rules
Source2:  https://raw.githubusercontent.com/LedgerHQ/btchip-python/3a941ed1a257a8ad519a473e361cda16fb4f36fd/LICENSE
BuildArch:     noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd
# /oreon:deps
%description

%package -n python3-%{libname}
Summary:        Python communication library for Ledger Hardware Wallet products
BuildRequires: python3-devel
BuildRequires: python3-setuptools
Requires: python3-hidapi hidapi >= 0.7.99
Requires: python3-mnemonic python-%{libname}-common
%description -n python3-%{libname}

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n python3-btchip -f %{oreon_filedir}/python3-btchip.list
%files -n python-btchip-common -f %{oreon_filedir}/python-btchip-common.list

%changelog

%autochangelog
