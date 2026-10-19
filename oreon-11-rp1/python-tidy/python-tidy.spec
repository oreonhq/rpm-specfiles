%global source0_hash 3c1fc9ce734d25568879a6daa27a9dd3f60c0bd7756d973bcc61757b5fcd6ef0
%global         oname uTidylib
Summary:        Python wrapper for tidy, from the HTML tidy project
Name:           python-tidy
Version:        0.6
Release:        1%{?dist}
License:        MIT
URL:            https://cihar.com/software/utidylib/
Source0:        http://dl.cihar.com/utidylib/uTidylib-%{version}.tar.bz2
Patch:          python-tidy-soname.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-tidy = %{version}-%{release}
# /oreon:deps
%description

%package     -n python3-tidy
Summary:        %summary
Requires:       libtidy
Requires:       python3-six
%description -n python3-tidy

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{oname}-%{version}

%build

%{pyproject_wheel}
%install
%{pyproject_install}
%oreon_autofiles python3-tidy usr/lib/python3*/site-packages/tidy* usr/lib64/python3*/site-packages/tidy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/tidy* usr/lib64/python3*/site-packages/tidy* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-tidy -f %{oreon_filedir}/python3-tidy.list

%changelog

%autochangelog
