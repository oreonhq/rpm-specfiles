%global source0_hash 5513527951aadb3ac4292a41a16cbc50dd1642432f5e8c20057d414bdafb4187

%global modname isort
%global srcname isort

Name:               python-%{modname}
Version:            7.0.0
Release:            2%{?dist}
Summary:            Python utility / library to sort Python imports

License:            MIT
URL:                https://github.com/timothycrosley/%{modname}
Source0:            %pypi_source
BuildArch:          noarch

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_pkgversion} version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

# Drop shebang
#sed -i -e '1{\@^#!.*@d}' %{modname}/main.py
#chmod -x LICENSE

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}
mv %{buildroot}%{_bindir}/%{modname}{,-%{python3_version}}
ln -s %{modname}-%{python3_version} %{buildroot}%{_bindir}/%{modname}-%{python3_pkgversion}
ln -s %{modname}-3 %{buildroot}%{_bindir}/%{modname}

# Re-enable once pylama is in Fedora.
#%check
#%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc *.md
%{_bindir}/%{modname}
%{_bindir}/%{modname}-%{python3_pkgversion}
%{_bindir}/%{modname}-%{python3_version}
%{_bindir}/%{modname}-identify-imports

%changelog
%autochangelog
