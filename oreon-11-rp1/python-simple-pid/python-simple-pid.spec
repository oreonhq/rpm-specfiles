%global source0_hash b7649cb8912435ef4f2f4f997b10f2b85757bc9ee79d94c4fab33f9d3b84dd5b

Name:		python-simple-pid
Version:	2.0.0
Release:	9%{?dist}
Summary:	A PID (proportional–integral–derivative) controller in Python

License:	MIT
URL:		https://github.com/m-lundberg/simple-pid
Source0:	%{pypi_source simple-pid}

BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-pytest

%global _description %{expand:
A simple and easy to use PID controller in Python. If you want a PID
controller without external dependencies that just works, this is for you!
The PID was designed to be robust with help from Brett Beauregards guide.}

%description %_description

%package -n python3-simple-pid
Summary:	A PID (proportional–integral–derivative) controller in Python

%description -n python3-simple-pid %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n simple-pid-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-simple-pid
%license LICENSE.md
%doc README.md
%{python3_sitelib}/simple_pid/
%{python3_sitelib}/simple_pid-%{version}.dist-info/

%changelog
%autochangelog
