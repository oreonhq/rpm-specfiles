%global source0_hash aa375238b27d797ab13756dabee432b13864a20719ab83a1147c89e5f961ded2

%global commit 7f3c0dd8bd9ed89e3e146f934212516831147c51
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20230801
%global commit_release .%{commit_date}git%{short_commit}

Name:           python-ana
Version:        0.06
Release:        24%{commit_release}%{?dist}
Summary:        Python module to provide easy distributed data storage

License:        BSD-2-Clause
URL:            https://github.com/zardus/ana
Source0:        https://github.com/zardus/ana/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
ANA is a project to provide easy distributed data storage. It provides every
object with a UUID and, when pickled, will first serialize the object's state
to a central location and then "pickle" the object into just its UUID.}

%description %_description

%package -n     python3-ana
Summary:        %{summary}

%description -n python3-ana %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ana-%{commit}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
sed -i "s|assertEquals|assertEqual|g" test.py # Patch deprecated synonym.

%install
%pyproject_install
%pyproject_save_files -l ana

%check
%{py3_test_envvars} %{python3} test.py

%files -n python3-ana -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
