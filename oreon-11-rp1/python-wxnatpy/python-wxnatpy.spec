%global source0_hash a9beab8fe58993dc1e86056dc2ff4809cbc8f3b74df458e29102d57e2635b460

%global desc %{expand: \
wxnatpy is a wxPython widget which allows users to browse the contents of a
XNAT repository.  It is built on top of wxPython and xnatpy.}

Name:           python-wxnatpy
Version:        0.4.0
Release:        %autorelease
Summary:        wxnatpy is a wxPython widget which allows users to browse the contents of a XNAT repository
License:        Apache-2.0
URL:            https://github.com/pauldmccarthy/wxnatpy
Source0:        %{url}/archive/%{version}/wxnatpy-%{version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%package -n python3-wxnatpy
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-wxnatpy
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n wxnatpy-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l wxnat

%check
%pyproject_check_import

%files -n python3-wxnatpy -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
