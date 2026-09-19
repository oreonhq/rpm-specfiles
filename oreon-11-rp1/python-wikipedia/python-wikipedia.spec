%global source0_hash 825dd4cd6c2594d282e75aadd1bca1b4a22c49537360a2de067428c416af487c

%global srcname wikipedia

Name:           python-%{srcname}
Version:        1.4.5
Release:        38%{?dist}
Summary:        Wikipedia API for Python

License:        MIT
URL:            https://github.com/barrust/Wikipedia
Source0:        https://github.com/barrust/Wikipedia/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Search Wikipedia, get article summaries, get data like links and images
from a page, and more.

%package -n     python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
Requires:       python3-beautifulsoup4
Requires:       python3-requests

%description -n python3-%{srcname}
Search Wikipedia, get article summaries, get data like links and images
from a page, and more.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Wikipedia-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%pyproject_check_import

%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
