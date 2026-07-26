%global source0_hash 3951d360f2daf0e0eacf839e15d2d1d2f4f5e7830231eb3188eeffef2dd17bad

Name:           python-libusb1
Version:        3.3.1
Release:        6%{?dist}
Summary:        Pure-python wrapper for libusb-1.0

License:        LGPL-2.1-or-later
URL:            https://github.com/vpelletier/python-libusb1
Source0:        %{pypi_source libusb1}
Source1:        https://github.com/vpelletier/%{name}/releases/download/%{version}/libusb1-%{version}.tar.gz.asc

#https://github.com/vpelletier/python-libusb1/blob/5bc97a163ee1ca98ca6bfc11045f5c4ab94ec654/KEYS
#Wed Jan 05 2022, exported the upstream gpg key using the command:
#gpg2 --armor --export --export-options export-minimal 983AE8B73B9115987A923845CAC936914257B0C1 > gpgkey-python-libusb1.gpg
Source2:        gpgkey-python-libusb1.gpg

BuildArch:      noarch
BuildRequires:  gnupg2
BuildRequires:  libusb1-devel
BuildRequires:  python3-devel
Requires:       libusb1

%global _description %{expand:
Pure-python wrapper for libusb-1.0.

Supports all transfer types, both in synchronous and asynchronous mode.}

%description %_description

%package -n python3-libusb1
Summary: %{summary}

%description -n python3-libusb1 %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n libusb1-%{version}
rm -rf libusb1.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l usb1 libusb1

%check
%pyproject_check_import
%{python3} -m unittest usb1/test*.py

%files -n python3-libusb1 -f %{pyproject_files}
%license COPYING COPYING.LESSER
%doc README.rst PKG-INFO

%changelog
%autochangelog
