%global srcname justbases
Name:       python-%{srcname}
Version:    0.15.2
Release:    %autorelease
Summary:    A small library for precise conversion between arbitrary bases

License:    LGPL-2.1-or-later
URL:        http://pypi.python.org/pypi/justbases
Source0:    https://pypi.io/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 de6646eb9891b59657d183c7fc9ffa823b8523856b942446707e2a8615f4866f
%global source0_file justbases-0.15.2.tar.gz
# oreon url source checksums end

BuildArch:  noarch

%description
A small library for precise conversion between arbitrary bases and native
Python numbers.

%package -n python3-%{srcname}
Summary:    A small library for precise conversion between arbitrary bases

BuildRequires:  python3-devel

%description -n python3-%{srcname}
A small library for precise conversion between arbitrary bases and native
Python numbers.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/justbases-0.15.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "de6646eb9891b59657d183c7fc9ffa823b8523856b942446707e2a8615f4866f" || { echo "oreon: Source0 SHA256 mismatch for justbases-0.15.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l justbases

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15.2-1
- Prepare for Oreon 11 (RP1)
