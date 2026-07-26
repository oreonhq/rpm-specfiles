%global source0_hash 372138a738e4216535cc76dcce6eddd5a1aaca95130f2354fb834264c06f18de

%global modname pyramid
%global sum The Pyramid web application framework, a Pylons project
%global desc Pyramid is a small, fast, down-to-earth, open source Python web development\
framework. It makes real-world web application development and deployment more\
fun, more predictable, and more productive.

Name:           python-%{modname}
Version:        2.0.2
Release:        11%{?dist}
Summary:        %{sum}

License:        BSD-4-Clause
URL:            https://trypyramid.com/
Source0:        %pypi_source %{modname}

# Allow InstancePropertyHelper to accept properties with names on Python 3.13+
Patch:          https://github.com/Pylons/pyramid/pull/3762.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
%{desc}

%package -n python3-pyramid
Summary:        %{sum}

%description -n python3-pyramid
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pyramid-%{version} -p1

# Remove bundled egg info
rm -rf %{modname}.egg-info

%generate_buildrequires
%pyproject_buildrequires -x testing

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

# Create the Python 3 executables.
for e in pserve prequest proutes pshell ptweens pviews pdistreport; do
    mv %{buildroot}/%{_bindir}/$e %{buildroot}/%{_bindir}/$e-%{python3_version};
    ln -s %{_bindir}/$e-%{python3_version} %{buildroot}/%{_bindir}/$e-3;
    ln -s %{_bindir}/$e-%{python3_version} %{buildroot}/%{_bindir}/$e
done;

%check
%pyproject_check_import
%pytest tests

%files -n python3-%{modname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst
%{_bindir}/pdistreport-%{python3_version}
%{_bindir}/pdistreport-3
%{_bindir}/pdistreport
%{_bindir}/prequest-%{python3_version}
%{_bindir}/prequest-3
%{_bindir}/prequest
%{_bindir}/proutes-%{python3_version}
%{_bindir}/proutes-3
%{_bindir}/proutes
%{_bindir}/pserve-%{python3_version}
%{_bindir}/pserve-3
%{_bindir}/pserve
%{_bindir}/pshell-%{python3_version}
%{_bindir}/pshell-3
%{_bindir}/pshell
%{_bindir}/ptweens-%{python3_version}
%{_bindir}/ptweens-3
%{_bindir}/ptweens
%{_bindir}/pviews-%{python3_version}
%{_bindir}/pviews-3
%{_bindir}/pviews

%changelog
%autochangelog
