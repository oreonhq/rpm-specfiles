%global source0_hash d8fa0bb17df5cbb2d95df95aad8abf5f48885f2b5820e97a3584273789613321
%{?python_enable_dependency_generator}
%bcond_without  docs
Name:           gcovr
Version:        8.6
Release:        1%{?dist}
Summary:        A code coverage report generator using GNU gcov
License:        BSD-3-Clause
URL:            https://gcovr.com/
Source0:        https://github.com/gcovr/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%if %{with docs}
%endif
Requires:       gcc
Requires:       %{py3_dist Jinja2}
Requires:       %{py3_dist colorlog}
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatch-fancy-pypi-readme) == 25.1.0
BuildRequires:  python3dist(hatch-vcs) == 0.5.0
BuildRequires:  python3dist(hatchling) == 1.27.0
Requires:       python3-gcovr = %{version}-%{release}
# /oreon:deps
%package -n       python3-gcovr+dev
Summary:        Metapackage for python3-gcovr dev extras
Requires:       python3-gcovr = %{version}-%{release}
Requires:       python3dist(pygments) == 2.19.2
Requires:       python3dist(pyinstaller) >= 6.16.0
Requires:       python3dist(pylint) < 4.0.0
Requires:       python3dist(ruff) >= 0.13.2
Requires:       python3dist(tomli) >= 1.1.0
Provides:       python3dist(gcovr[dev]) = %{version}-%{release}

%description -n python3-gcovr+dev
Metapackage for python3-gcovr dev extras.

%description
Gcovr provides a utility for managing the use of the GNU gcov utility
and generating summarized code coverage results.

This command is inspired by the Python coverage.py package, which provides
a similar utility in Python. The gcovr command produces either compact
human-readable summary reports, machine readable XML reports
(in Cobertura format) or simple HTML reports. Thus, gcovr can be viewed
as a command-line alternative to the lcov utility, which runs gcov and
generates an HTML-formatted report.

%if %{with docs}
%package        doc
Summary:        Documentation of gcovr
%description    doc
Documentation of gcovr.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Relax the strict version requirements.
sed -i -e "s/hatchling==1.27.0/hatchling/" -e "s/hatch-vcs==0.5.0/hatch-vcs/" -e "s/hatch-fancy-pypi-readme==25.1.0/hatch-fancy-pypi-readme/" pyproject.toml

%build

export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
%dnl %check
%dnl %pytest
%install
%pyproject_install
%if %{with docs}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHON=python3
pushd .
cd doc
sphinx-build -M man source build %{?fedora:-W}
install -D -p -m 0644 build/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
sphinx-build -M html source build %{?fedora:-W}
rm build/html/.buildinfo
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files
%files -n gcovr-doc -f %{oreon_filedir}/gcovr-doc.list

%changelog

%autochangelog
