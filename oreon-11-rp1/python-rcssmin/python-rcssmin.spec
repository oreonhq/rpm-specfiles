%global source0_hash 806986eaf7414545edc28a1d29523e9560e49e151ff4a337d9d1f0271d6e1cc4

%global pypi_name rcssmin
%global desc %{expand: \
RCSSmin is a CSS minifier.

The minifier is based on the semantics of the YUI compressor, which itself
is based on the rule list by Isaac Schlueter.

This module is a re-implementation aiming for speed instead of maximum
compression, so it can be used at runtime (rather than during a preprocessing
step).}

Name:		python-%{pypi_name}
Version:	1.2.2
Release:	%autorelease
Summary:	CSS Minifier

License:	Apache-2.0
URL:		http://opensource.perlig.de/rcssmin/
Source:		%{pypi_source}

BuildRequires:	gcc
BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:	CSS Minifier

%description -n python3-%{pypi_name}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

# strip bang path from rcssmin.py
sed -i '1d' rcssmin.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{python3_sitearch}/_%{pypi_name}.cpython*

%changelog
%autochangelog
