%global source0_hash 8c0eae73f1d576b0d0177357d026eee30325e1249dedc03f54ebed451cc3b013

%global modname phyghtmap

Name:           python-phyghtmap
Version:        2.23
Release:        17%{?dist}
Summary:        Generate OSM contour lines from NASA SRTM data
License:        GPL-2.0-or-later
URL:            http://katze.tfiu.de/projects/phyghtmap/
Source0:        %{url}/%{modname}_%{version}.orig.tar.gz
# Compatibility fixes with newer numpy not yet upstream
Patch0:         0001-phyghtmap_numpy_arrays.patch
# Compatibility fixes for newer version of matplotplib, not yet upstream
Patch1:         0002-Fix_matplotlib_after_3_6_0.patch
BuildArch:      noarch
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
%{modname} is a little program which lets you easily generate OSM contour\
lines from NASA SRTM data.\

%description %_description

%package -n python3-phyghtmap
Summary: %summary
Requires:       python3-gdal
Requires:       python3-numpy
Requires:       python3-beautifulsoup4
Requires:       python3-matplotlib
# With matplotlib > 3.6.0, contour is used from external package
Requires:       python3-contourpy

%description -n python3-phyghtmap %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{modname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}
install -Dpm 644 docs/%{modname}.1 %{buildroot}%{_mandir}/man1/%{modname}.1

%files -n python3-%{modname} -f %{pyproject_files}
%doc README Changelog
%license LICENSE_GPL-2 COPYRIGHT
%{_bindir}/%{modname}
%{_mandir}/man1/%{modname}.1*

%changelog
%autochangelog
