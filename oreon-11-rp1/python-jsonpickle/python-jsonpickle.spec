%global source0_hash 3e650b9853adcdab9d9d62a88412b6d36e9a59ba423b01cacf0cd4ee80733aca

Name:           python-jsonpickle
# version is inserted into setup.cfg manually (see %%prep). Please be careful
# to use a Python-compatible version number if you need to set an "uncommon"
# version for this RPM.
Version:        4.0.2
Release:        7%{?dist}
Summary:        A module that allows any object to be serialized into JSON

License:        BSD-3-Clause
URL:            https://github.com/jsonpickle/jsonpickle
Source0:        %{pypi_source jsonpickle}

%global _docdir_fmt %{name}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
jsonpickle is a library for the two-way conversion of complex Python objects
and JSON. jsonpickle builds upon the existing JSON encoders, such as
simplejson, json, and ujson.}

%description %{_description}

%package -n python3-jsonpickle
Summary:        A module that allows any object to be serialized into JSON

%description -n python3-jsonpickle %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jsonpickle-%{version} -p1

sed -r -i 's/[[:blank:]]--cov[^[:blank:]]*//g' pytest.ini

sed -i /bson/d pyproject.toml
sed -i /pymongo/d pyproject.toml
sed -i /histogram/d pyproject.toml
sed -i /black\ /d pyproject.toml
sed -i /pytest-checkdocs\ /d pyproject.toml
sed -i /pytest-cov\ /d pyproject.toml
sed -i /pytest-flake8\ /d pyproject.toml
sed -i /pytest-enabler\ /d pyproject.toml
sed -i /pytest-ruff\ /d pyproject.toml
sed -i /atheris\ /d pyproject.toml

%if 0%{?el9}
# Not yet packaged:
# [RFE:EPEL9] EPEL9 branch for python-pandas
# https://bugzilla.redhat.com/show_bug.cgi?id=2032550
# (python-scikit-learn: no EPEL9 request yet)
sed -r -i -e 's/^([[:blank:]]*)(pandas|scikit-learn)/\1# \2/' setup.cfg
%endif

%generate_buildrequires
%pyproject_buildrequires -x testing,testing.libs

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jsonpickle

%check
%pytest %{?el9:--ignore=jsonpickle/ext/pandas.py} --ignore=fuzzing/

%files -n python3-jsonpickle -f %{pyproject_files}

%changelog
%autochangelog
