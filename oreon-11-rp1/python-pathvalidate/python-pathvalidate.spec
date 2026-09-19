%global source0_hash b18c07212bfead624345bb8e1d6141cdcf15a39736994ea0b94035ad2b1ba177

Name:      python-pathvalidate
Version:   3.3.1
Release:   %autorelease
Summary:   Library to sanitize/validate a string such as file-names/file-paths/etc

# SPDX
License:   MIT
URL:       https://github.com/thombashi/pathvalidate
Source:    %{pypi_source pathvalidate}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-allpairspy
BuildRequires:  python3-click
BuildRequires:  python3-tcolorpy

%description
%{summary}.

%package -n python3-pathvalidate
Summary:        %{summary}

%description -n python3-pathvalidate
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pathvalidate-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files -l pathvalidate

%check
%pytest -r fEs

%files -n python3-pathvalidate -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
