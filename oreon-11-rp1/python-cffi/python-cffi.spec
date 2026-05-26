# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 e32bea840b50779a43dcaff13dcf6fa8bc29aa1b071c2cb4e27c1bd79114a202
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           python-cffi
Version:        2.0.0
Release:        %autorelease
Summary:        Foreign Function Interface for Python to call C code
# cffi is MIT
# cffi/_imp_emulation.py has bits copied from CPython (PSF-2.0)
License:        MIT AND PSF-2.0
URL:            https://github.com/python-cffi/cffi
Source:        https://github.com/python-cffi/cffi/archive/v2.0.0/cffi-2.0.0.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  make
BuildRequires:  libffi-devel
BuildRequires:  gcc

# For tests:
BuildRequires:  gcc-c++

%description
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.


%package -n python3-cffi
Summary:        %{summary}

%description -n python3-cffi
Foreign Function Interface for Python, providing a convenient and
reliable way of calling existing C code from Python. The interface is
based on LuaJIT’s FFI.


%package doc
Summary:        Documentation for CFFI
BuildArch:      noarch
BuildRequires:  python3-sphinx

%description doc
Documentation for CFFI, the Foreign Function Interface for Python.


%prep
%oreon_verify_sources
%autosetup -p1 -n cffi-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

cd doc
make html
rm build/html/.buildinfo


%install
%pyproject_install
%pyproject_save_files _cffi_backend cffi


%check
%pytest


%files -n python3-cffi -f %{pyproject_files}
%doc README.md

%files doc
%license LICENSE
%doc doc/build/html


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.0-1
- Prepare for Oreon 11 (RP1)
