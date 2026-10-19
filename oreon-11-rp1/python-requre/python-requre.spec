%global source0_hash 3c3064c1ca3795730d63a5640944e1241b1f29752eaa7edcb803dba9fe5e85cc
%global desc %{expand:
REQUest REcordingRequre [rekure] - Is Library for storing output of various
function and methods to persistent storage and be able to replay the stored
output to functions.}
Name:           python-requre
Version:        0.9.1
Release:        1%{?dist}
Summary:        Python library that allows re/store output of various objects for testing
License:        MIT
URL:            https://github.com/packit/requre
Source0:        https://files.pythonhosted.org/packages/source/r/requre/requre-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-requre = %{version}-%{release}
# /oreon:deps
%package -n       python3-requre+testing
Summary:        Metapackage for python3-requre testing extras
Requires:       python3-requre = %{version}-%{release}
Provides:       python3dist(requre[testing]) = %{version}-%{release}

%description -n python3-requre+testing
Metapackage for python3-requre testing extras.

%description
%{desc}

%package -n     python3-requre
Summary:        Python library that allows re/store output of various objects for testing
%description -n python3-requre
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir requre-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-requre usr/lib/python3*/site-packages/requre* usr/lib64/python3*/site-packages/requre* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/requre* usr/lib64/python3*/site-packages/requre* usr/bin/*

%files
%files -n python3-requre -f %{oreon_filedir}/python3-requre.list

%changelog

%autochangelog
