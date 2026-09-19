%global source0_hash 5a9dfabd51285950dfba5db35f98ef3b3576d4bacb95c421b09e0fdabe781acf

%global proj_name gbinder-python

Name:           python-gbinder
Version:        1.3.0
Release:        2%{?dist}
Summary:        Python bindings for libgbinder

License:        GPL-3.0-only
URL:            https://github.com/waydroid/%{proj_name}
Source:         %{url}/archive/%{version}/%{proj_name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global libgbinder_version 1.1.20
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  gcc
BuildRequires:  pkgconfig(libgbinder) >= %{libgbinder_version}

%global _description %{expand:
Cython extension module for libgbinder.
Provides IPC comunication over the /dev/binder protocol for python scripts.}

%description %{_description}

%package -n python3-gbinder
Summary:        %{summary}
Requires:       libgbinder >= %{libgbinder_version}

%description -n python3-gbinder %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{proj_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files gbinder

%files -n python3-gbinder -f %{pyproject_files}

%changelog
%autochangelog
