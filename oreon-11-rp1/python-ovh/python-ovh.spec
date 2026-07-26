%global source0_hash b24a47bc37ffb14fee2d9525b4aa0b86eeb2aab24755fd6e74707c4e4d0b807a

Name:           python-ovh
Version:        1.1.2
Release:        8%{?dist}
Summary:        Lightweight wrapper around OVHcloud's APIs

License:        BSD
URL:            https://github.com/ovh/python-ovh
Source:         %{url}/archive/v%{version}/python-ovh-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# For building man pages
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pytest)

%global _description %{expand:
Lightweight wrapper around OVHcloud's APIs. Handles all the hard work
including credential creation and requests signing.
}

%description %_description

%package -n python3-ovh
Summary:        %{summary}

%description -n python3-ovh %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n python-ovh-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel
cd docs/ && make man

%install
%pyproject_install
%pyproject_save_files ovh

mkdir -p %{buildroot}/%{_mandir}/man1/
install -m 0644 docs/_build/man/python-ovh.1* %{buildroot}/%{_mandir}/man1/

%check
# Deselect network-dependent tests
%pytest --deselect tests/test_client.py::TestClient::test_endpoints

%files -n python3-ovh -f %{pyproject_files}
%doc examples/ README.rst
%{_mandir}/man1/python-ovh.1*

%changelog
%autochangelog
