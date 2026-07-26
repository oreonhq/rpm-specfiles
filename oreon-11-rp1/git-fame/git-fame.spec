%global source0_hash e74319c409aed8c84fccb1695782c2d1b01178f32e85165ea87e4a1bedb24920

Name:           git-fame
Version:        2.0.1
Release:        14%{?dist}
Summary:        Pretty-print git repository collaborators sorted by contributions

License:        MPL-2.0
URL:            https://pypi.python.org/pypi/git-fame
Source0:        %{pypi_source}

BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
Requires:       git-core
Requires:       python%{python3_version}dist(argopt) >= 0.3.5
# Only for beautifulness
Recommends:     python%{python3_version}dist(tqdm)
Recommends:     python%{python3_version}dist(tabulate)

%description
Pretty-print git repository collaborators sorted by contributions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_libexecdir}/git-core
ln -s %{_bindir}/%{name} %{buildroot}%{_libexecdir}/git-core/%{name}
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 gitfame/git-fame.1

%check
# Tests depend on real git repo

%files
%license LICENCE
%doc README.rst
%{_bindir}/%{name}
%{_libexecdir}/git-core/%{name}
%{_mandir}/man1/%{name}.1*
%{python3_sitelib}/git_fame-*.egg-info/
%{python3_sitelib}/gitfame/

%changelog
%autochangelog
