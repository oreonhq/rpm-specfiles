Name:           python-cffi
Version:        2.0.0
Release:        %autorelease
Summary:        Foreign Function Interface for Python to call C code
# cffi is MIT
# cffi/_imp_emulation.py has bits copied from CPython (PSF-2.0)
License:        MIT AND PSF-2.0
URL:            https://github.com/python-cffi/cffi
Source:        https://github.com/python-cffi/cffi/archive/v2.0.0/cffi-2.0.0.tar.gz
# oreon url source checksums begin
%global source0_sha256 e32bea840b50779a43dcaff13dcf6fa8bc29aa1b071c2cb4e27c1bd79114a202
%global source0_file cffi-2.0.0.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/cffi-2.0.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e32bea840b50779a43dcaff13dcf6fa8bc29aa1b071c2cb4e27c1bd79114a202" || { echo "oreon: Source0 SHA256 mismatch for cffi-2.0.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
