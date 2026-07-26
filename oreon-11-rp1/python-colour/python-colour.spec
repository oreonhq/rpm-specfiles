%global source0_hash af20120fefd2afede8b001fbef2ea9da70ad7d49fafdb6489025dae8745c3aee

%global pypi_name colour

Name:           python-%{pypi_name}
Version:        0.1.5
Release:        29%{?dist}
Summary:        Python module to convert and manipulate color representations

License:        BSD-2-Clause
URL:            https://github.com/vaab/colour
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Converts and manipulates common color representation (RGB, HSL, web, etc.)

- Damn simple and pythonic way to manipulate color representation
- Full conversion between RGB, HSL, 6-digit hex, 3-digit hex, human color
- One object (Color) or bunch of single purpose function (rgb2hex, hsl2rgb,
  etc.) web format that use the smallest representation between 6-digit 
  (e.g. #fa3b2c), 3-digit (e.g. #fbb), fully spelled color (e.g. white),
  following W3C color naming for compatible CSS or HTML color specifications.
- smooth intuitive color scale generation choosing N color gradients.
- can pick colors for you to identify objects of your application.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Converts and manipulates common color representation (RGB, HSL, web, etc.)

- Damn simple and pythonic way to manipulate color representation
- Full conversion between RGB, HSL, 6-digit hex, 3-digit hex, human color
- One object (Color) or bunch of single purpose function (rgb2hex, hsl2rgb,
  etc.) web format that use the smallest representation between 6-digit 
  (e.g. #fa3b2c), 3-digit (e.g. #fbb), fully spelled color (e.g. white),
  following W3C color naming for compatible CSS or HTML color specifications.
- smooth intuitive color scale generation choosing N color gradients.
- can pick colors for you to identify objects of your application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst TODO.rst
%license LICENSE

%changelog
%autochangelog
