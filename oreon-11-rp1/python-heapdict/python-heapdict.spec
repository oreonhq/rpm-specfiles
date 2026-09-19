%global source0_hash 8495f57b3e03d8e46d5f1b2cc62ca881aca392fd5cc048dc0aa2e1a6d23ecdb6

%global srcname heapdict
%global pkgname HeapDict

Name:           python-%{srcname}
Version:        1.0.1
Release:        26%{?dist}
Summary:        A heap with decrease-key and increase-key operations

License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        %pypi_source %{pkgname}

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%global _description \
HeapDict is designed to be used as a priority queue, where items are added and \
consumed by priority. Compared to an ordinary dict, a heapdict has the \
following differences: popitem and peekitem returns the (key, priority) pair \
with the lowest priority, instead of a random object.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-test

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkgname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%{python3} -m unittest test_heap.py

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
