%global source0_hash e855b1fe2108f63127794411f7bc8ba8b44557f38bdbbc65b7a63b7973fdc8ac

Name:           python-hanzidentifier
Version:        1.3.0
Release:        %autorelease
Summary:        Identify Chinese text as Simplified or Traditional

License:        MIT
URL:            https://github.com/tsroten/hanzidentifier
Source:         %{url}/archive/v%{version}/hanzidentifier-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Hanzi Identifier is a simple Python module that identifies a string of text as
having Simplified or Traditional characters.}

%description %_description

%package -n     python3-hanzidentifier
Summary:        %{summary}

%description -n python3-hanzidentifier %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n hanzidentifier-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files hanzidentifier

%check
%pyproject_check_import
%pytest

%files -n python3-hanzidentifier -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
