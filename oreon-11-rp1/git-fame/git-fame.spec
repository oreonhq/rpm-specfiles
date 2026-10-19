%global source0_hash e74319c409aed8c84fccb1695782c2d1b01178f32e85165ea87e4a1bedb24920
Name:           git-fame
Version:        4.2.1
Release:        1%{?dist}
Summary:        Pretty-print git repository collaborators sorted by contributions
License:        MPL-2.0
URL:            https://pypi.python.org/pypi/git-fame
Source0:        https://files.pythonhosted.org/packages/source/g/git-fame/git-fame-%{version}.tar.gz
BuildArch:      noarch
Requires:       git-core
Requires:       python%{python3_version}dist(argopt) >= 0.3.5
Recommends:     python%{python3_version}dist(tqdm)
Recommends:     python%{python3_version}dist(tabulate)
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
# /oreon:deps
%description
Pretty-print git repository collaborators sorted by contributions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%py3_build
%install
%py3_install
mkdir -p %{buildroot}%{_libexecdir}/git-core
ln -s %{_bindir}/%{name} %{buildroot}%{_libexecdir}/git-core/%{name}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 gitfame/git-fame.1
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
