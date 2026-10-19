%global source0_hash 0395fa126940340215090c344a2bf4e2a77bcbe7daab16f41b37b98c95809ff9
%bcond bootstrap 0
%bcond tests %{without bootstrap}
Name:           python-hatch-vcs
Version:        0.5.0
Release:        1%{?dist}
Summary:        Hatch plugin for versioning with your preferred VCS
License:        MIT
URL:            https://github.com/ofek/hatch-vcs
Source0:        https://files.pythonhosted.org/packages/source/h/hatch-vcs/hatch_vcs-%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
%global common_description %{expand:
This provides a plugin for Hatch that uses your preferred version control
system (like Git) to determine project versions.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.1.0
Requires:       python3-hatch-vcs = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-hatch-vcs
Summary:        Hatch plugin for versioning with your preferred VCS
# oreon:reqs
Requires:       python3dist(hatchling) >= 1.1.0
Requires:       python3dist(setuptools-scm) >= 8.2.0
# /oreon:reqs
%description -n python3-hatch-vcs %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir hatch_vcs-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hatch-vcs usr/lib/python3*/site-packages/hatch_vcs* usr/lib64/python3*/site-packages/hatch_vcs* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hatch_vcs* usr/lib64/python3*/site-packages/hatch_vcs* usr/bin/*

%check

%if %{with tests}
%pyproject_check_import
%pytest
%endif
%files
%files -n python3-hatch-vcs -f %{oreon_filedir}/python3-hatch-vcs.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.0-1
- Import
