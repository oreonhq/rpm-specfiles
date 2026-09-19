%global source0_hash bfc16531d1246dd2558eb9b3a63aa37a9978672b956860dc5426da2343ebf366

Summary:        Python bindings for wc(s)width
Name:           python-cwcwidth
Version:        0.1.12
Release:        2%{?dist}
License:        MIT
URL:            https://github.com/sebastinas/cwcwidth
Source0:        %{pypi_source cwcwidth}
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.28
%global _description \
Python bindings for wc(s)widthcwcwidth provides Python bindings for \
wcwidth and wcswidth functions defined in POSIX.1-2001 and \
POSIX.1-2008 based on Cython . These functions compute the printable \
length of a unicode character/string on a terminal.
%description %_description

%package     -n python3-cwcwidth
Summary:        %{summary}
%description -n python3-cwcwidth %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cwcwidth-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cwcwidth

%check
%pyproject_check_import

(cd tests ; PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} -m unittest -v)

%files -n python3-cwcwidth -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
