%global source0_hash 4feae057a2334c9a513e6933cdb9be819d8b822f3b5b435a36138bd218897d23
Name:           reuse
Version:        6.2.0
Release:        1%{?dist}
Summary:        A tool for compliance with the REUSE recommendations
License:        Apache-2.0 AND CC0-1.0 AND CC-BY-SA-4.0 AND GPL-3.0-or-later
Url:            https://github.com/fsfe/reuse-tool
Source0:        https://files.pythonhosted.org/packages/source/r/%{name}/%{name}-%{version}.tar.gz
Patch: 0001-use-python-file-magic-for-filetype-detection.patch
Recommends:     git
Recommends:     mercurial
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.1.0
Requires:       python3-reuse = %{version}-%{release}
# /oreon:deps
%description
A tool for compliance with the REUSE recommendations. Essentially,
it is a linter that checks for a project's compliance, and a compiler that
generates a project's bill of materials.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
pushd docs
PBR_VERSION=%{version} sphinx-build-%{python3_version} . html
PBR_VERSION=%{version} sphinx-build-%{python3_version} -b man . manpages
rm -rf {html,man}/.{doctrees,buildinfo}
popd
%install
%pyproject_install
install -p -m0644 -Dt "${RPM_BUILD_ROOT}%{_mandir}/man1" docs/manpages/*.1
%oreon_autofiles main

%check

%{pytest} tests/ "${RPM_BUILD_ROOT}/%{python3_sitearch}/reuse/"
%files

%changelog

%autochangelog
