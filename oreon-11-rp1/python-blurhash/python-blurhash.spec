%global source0_hash da56b163e5a816e4ad07172f5639287698e09d7f3dc38d18d9726d9c1dbc4cee

Name:           python-blurhash
Version:        1.1.4
Release:        %autorelease
Summary:        Pure-Python implementation of the blurhash algorithm

License:        MIT
URL:            https://github.com/halcy/blurhash-python
Source:         %{pypi_source blurhash}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy
BuildRequires:  python3-pillow

%global _description %{expand:
Implementation of the blurhash ( https://github.com/woltapp/blurhash )
algorithm in pure python}

%description %_description

%package -n     python3-blurhash
Summary:        %{summary}

%description -n python3-blurhash %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n blurhash-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files blurhash

%check
%pyproject_check_import

%files -n python3-blurhash -f %{pyproject_files}

%changelog
%autochangelog
