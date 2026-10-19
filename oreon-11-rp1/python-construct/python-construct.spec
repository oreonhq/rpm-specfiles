%global source0_hash 4d2472f9684731e58cc9c56c463be63baa1447d674e0d66aeb5627b22f512c29
Summary:        A powerful declarative parser/builder for binary data
Name:           python-construct
Version:        2.10.70
Release:        1%{?dist}
License:        MIT
URL:            http://construct.readthedocs.org
Source0:        https://pypi.python.org/packages/source/c/construct/construct-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-construct = %{version}-%{release}
# /oreon:deps
%description
%package     -n python3-construct
Summary:        %summary
Requires:       python3-six
%description -n python3-construct

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir construct-%{version}
%oreon_prep
%build

%{pyproject_wheel}
%install
%{pyproject_install}
%oreon_autofiles python3-construct usr/lib/python3*/site-packages/construct* usr/lib64/python3*/site-packages/construct* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/construct* usr/lib64/python3*/site-packages/construct* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-construct -f %{oreon_filedir}/python3-construct.list

%changelog

%autochangelog
