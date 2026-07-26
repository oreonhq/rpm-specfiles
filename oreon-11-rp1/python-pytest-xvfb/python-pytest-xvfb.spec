%global source0_hash 5ec234651709d92cb13ef085cce01633b23407459f88ccd85c77d4a76c877d2f

Name:           python-pytest-xvfb
Version:        3.1.1
Release:        6%{?dist}
Summary:        A pytest plugin to run Xvfb for tests

License:        MIT
URL:            https://github.com/The-Compiler/pytest-xvfb
Source0:        %{url}/archive/v%{version}/pytest-xvfb-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-tkinter
BuildRequires:  tigervnc-server-minimal
BuildRequires:  xorg-x11-server-Xephyr
BuildRequires:  xorg-x11-xauth

%global _description %{expand:
With Xvfb and the plugin installed, your testsuite automatically runs with
Xvfb. This allows tests to be run without windows popping up during GUI tests
or on systems without a display (like a CI).

If Xvfb is not installed, the plugin does not run and your tests will still
work as normal. However, a warning message will print to standard output
letting you know that Xvfb is not installed.

If you're currently using xvfb-run in something like .travis.yml, simply remove
it and install this plugin instead - then you'll also have the benefits of Xvfb
locally.}

%description %_description

%package -n     python3-pytest-xvfb
Summary:        %{summary}

%description -n python3-pytest-xvfb %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pytest-xvfb-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_xvfb

%check
%pytest

%files -n python3-pytest-xvfb -f %{pyproject_files}
%doc CHANGELOG.rst README.rst

%changelog
%autochangelog
