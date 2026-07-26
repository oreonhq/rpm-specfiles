%global source0_hash 3c1fc9ce734d25568879a6daa27a9dd3f60c0bd7756d973bcc61757b5fcd6ef0

%global         oname uTidylib

Summary:        Python wrapper for tidy, from the HTML tidy project
Name:           python-tidy
Version:        0.6
Release:        25%{?dist}
License:        MIT
URL:            https://cihar.com/software/utidylib/
Source0:        http://dl.cihar.com/utidylib/uTidylib-%{version}.tar.bz2
Patch:          python-tidy-soname.patch
BuildRequires:  libtidy
BuildRequires:  python3-devel
BuildRequires:  python3-six
BuildArch:      noarch
%global         _description\
Python wrapper (bindings) for tidylib, this allows you to tidy HTML\
files through a Pythonic interface.

%description    %_description

%package     -n python3-tidy
Summary:        %summary
Requires:       libtidy
Requires:       python3-six
%description -n python3-tidy %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{oname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%{pyproject_wheel}

%install
%{pyproject_install}
%pyproject_save_files -l tidy

%check
%pyproject_check_import

%files -n python3-tidy -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
