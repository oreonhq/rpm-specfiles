%global source0_hash bcb01efc0c83d3c9362e200b5359fe22e11b859962dd27e5bebf3ada7620ae2f

Name:             python-flake8
Version:          6.1.0
Release:          10%{?dist}
Summary:          Python code checking using pyflakes, pycodestyle, and mccabe

License:          MIT
URL:              https://github.com/PyCQA/flake8
Source:           %{url}/archive/%{version}/flake8-%{version}.tar.gz
# Support Python 3.14 - rebased
# https://github.com/PyCQA/flake8/commit/bdcd5c2c0afadaf
Patch:            Handle-escaped-braces-in-f-strings.patch
# https://github.com/PyCQA/flake8/commit/019424b80d3d7d
Patch:            Support-Python-3.14.patch

BuildArch:        noarch

BuildRequires:    python%{python3_pkgversion}-devel

# tox config mixes coverage and tests, so we specify this manually instead
BuildRequires:    python%{python3_pkgversion}-pytest

%description
Flake8 is a wrapper around PyFlakes, pycodestyle, and Ned's McCabe
script. It runs all the tools by launching the single flake8 script,
and displays the warnings in a per-file, merged output.

It also adds a few features: files that contain "# flake8: noqa" are
skipped, lines that contain a "# noqa" comment at the end will not
issue warnings, Git and Mercurial hooks are included, a McCabe
complexity checker is included, and it is extendable through
flake8.extension entry points.

%package -n python%{python3_pkgversion}-flake8
Summary:          %{summary}

%description -n python%{python3_pkgversion}-flake8
Flake8 is a wrapper around PyFlakes, pycodestyle, and Ned's McCabe
script. It runs all the tools by launching the single flake8 script,
and displays the warnings in a per-file, merged output.

It also adds a few features: files that contain "# flake8: noqa" are
skipped, lines that contain a "# noqa" comment at the end will not
issue warnings, Git and Mercurial hooks are included, a McCabe
complexity checker is included, and it is extendable through
flake8.extension entry points.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n flake8-%{version}
# Allow pycodestyle 2.12, https://bugzilla.redhat.com/2325146
sed -i 's/pycodestyle>=2.11.0,<2.12.0/pycodestyle>=2.11.0,<2.13.0/' setup.cfg

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flake8

# Backwards-compatibility symbolic links from when we had both Python 2 and 3
ln -s flake8 %{buildroot}%{_bindir}/flake8-3
ln -s flake8 %{buildroot}%{_bindir}/flake8-%{python3_version}
ln -s flake8 %{buildroot}%{_bindir}/python3-flake8

%check
# skip test_all_pyflakes_messages_have_flake8_codes_assigned for now
# missing Python 3.14 compat - upstream only fixes things on released pyflakes
%pytest -v -k "not test_all_pyflakes_messages_have_flake8_codes_assigned"

%files -n python%{python3_pkgversion}-flake8 -f %{pyproject_files}
%doc README.rst CONTRIBUTORS.txt
%{_bindir}/flake8
%{_bindir}/flake8-3
%{_bindir}/flake8-%{python3_version}
%{_bindir}/python3-flake8

%changelog
%autochangelog
