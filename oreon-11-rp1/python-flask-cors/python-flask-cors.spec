%global source0_hash bab02db4299c1efd487d690a23b2a016b99a1e9e50149c5f911399d4141f8891

%global srcname flask-cors

Name:           python-%{srcname}
Version:        6.0.2
Release:        %autorelease
Summary:        Cross Origin Resource Sharing (CORS) support for Flask
License:        MIT
URL:            https://github.com/corydolphin/%{srcname}
Source0:        https://github.com/corydolphin/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS),
making cross-origin AJAX possible.

%package -n python3-%{srcname}
Summary:        Cross Origin Resource Sharing (CORS) support for Flask

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-%{srcname}
Python3 flask_cors package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files -l flask_cors -L

%check
%pyproject_check_import
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md README.rst

%changelog
%autochangelog
