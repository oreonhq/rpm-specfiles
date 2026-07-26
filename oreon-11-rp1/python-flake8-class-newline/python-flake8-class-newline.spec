%global source0_hash b5993799a98acd2e391195ec92bd2ab7735be6796e13dae1e6893f14a121fd0c

%global srcname flake8-class-newline

Name:           python-%{srcname}
Version:        1.6.0
Release:        10%{?dist}
Summary:        Flake8 extension to check for new lines after class definitions

License:        MIT
URL:            https://github.com/AlexanderVanEck/flake8-class-newline
Source0:        https://github.com/AlexanderVanEck/flake8-class-newline/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
PEP8 says we should surround every class method with a single blank line.
However flake8 is ambiguous about the first method having a blank line above
it. This plugin was made to enforce that it should.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l flake8_class_newline

%check
%{py3_test_envvars} %{__python3} -m unittest -v

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.rst

%changelog
%autochangelog
