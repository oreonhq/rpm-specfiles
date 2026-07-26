%global source0_hash f69d31a3b56eee119d1ec6063e9c732dd44fbba352ef738cb22d9699fc4009fe

Name:          python-allpairspy
Version:       2.5.1
Release:       6%{?dist}
Summary:       Pairwise test combinations generator

License:       MIT
URL:           https://github.com/thombashi/allpairspy
Source0:       %{pypi_source allpairspy}

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-allpairspy
Summary:        %{summary}

%description -n python3-allpairspy
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n allpairspy-%{version}
rm -rf allpairspy.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l allpairspy

%check
%{pytest}

%files -n python3-allpairspy -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt

%changelog
%autochangelog
