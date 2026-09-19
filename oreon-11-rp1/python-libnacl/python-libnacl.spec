%global source0_hash f3418da7df29e6d9b11fd7d990289d16397dc1020e4e35192e11aee826922860

Name:           python-libnacl
Version:        2.1.0
Release:        13%{?dist}
Summary:        Python bindings for libsodium based on ctypes

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://libnacl.readthedocs.org/
Source0:        %{pypi_source libnacl}

BuildArch:      noarch

Requires:       libsodium
BuildRequires:  python3-devel

# Testing
BuildRequires:  libsodium-devel
BuildRequires:  python3dist(pytest)

# Documentation
BuildRequires:  python3-sphinx
BuildRequires:  make

%global _description %{expand:
Python libnacl is used to gain direct access to the functions exposed by
Daniel J. Bernstein's nacl library via libsodium. It has been constructed to
maintain extensive documentation on how to use nacl as well as being completely
portable.}

%description %_description

%package -n python3-libnacl
Summary: %{summary}

%description -n python3-libnacl %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libnacl-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

make -C doc man html

%install
%pyproject_install

%pyproject_save_files libnacl

install -D -m 644 doc/_build/man/libnacl.1 %{buildroot}%{_mandir}/man1/libnacl.1

%check
%{pytest}

%files -n python3-libnacl -f %{pyproject_files}
%license LICENSE
%doc README.rst
%doc doc/_build/html/
%{_mandir}/man1/libnacl.1*

%changelog
%autochangelog
