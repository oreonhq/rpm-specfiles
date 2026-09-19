%global source0_hash cda8c9df3a365cc8eed901c5d76ed5757bd4c49a68225c345954afea91941f18

Name:           python-pysingular
Version:        0.9.7
Release:        29%{?dist}
Summary:        Python interface to Singular

License:        GPL-2.0-or-later
URL:            https://github.com/sebasguts/PySingular
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/PySingular-%{version}.tar.gz

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildSystem:    pyproject
BuildOption(install): -l PySingular

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Singular)

%global _description %{expand:This package contains a basic interface to call Singular from python.  It is
meant to be used in the Jupyter interface to Singular.}

%description
%_description

%package     -n python3-pysingular
Summary:        Python 3 interface to Singular

%description -n python3-pysingular
%_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n PySingular-%{version}

%files -n python3-pysingular -f %{pyproject_files}
%doc README
%license GPLv2

%changelog
%autochangelog
