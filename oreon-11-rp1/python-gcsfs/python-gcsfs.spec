%global source0_hash 12c66c1601167cdd560d7b258e500161e5297856e42cb33435ae72ef27dfee22

%global srcname gcsfs

Name:           python-%{srcname}
Version:        2025.10.0
Release:        %autorelease
Summary:        Convenient filesystem interface over GCS

License:        BSD-3-Clause
URL:            https://github.com/fsspec/gcsfs
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
Patch0:         gcsfs-fsspec-pin.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
GCSFS is a pythonic filesystem interface to Google Cloud Storage.
It builds on fsspec.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%pyproject_extras_subpkg -n python3-%{srcname} crc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x crc

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
