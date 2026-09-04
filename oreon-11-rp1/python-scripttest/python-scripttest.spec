%global source0_hash 99c406d3ee3f8e0e9cf82de5d6735975e879354297b20aa782bed6b6db337cf5

Name:           python-scripttest
Version:        3.0
Release:        %autorelease
Summary:        Helper to test command-line scripts

License:        MIT
URL:            http://pypi.python.org/pypi/ScriptTest/
Source:         https://github.com/pypa/scripttest/archive/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description
ScriptTest is a library to help you test your interactive 
command-line applications.

With it you can easily run the command (in a subprocess) and see 
the output (stdout, stderr) and any file modifications.

%package -n     python%{python3_pkgversion}-scripttest
Summary:        %{summary}

%description -n python%{python3_pkgversion}-scripttest
ScriptTest is a library to help you test your interactive 
command-line applications.

With it you can easily run the command (in a subprocess) and see 
the output (stdout, stderr) and any file modifications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n scripttest-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
# there is no LICENSE file
%pyproject_save_files -L scripttest

%check
%pytest -v

%files -n python%{python3_pkgversion}-scripttest -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
