%global source0_hash 80a9354e3f056144b5cf1f11e70618da44bd034a48eaefd27636d320a1cee284

Name:           python-ogr
Version:        0.61.1
Release:        1%{?dist}
Summary:        One API for multiple git forges

License:        MIT
URL:            https://github.com/packit/ogr
Source0:        %{pypi_source ogr}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
One Git library to Rule!

%package -n     python3-ogr
Summary:        %{summary}

%description -n python3-ogr
One Git library to Rule!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ogr-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files ogr

%files -n python3-ogr -f %{pyproject_files}
# Epel9 does not tag the license file in pyproject_files as a license. Manually install it in this case
%if 0%{?el9}
%license LICENSE
%endif
%doc README.md

%changelog
%autochangelog
