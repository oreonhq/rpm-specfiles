%global source0_hash 4784c823dbe98e4dc3909b560857c64f5786bca01d00d16f2e3ae37a32a54174

%global pypi_name trio-websocket
%global pypi_name_underscore %(echo "%{pypi_name}" | tr '-' '_')

Name: python-%{pypi_name}
Summary: WebSocket implementation focused on safety and correctness
License: MIT

Version: 0.12.2
Release: 6%{?dist}

URL: https://github.com/python-trio/trio-websocket
Source: %{URL}/archive/%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: attr
BuildRequires: make
BuildRequires: pytest

BuildRequires: python3-devel
BuildRequires: python3-pytest-trio
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: python3-sphinxcontrib-trio
BuildRequires: python3-trustme

%global _description %{expand:
This library implements both server and client aspects of the the WebSocket
protocol, striving for safety, correctness, and ergonomics. It is based
on the wsproto project, which is a Sans-IO state machine that implements
the majority of the WebSocket protocol, including framing, codecs, and events.
This library handles I/O using the Trio framework.
This library passes the Autobahn Test Suite.
}

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %_description

%package doc
Summary: Documentation for %{pypi_name}
Provides: bundled(js-jquery)
Provides: bundled(nodejs-underscores)

%description doc
This package contains documentation (in HTML format)
for %{pypi_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

export PYTHONPATH="$(pwd)"
%make_build -C docs html PYTHON=python3 BUILDDIR=build
rm docs/build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files %{pypi_name_underscore}

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}

%files doc
%license LICENSE
%doc docs/build/html

%changelog
%autochangelog
