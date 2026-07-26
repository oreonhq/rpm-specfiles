%global source0_hash 582db6e14315f9b08cbd2df39b136dc344bfe8a27c2f05b995460fb0969ec19e

%global srcname pytest-mpl

Name:           python-%{srcname}
Version:        0.13
Release:        20%{?dist}
Summary:        Pytest plugin for testing figure output from Matplotlib

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/matplotlib/pytest-mpl
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
# Probably not going upstream.
Patch0001:      0001-Increase-tolerance-for-new-FreeType.patch

BuildArch:      noarch

%global _description \
This is a plugin to facilitate image comparison for Matplotlib figures. \
For each figure to test, an image is generated and then subtracted from an \
existing reference image. If the RMS of the residual is larger than \
a user-specified tolerance, the test will fail. Alternatively, the generated \
image can be hashed and compared to an expected value.

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
# Skip networked tests.
MPLBACKEND=Agg %{pytest} --mpl tests -k 'not test_succeeds_remote and not test_succeeds_faulty_mirror'
MPLBACKEND=Agg %{pytest} tests -k 'not test_succeeds_remote and not test_succeeds_faulty_mirror'

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_mpl/
%{python3_sitelib}/pytest_mpl-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
