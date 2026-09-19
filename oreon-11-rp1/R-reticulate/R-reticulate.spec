%global source0_hash 2e714a832a5d7c48c539f1725850e04419565a4437caaa627435f5cc4c161382

Name:           R-reticulate
Version:        %R_rpm_version 1.44.1
Release:        %autorelease
Summary:        R Interface to 'Python'

License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy)
Requires:       python3

%description
Interface to Python modules, classes, and functions. When calling into Python,
R data types are automatically converted to their equivalent Python types. When
values are returned from Python to R they are converted back to R types.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
sed -i 's/# skip_if_offline/skip/' \
    reticulate/tests/testthat/test-python-source.R

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%py_byte_compile %{python3} %{buildroot}%{_R_libdir}/reticulate/python/rpytools
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
