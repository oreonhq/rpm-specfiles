%global source0_hash c5452179b56601c178b03d468a5326cc1fe37d9be81d24d0d6bdab36c4b93ad8

Name:           python-colorful
Version:        0.5.7
Release:        %autorelease
Summary:        Terminal string styling done right
License:        MIT
URL:            https://github.com/timofurrer/colorful
Source:         %{pypi_source colorful}
BuildArch:      noarch

%description
%{summary}.

%package -n python3-colorful
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-colorful
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n colorful-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l colorful

%check
%pytest --verbose tests

%files -n python3-colorful -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
