%global source0_hash c4319b3b3a46e6f8014246cd1e58d699d70cd5683643797b4653ca02532355ee
Name:           kalamine
Version:        0.40
Release:        1%{?dist}
Summary:        Cross-platform Keyboard Layout Maker
License:        MIT
URL:            https://github.com/OneDeadKey/kalamine
Source0:        https://files.pythonhosted.org/packages/source/k/kalamine/kalamine-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27
Requires:       python3-kalamine = %{version}-%{release}
# /oreon:deps
%package -n       python3-kalamine+dev
Summary:        Metapackage for python3-kalamine dev extras
Requires:       python3-kalamine = %{version}-%{release}
Requires:       python3dist(mypy) >= 1.13.0
Requires:       python3dist(ruff) >= 0.8.0
Requires:       python3dist(twine) >= 5.1.1
Requires:       python3dist(docutils) >= 0.22
Provides:       python3dist(kalamine[dev]) = %{version}-%{release}

%description -n python3-kalamine+dev
Metapackage for python3-kalamine dev extras.

%description
A text-based, cross-platform Keyboard Layout Maker.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# rpmlint: E: zero-length
mv kalamine/generators/{__init.py__,__init__.py}
# rpmlint: E: non-executable-script
sed -e '1{/^#!/d}' -i kalamine/{__init__.py,cli*.py}
# remove Windows-only CLI
sed -e '/wkalamine/d' -i pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%{py3_test_envvars} %{python3} -m kalamine.cli build layouts/*.toml
%{py3_test_envvars} %{python3} -m kalamine.cli new test.toml
%pytest
%files

%changelog

%autochangelog
