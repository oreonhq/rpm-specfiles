%global source0_hash 6171d12403e0d9474c97c92db4b3ceaae86936edd967428eb15b7d610b31d4d1

Name:           python-lxml-html-clean
Version:        0.4.4
Release:        %autorelease
Summary:        HTML cleaner from lxml project
License:        BSD-3-Clause
URL:            https://github.com/fedora-python/lxml_html_clean/
Source:         %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
HTML cleaner from lxml project.}

%description %_description

%package -n     python3-lxml-html-clean
Summary:        %{summary}

%description -n python3-lxml-html-clean %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n lxml_html_clean-%{version}
sed -i "/memory_profiler/d" tox.ini
# This test requires newer version of libxml2
# https://src.fedoraproject.org/rpms/libxml2/pull-request/16
rm tests/test_clean.txt
sed -i "s@tests/test_clean.txt@@" tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l lxml_html_clean

%check
%tox

%files -n python3-lxml-html-clean -f %{pyproject_files}
%doc CHANGES.rst README.md

%changelog
%autochangelog
