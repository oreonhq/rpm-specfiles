%global source0_hash b01ca8b6fe7d53dfc1b3fe642a6ede28e8cc8a98526a041f7a485a15f9c34e7b

%global srcname incremental

%global common_description %{expand:
Incremental is a small library that versions your Python projects.}

Name:           python-%{srcname}
Version:        24.7.2
Release:        %autorelease
Summary:        It versions your Python projects

License:        MIT
URL:            https://github.com/twisted/incremental
Source0:        %{url}/archive/%{srcname}-%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}
Provides:       %{srcname} = %{version}-%{release}

%description -n python3-%{srcname} %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
