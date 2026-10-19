%global source0_hash 267b43216a0e667262bd94bc8f4adb31fc390bb053bdde7b21b0ee076a688250
Name:           python-eth-event
Version:        1.4.10
Release:        1%{?dist}
Summary:        Ethereum event decoder and topic generator
License:        MIT
URL:            https://github.com/iamdefinitelyahuman/eth-event
Source0:        https://files.pythonhosted.org/packages/source/e/eth_event/eth_event-%{version}.tar.gz
Patch:         python-eth-event-0001-Relax-deps.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(faster-eth-abi) == 5.2.30
BuildRequires:  python3dist(faster-hexbytes) == 1.3.8
BuildRequires:  python3dist(mypy[mypyc]) == 1.19.1
Requires:       python3-eth-event = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-eth-event
Summary:        Ethereum event decoder and topic generator
%description -n python3-eth-event

%prep
%global oreon_srcdir eth_event-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-eth-event usr/lib/python3*/site-packages/eth_event* usr/lib64/python3*/site-packages/eth_event* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/eth_event* usr/lib64/python3*/site-packages/eth_event* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-eth-event -f %{oreon_filedir}/python3-eth-event.list

%changelog

%autochangelog
