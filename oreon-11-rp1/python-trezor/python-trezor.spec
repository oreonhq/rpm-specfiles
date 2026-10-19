%global source0_hash 0ab3cebb44fecb532b77d5a2b401b50187a1d70b7251a6cc2df5494e52ffdf57
Name:           python-trezor
Version:        0.20.2
Release:        1%{?dist}
Summary:        Python library for communicating with Trezor Hardware Wallet
License:        LGPL-3.0-only
URL:            https://github.com/trezor/trezor-firmware/tree/main/python
Source0:        https://files.pythonhosted.org/packages/source/t/trezor/trezor-%{version}.tar.gz
BuildArch:      noarch
Patch:          remove_click_upper_bound.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 5
BuildRequires:  python3dist(flit-core) >= 3.11
Requires:       python3-trezor = %{version}-%{release}
# /oreon:deps
%package -n       python3-trezor+hidapi
Summary:        Metapackage for python3-trezor hidapi extras
Requires:       python3-trezor = %{version}-%{release}
Requires:       python3dist(hidapi) >= 0.7.99.post20
Provides:       python3dist(trezor[hidapi]) = %{version}-%{release}

%description -n python3-trezor+hidapi
Metapackage for python3-trezor hidapi extras.

%package -n       python3-trezor+ethereum
Summary:        Metapackage for python3-trezor ethereum extras
Requires:       python3-trezor = %{version}-%{release}
Requires:       python3dist(web3) >= 5
Provides:       python3dist(trezor[ethereum]) = %{version}-%{release}

%description -n python3-trezor+ethereum
Metapackage for python3-trezor ethereum extras.

%package -n       python3-trezor+qt-widgets
Summary:        Metapackage for python3-trezor qt-widgets extras
Requires:       python3-trezor = %{version}-%{release}
Provides:       python3dist(trezor[qt-widgets]) = %{version}-%{release}

%description -n python3-trezor+qt-widgets
Metapackage for python3-trezor qt-widgets extras.

%package -n       python3-trezor+extra
Summary:        Metapackage for python3-trezor extra extras
Requires:       python3-trezor = %{version}-%{release}
Requires:       python3dist(pillow) >= 10
Provides:       python3dist(trezor[extra]) = %{version}-%{release}

%description -n python3-trezor+extra
Metapackage for python3-trezor extra extras.

%package -n       python3-trezor+stellar
Summary:        Metapackage for python3-trezor stellar extras
Requires:       python3-trezor = %{version}-%{release}
Requires:       python3dist(stellar-sdk) >= 13
Requires:       python3dist(stellar-sdk) >= 15
Provides:       python3dist(trezor[stellar]) = %{version}-%{release}

%description -n python3-trezor+stellar
Metapackage for python3-trezor stellar extras.

%package -n       python3-trezor+ble
Summary:        Metapackage for python3-trezor ble extras
Requires:       python3-trezor = %{version}-%{release}
Requires:       python3dist(bleak) >= 1.1.0
Provides:       python3dist(trezor[ble]) = %{version}-%{release}

%description -n python3-trezor+ble
Metapackage for python3-trezor ble extras.

%package -n       python3-trezor+full
Summary:        Metapackage for python3-trezor full extras
Requires:       python3-trezor = %{version}-%{release}
Requires:       python3dist(hidapi) >= 0.7.99.post20
Requires:       python3dist(web3) >= 5
Requires:       python3dist(pillow) >= 10
Requires:       python3dist(stellar-sdk) >= 13
Requires:       python3dist(stellar-sdk) >= 15
Requires:       python3dist(bleak) >= 1.1.0
Provides:       python3dist(trezor[full]) = %{version}-%{release}

%description -n python3-trezor+full
Metapackage for python3-trezor full extras.

%description

%package -n     python3-trezor
Summary:        Python library for communicating with Trezor Hardware Wallet
# oreon:reqs
Requires:       python3dist(click) < 9
Requires:       python3dist(click) >= 8
Requires:       python3dist(construct) >= 2.9
Requires:       python3dist(construct-classes) >= 0.1.2
Requires:       python3dist(cryptography) >= 47
Requires:       python3dist(keyring) >= 25.7.0
Requires:       python3dist(libusb1) >= 1.6.4
Requires:       python3dist(mnemonic) >= 0.20
Requires:       python3dist(noiseprotocol) < 0.4.0
Requires:       python3dist(noiseprotocol) >= 0.3.1
Requires:       python3dist(platformdirs) >= 4.4.0
Requires:       python3dist(requests) >= 2.4.0
Requires:       python3dist(shamir-mnemonic) >= 0.3.0
Requires:       python3dist(slip10) >= 1.0.1
Requires:       python3dist(typing-extensions) >= 4.7.1
# /oreon:reqs
%description -n python3-trezor

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir trezor-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-trezor usr/lib/python3*/site-packages/trezor* usr/lib64/python3*/site-packages/trezor* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/trezor* usr/lib64/python3*/site-packages/trezor* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-trezor -f %{oreon_filedir}/python3-trezor.list

%changelog

%autochangelog
