%global source0_hash 5860ab66f077b7c8f21729f8ab69f3dbda15d3acf4c658a9b067e4a58b4c4876

Name:           python-perky
Version:        0.9.3
Release:        7%{?dist}
Summary:        A simple, Pythonic file format

License:        MIT
URL:            https://github.com/larryhastings/perky/
Source:         %{url}/archive/%{version}/perky-%{version}.tar.gz
Patch:          use-flit_core-instead-of-flit-to-build-wheel.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A friendly, easy, Pythonic text file format.
Perky is a new, simple "rcfile" text file format for Python programs. It solves
the same problem as "INI" files, "TOML" files, and "JSON" files, but with its
own opinion about how to best solve the problem.}

%description %{_description}

%package -n     python3-perky
Summary:        %{summary}

%description -n python3-perky %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n perky-%{version}
# Remove shebang from non-executable file
sed -i -e '1{\@^#!.*@d}' perky/utility.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files perky

%check
cd tests
%{py3_test_envvars} %{python3} -m unittest discover

%files -n python3-perky -f %{pyproject_files}
# I don't like relying on %%pyproject_save_files for this
%license LICENSE
%doc README.md

%changelog
%autochangelog
