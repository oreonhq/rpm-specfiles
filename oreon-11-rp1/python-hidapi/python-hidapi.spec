%global source0_hash ecbc265cbe8b7b88755f421e0ba25f084091ec550c2b90ff9e8ddd4fcd540311

%global py_setup_args --with-system-hidapi --with-libusb

Name:     python-hidapi
Version:  0.15.0
Release:  2%{?dist}
Summary:  Interface to the hidapi library

# Automatically converted from old format: GPLv3+ or BSD or Public Domain - review is highly recommended.
License:  GPL-3.0-or-later OR LicenseRef-Callaway-BSD OR LicenseRef-Callaway-Public-Domain
URL:      https://github.com/trezor/cython-hidapi
Source0:  %{pypi_source hidapi}

BuildRequires: gcc
BuildRequires: hidapi-devel
BuildRequires: libusb1-devel
BuildRequires: libudev-devel

BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: python3-setuptools
BuildRequires: python3-cython

%description
%{summary}.

%package -n python3-hidapi
Summary:  %{summary}

%description -n python3-hidapi
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n hidapi-%{version}

# Remove pre-built and bundled hidapi.
rm -rf hidapi hidapi.egg-info hid.c

%if 0%{?flatpak}
# hidapi is not part of the runtime and is also built into /app
sed -i -e 's|/usr/include/hidapi|%{_includedir}/hidapi|' setup.py
%endif

%build
%py3_build

%install
%py3_install

%check
%{pytest} tests.py

%files -n python3-hidapi
%license LICENSE*.txt
%doc README.rst try.py
%{python3_sitearch}/hid%{python3_ext_suffix}
%{python3_sitearch}/hidraw%{python3_ext_suffix}
%{python3_sitearch}/hidapi-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
