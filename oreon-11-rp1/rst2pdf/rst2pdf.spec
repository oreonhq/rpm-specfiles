%global source0_hash 857e8741014ec5015f7a00aafb5dccbb56378ef4c1da55a828d44bcf5ff3acdb

Name: rst2pdf
Version: 0.105
Release: %autorelease
Summary: Tool for transforming reStructuredText to PDF
License: MIT

URL: https://rst2pdf.org/
Source0: %{pypi_source}

BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}
BuildArch: noarch

%description
Tool for transforming reStructuredText to PDF using ReportLab

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p 1
# Remove version limit for packaging and docutils
sed -i 's/"packaging.*"/"packaging"/' pyproject.toml
sed -i 's/"docutils.*"/"docutils"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files rst2pdf

%files -n %{name} -f %{pyproject_files}
%doc CHANGES.rst Contributors.txt README.rst
%license LICENSE.txt
%{_bindir}/%{name}

%changelog
%autochangelog
