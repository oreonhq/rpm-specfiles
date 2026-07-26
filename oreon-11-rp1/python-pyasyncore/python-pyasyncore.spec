%global source0_hash 2c7a8b9b750ba6260f1e5a061456d61320a80579c6a43d42183417da89c7d5d6

%global srcname pyasyncore
%global modname asyncore

Name:           python-%{srcname}
Version:        1.0.4
Release:        %{autorelease}
Summary:        Make %{modname} available for Python 3.12 onwards

License:        Python-2.0.1
URL:            https://github.com/simonrob/%{srcname}
Source:         https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package contains the asyncore module as found in Python versions
prior to 3.12. It is provided so that existing code relying on import
asyncore is able to continue being used without significant
refactoring.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
# these should not be executable
chmod ugo-x README.md LICENSE

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
# there are no tests upstream
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
