%global source0_hash 7340bef99a7e0032613f56dc36027b959fd3b30a787ed62d310e951f7c3a3a58

Name:           python-python-multipart
Version:        0.0.22
Release:        %autorelease
Summary:        A streaming multipart parser for Python

License:        Apache-2.0
URL:            https://github.com/Kludex/python-multipart
Source:         %{pypi_source python_multipart}


BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

BuildRequires:  tomcli

# See testenv.deps from
# https://github.com/Kludex/python-multipart/blob/%%{version}/tox.ini.  Because
# of unwanted coverage dependencies and arguments, it’s not worth packaging
# from the GitHub source archive and generating test dependencies with tox;
# it’s much easier to just enumerate them manually.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist PyYAML}

%global common_description %{expand:
Python-Multipart is a streaming multipart parser for Python.}

%description %{common_description}

%package -n python3-python-multipart
Summary:        %{summary}

%description -n python3-python-multipart %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n python_multipart-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l python_multipart

%check
%pytest

%files -n python3-python-multipart -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
