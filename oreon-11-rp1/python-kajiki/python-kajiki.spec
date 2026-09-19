%global source0_hash fe42d26abc4331982bde426d9f6f4848969868682a19c5882781d5a3e975cc69

%global modname kajiki

Name:               python-kajiki
Version:            1.0.2
Release:            7%{?dist}
Summary:            Really fast well-formed xml templates

License:            MIT
URL:                https://pypi.io/project/Kajiki
Source0:            %pypi_source kajiki

BuildArch:          noarch

BuildRequires:      python3-devel
#BuildRequires:      python3-setuptools
#BuildRequires:      python3-babel
BuildRequires:      python3-pytest

%description
Are you tired of the slow performance of Genshi? But you still long for the
assurance that your output is well-formed that you miss from all those
other templating engines? Do you wish you had Jinja's blocks with Genshi's
syntax? Then look  no further, Kajiki is for you! Kajiki quickly compiles
Genshi-like syntax to *real python bytecode* that renders with blazing-fast
speed! Don't delay! Pick up your copy of Kajiki today!

%package -n python3-kajiki
Summary:            Really fast well-formed xml templates
%{?python_provide:%python_provide python3-kajiki}

Requires:           python3-babel

%description -n python3-kajiki
Are you tired of the slow performance of Genshi? But you still long for the
assurance that your output is well-formed that you miss from all those
other templating engines? Do you wish you had Jinja's blocks with Genshi's
syntax? Then look  no further, Kajiki is for you! Kajiki quickly compiles
Genshi-like syntax to *real python bytecode* that renders with blazing-fast
speed! Don't delay! Pick up your copy of Kajiki today!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n kajiki-%{version} -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files kajiki

%check
%pytest

%files -n python3-kajiki -f %{pyproject_files}
%doc README.rst LICENSE.rst PKG-INFO
%{_bindir}/kajiki

%changelog
%autochangelog
