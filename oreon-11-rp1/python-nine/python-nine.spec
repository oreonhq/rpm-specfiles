%global source0_hash 352a7dfe11953b7f4d128a847ae01ee74b1d9dfc952f82f3cb1f1dbd41e66ca9

%global modname nine

Name:               python-nine
Version:            1.2.0
Release:            6%{?dist}
Summary:            Python 2 / 3 compatibility, like six, but favouring Python 3

License:            LicenseRef-Fedora-Public-Domain
URL:                http://pypi.python.org/pypi/nine
Source0:            %pypi_source nine
BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-pytest

%generate_buildrequires
%pyproject_buildrequires

%global _description\
Let's write Python 3 right now!\
\
When the best Python 2/Python 3 compatibility modules -- especially the\
famous `*six* library invented by Benjamin Peterson\
<https://pypi.python.org/pypi/six>`_ -- were created, they were written\
from the point of view of a Python 2 programmer starting to grok Python 3.\
\
When thou writeth Python, thou shalt write Python 3 and, just for a while,\
ensure that the thing worketh on Python 2.7 and, possibly, even 2.6.\
\
Just before Python 2 is finally phased out, thine codebase shall look more\
like 3 than like 2.\
\
nine facilitates this new point of view. You can write code that is as\
3ish as possible while still supporting 2.6. Very comfortable for writing\
new projects.

%description %_description

%package -n python3-nine
Summary:            %{summary}
%{?python_provide:%python_provide python3-nine}

%description -n python3-nine  %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files nine

%check
%pytest

%files -n python3-nine -f %{pyproject_files}
%doc README.rst
%license LICENSE.rst

%changelog
%autochangelog
