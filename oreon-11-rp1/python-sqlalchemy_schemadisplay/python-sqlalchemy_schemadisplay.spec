%global source0_hash 4f5cfcc4d665b901d87276c4bfbe7b990dc5d58bd6ef4a073872feb169fd5e29

%global srcname sqlalchemy_schemadisplay
%global gittag 2.0

Name:           python-%{srcname}
Version:        2.0
Release:        %autorelease
Summary:        Turn SQLAlchemy DB Model into a graph

License:        MIT
URL:            https://github.com/fschulze/%{srcname}
Source0:        %{url}/archive/%{gittag}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

# For tests
BuildRequires:  %{py3_dist pytest}

%description
Turn SQLAlchemy DB Model into a graph.

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import
%pytest -q tests

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
%autochangelog
