%global source0_hash 5c8d74aa01ca4e29d3298a6414ed5ac9ad77d432b4f4f216c07996426f5ddc2a

%global srcname pyrtlsdr
Name:             python-%{srcname}
Version:          0.3.0
Release:          15%{?dist}
Summary:          Python binding for librtlsdr
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:          GPL-3.0-only
URL:              https://github.com/roger-/pyrtlsdr
Source0:          https://github.com/roger-/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:        noarch

%description
Python binding for librtlsdr (a driver for Realtek RTL2832U based SDR's).

%package -n python3-%{srcname}
Summary:          Python 3 binding for librtlsdr
BuildRequires:    python3-devel
# needed for librtlsdr
Requires:         rtl-sdr
# faster arrays
Recommends:       python3-numpy

%description -n python3-%{srcname}
Python 3 binding for librtlsdr (a driver for Realtek RTL2832U based SDR's).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}
rm -rf pyrtlsdr.egg-info
chmod 644 rtlsdr/rtlsdrtcp/base.py

find . -name '*.py' | xargs sed -i '1s|^#!.*|#!%{__python3}|'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files rtlsdr

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
