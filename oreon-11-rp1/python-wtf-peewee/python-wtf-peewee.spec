%global source0_hash 2d06ce5a0eb9acf4d22d154ae6fbea99db11b1768381c619e78a2ac60a561915

%global srcname wtf-peewee

Name:		python-wtf-peewee
Version:	3.0.5
Release:	11%{?dist}
Summary:	WTForms integration for peewee models

License:	MIT
URL:		https://github.com/coleifer/wtf-peewee/
Source0:	https://pypi.python.org/packages/source/w/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	pyproject-rpm-macros

%description
Wtf-peewee, based on the code found in wtforms.ext, provides a bridge between
peewee models and wtforms, mapping model fields to form fields.

%package -n python3-%{srcname}
Summary:        WTForms integration for peewee models

%description -n python3-%{srcname}
Wtf-peewee, based on the code found in wtforms.ext, provides a bridge between
peewee models and wtforms, mapping model fields to form fields.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

# Remove shebang and executable bits from runtests.py
chmod -x runtests.py
sed -i '1d' runtests.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files wtfpeewee

%check
%{python3} runtests.py

%files -n python3-%{srcname} -f %pyproject_files
%doc README.md
%license LICENSE

%changelog
%autochangelog
