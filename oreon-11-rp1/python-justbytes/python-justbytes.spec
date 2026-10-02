%global source0_hash 815dba096750c0e0158bbc872ee1b7e2bde4551b5792e9b256e85213c690de58

%global srcname justbytes

Name:           python-%{srcname}
Version:        0.15.3
Release:        %autorelease
Summary:        Library for handling computation with address ranges in bytes

License:        LGPL-2.1-or-later
URL:            http://pypi.python.org/pypi/justbytes
Source0:        https://pypi.io/packages/source/j/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
A library for handling computations with address ranges. The library also offers\
a configurable way to extract the representation of a value.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l justbytes

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
