%global source0_hash 79400b081cd77819a85d6772a076f058e00bbac3c2e1e3546e1da08916c6d413

%global pypi_name jcconv

Name:          python-%{pypi_name}
Version:       0.3.0
Release:       7%{?dist}
Summary:       JapaneseCharacterCONVerter

License:       MIT
URL:           https://pypi.python.org/pypi/%{pypi_name}
Source0:       https://github.com/besser82/jcconv/archive/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel

%description
inter-convert hiragana, katakana, and half-width kana

%package -n python3-%{pypi_name}
Summary:       %{summary}

%description -n python3-%{pypi_name}
inter-convert hiragana, katakana, and half-width kana

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%py3_test_envvars
%pyproject_check_import
%{python3} -m unittest -v

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc %{pypi_name}.egg-info/PKG-INFO README.rst

%changelog
%autochangelog
