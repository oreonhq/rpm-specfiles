%global source0_hash 6b351bbb12dd58af57ffef05bc78425d08d1914e0fd68ee14143b7ade023c5bc

%global srcname WTForms

Name:           python-wtforms
Version:        3.0.1
Release:        20%{?dist}
Summary:        Forms validation and rendering library for python

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://wtforms.simplecodes.com/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
With wtforms, your form field HTML can be generated for you.
This allows you to maintain separation of code and presentation,
and keep those messy parameters out of your python code.

%package -n python3-wtforms
Summary:        Forms validation and rendering library for python

%description -n python3-wtforms
With wtforms, your form field HTML can be generated for you.
This allows you to maintain separation of code and presentation,
and keep those messy parameters out of your python code.

%pyproject_extras_subpkg -n python3-wtforms email

%generate_buildrequires
%pyproject_buildrequires -rx email

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files wtforms

%check
%py3_check_import wtforms

%files -n python3-wtforms -f %{pyproject_files}
%doc docs/ README.rst CHANGES.rst
%license LICENSE.rst

%changelog
%autochangelog
