%global source0_hash ecb3d768f32202af770477b8b65f318fa4f566c22948673a977b00d589dd80f6

Name:           python-webcolors
Version:        24.11.1
Release:        %autorelease
Summary:        A library for working with the color formats defined by HTML and CSS
License:        BSD-3-Clause
URL:            https://github.com/ubernostrum/webcolors
Source:         %{pypi_source webcolors}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
webcolors is a module for working with and converting between the various
HTML/CSS color formats.}

%description %_description

%package -n python3-webcolors
Summary:        %{summary}

%description -n python3-webcolors %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n webcolors-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L webcolors

%check
%{py3_test_envvars} %{python3} -m unittest discover

%files -n python3-webcolors -f %{pyproject_files}
%license %{python3_sitelib}/webcolors-%{version}.dist-info/licenses/LICENSE
%doc README.rst

%changelog
%autochangelog
