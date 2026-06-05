%global source0_hash 793c31816d952cee405b83488ce001c719f325d9cda69f1fc4cd750527640ea6

Name:           python-hatchling
Version:        1.29.0
Release:        %autorelease
Summary:        The build backend used by Hatch

# SPDX
License:        MIT
URL:            https://pypi.org/project/hatchling
Source0:        https://files.pythonhosted.org/packages/source/h/hatchling/hatchling-1.29.0.tar.gz#/python-hatchling-1.29.0.tar.gz
# Written for Fedora in groff_man(7) format based on --help output
Source100:      hatchling.1
Source200:      hatchling-build.1
Source300:      hatchling-dep.1
Source310:      hatchling-dep-synced.1
Source400:      hatchling-metadata.1
Source500:      hatchling-version.1

# We cannot run the “downstream integration tests” included with the PyPI sdist
# in an offline build. The primary tests are Hatch’s “backend” tests.

BuildArch:      noarch

%global common_description %{expand:
This is the extensible, standards compliant build backend used by Hatch.}

%description %{common_description}


%package -n python3-hatchling
Summary:        %{summary}

%description -n python3-hatchling %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n hatchling-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L hatchling
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE100}' \
    '%{SOURCE200}' \
    '%{SOURCE300}' '%{SOURCE310}' \
    '%{SOURCE400}' \
    '%{SOURCE500}'


%files -n python3-hatchling -f %{pyproject_files}
%doc README.md

%{_bindir}/hatchling
%{_mandir}/man1/hatchling.1*
%{_mandir}/man1/hatchling-*.1*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.29.0-1
- Import
