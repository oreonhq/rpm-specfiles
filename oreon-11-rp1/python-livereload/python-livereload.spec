%global source0_hash 3d9bf7c05673df06e32bea23b494b8d36ca6d10f7d5c3c8a6989608c09c986a9

Name:           python-livereload
Version:        2.7.1
Release:        %autorelease
Summary:        Reload webpages on changes
License:        BSD-3-Clause
URL:            https://github.com/lepture/python-livereload
Source:         %{pypi_source livereload}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Reload webpages on changes, without hitting refresh in your browser.}

%description %_description

%package -n python3-livereload
Summary:        %{summary}

%description -n python3-livereload %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n livereload-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l livereload

%check
%pytest

%files -n python3-livereload -f %{pyproject_files}
%{_bindir}/livereload

%changelog
%autochangelog
