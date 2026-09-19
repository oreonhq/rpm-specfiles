%global source0_hash 2b6e4a97454983166e9a5fe08aca41cd8b28288ef693b954bc0e8b8518eafd3b

%global srcname vcstool

Name:           python-%{srcname}
Version:        0.3.0
Release:        16%{?dist}
Summary:        Tool to invoke vcs commands on multiple repositories

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/dirk-thomas/%{srcname}
Source0:        https://github.com/dirk-thomas/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
Vcstool is a version control system (VCS) tool, designed to make working with
multiple repositories easier.

Note: This tool should not be confused with vcstools (with a trailing s) which
provides a Python API for interacting with different version control systems.
The biggest differences between the two are:

- vcstool doesn't use any state beside the repository working copies available
  in the filesystem.
- The file format of vcstool export uses the relative paths of the repositories
  as keys in YAML which avoids collisions by design.
- vcstool has significantly less lines of code than vcstools including the
  command line tools built on top.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  git
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-PyYAML
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-PyYAML
Requires:       python%{python3_pkgversion}-setuptools
%endif

%if !0%{?rhel} || 0%{?rhel} >= 8
Recommends:     git
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Vcstool is a version control system (VCS) tool, designed to make working with
multiple repositories easier.

Note: This tool should not be confused with vcstools (with a trailing s) which
provides a Python API for interacting with different version control systems.
The biggest differences between the two are:

- vcstool doesn't use any state beside the repository working copies available
  in the filesystem.
- The file format of vcstool export uses the relative paths of the repositories
  as keys in YAML which avoids collisions by design.
- vcstool has significantly less lines of code than vcstools including the
  command line tools built on top.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%build
%py3_build

%install
# There are three extra things we're doing here:
# 1. Making each executable available with a -X and -X.Y suffix
# 2. Giving each python version a directory of executables for %%check
# 3. Integrating with the bash-completion package

install -d %{buildroot}%{_datadir}/bash-completion/completions %{buildroot}%{_bindir}

%py3_install -- --install-scripts %{_bindir}%{python3_pkgversion}

echo -n "" > py3_bins
for f in `ls %{buildroot}%{_bindir}%{python3_pkgversion}`; do
  mv %{buildroot}%{_bindir}%{python3_pkgversion}/$f %{buildroot}%{_bindir}/$f-%{python3_version}
  ln -s $f-%{python3_version} %{buildroot}%{_bindir}/$f-3
  ln -s $f-%{python3_version} %{buildroot}%{_bindir}/$f
  echo -e "%{_bindir}/$f\n%{_bindir}/$f-3\n%{_bindir}/$f-%{python3_version}" >> py3_bins
done

# Integrate bash completion with the bash-completion package
cp -af %{buildroot}%{_datadir}/%{srcname}-completion/vcs.bash %{buildroot}%{_datadir}/bash-completion/completions/vcs
ln -sf vcs %{buildroot}%{_datadir}/bash-completion/completions/vcs-3
ln -s vcs %{buildroot}%{_datadir}/bash-completion/completions/vcs-%{python3_version}

%check
# We skip two classes of test:
# 1. Code style
# 2. Tests which require network access
%define pytest_options \\\
  --ignore=test/test_flake8.py \\\
  --ignore test/test_commands.py \\\
  test

PYTHONWARNINGS=ignore \
  %{__python3} -m pytest %pytest_options

%files -n python%{python3_pkgversion}-%{srcname} -f py3_bins
%license LICENSE
%doc CONTRIBUTING.md README.rst
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/
%{_datadir}/%{srcname}-completion
%{_datadir}/bash-completion/completions/vcs
%{_datadir}/bash-completion/completions/vcs-3
%{_datadir}/bash-completion/completions/vcs-%{python3_version}

%changelog
%autochangelog
