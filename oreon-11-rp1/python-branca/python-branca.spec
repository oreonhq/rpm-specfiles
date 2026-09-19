%global source0_hash 37fe385f14ad40610ec69b245a8640f0449c8eb96b9f764930e7c11c3d979898

%global srcname branca

Name:           python-%{srcname}
Version:        0.8.2
Release:        %autorelease
Summary:        Generate complex HTML+JS pages with Python

License:        MIT
URL:            https://github.com/python-visualization/branca
Source0:        https://github.com/python-visualization/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
This library is a spinoff from folium, that would host the non-map-specific \
features. It may become a HTML+JS generation library in the future. It is based \
on Jinja2 only.

%description %{_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(ipykernel)
BuildRequires:  python3dist(jupyter-client)
BuildRequires:  python3dist(nbconvert)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pytest)

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# Skip selenium test as Firefox is no longer available that way.
rm tests/test_iframe.py
%{pytest}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE.txt

%changelog
%autochangelog
