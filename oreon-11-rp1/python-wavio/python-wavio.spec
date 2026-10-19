%global source0_hash 05dd659e2de71d0494588e7bc5fc23c53ffab63cd808e55ecd1e1c1de83e08f3
%global pypi_name wavio
%global pypi_description wavio is simple a Python module that allows to \
read and write WAV files as numpy arrays.
Name: python-%{pypi_name}
Summary:        Read and write WAV files as numpy arrays
License: BSD-2-Clause
Version: 0.0.9
Release:        8%{?dist}
URL: https://github.com/WarrenWeckesser/wavio
Source0:        https://github.com/WarrenWeckesser/%{pypi_name}/archive/v%{version}/%{pypi_name}-v%{version}.tar.gz
Patch0: 0000-test-endianness.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{pypi_description}

%package -n python3-%{pypi_name}
Summary:        Read and write WAV files as numpy arrays
BuildArch: noarch
%description -n python3-%{pypi_name}
%{pypi_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Extract license text from comment at top of source
awk 'BEGIN { start_print=0 }
/^-----$/ { start_print=1; next }
/^"""$/ { if ( start_print==1 ) exit }
/.*/ { if (start_print == 1) print $0 }' < wavio.py > LICENSE

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest
%files -f %{oreon_filedir}/main.list
%files -n python3-wavio -f %{oreon_filedir}/python3-wavio.list

%changelog

%autochangelog
