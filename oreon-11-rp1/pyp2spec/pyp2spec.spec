%global source0_hash 535f31358402ad9626127b50ecb20bbdc347dcc1d0376953453c88f2143c9dec
Name:           pyp2spec
Version:        0.16.0
Release:        1%{?dist}
Summary:        Generate Fedora RPM spec files for Python projects
License:        MIT AND MIT-0
URL:            https://github.com/befeleme/pyp2spec
Source0:        https://files.pythonhosted.org/packages/source/p/pyp2spec/pyp2spec-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyp2spec = %{version}-%{release}
# /oreon:deps
%package -n       python3-pyp2spec+test
Summary:        Metapackage for python3-pyp2spec test extras
Requires:       python3-pyp2spec = %{version}-%{release}
Provides:       python3dist(pyp2spec[test]) = %{version}-%{release}

%description -n python3-pyp2spec+test
Metapackage for python3-pyp2spec test extras.

%description
pyp2spec is a tech preview. It is a tool generating Fedora RPM spec files
for Python distributions. It utilizes the benefits of pyproject-rpm-macros.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyp2spec-%{version}

# Remove the compat shims when Fedora 42 is EOL
# Older setuptools can't deal with the PEP 639 metadata declaration
sed -i "s/license = \"MIT AND MIT-0\"/license.text = \"MIT AND MIT-0\"/" pyproject.toml
sed -i "/license-files/d" pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%tox
%files

%changelog

%autochangelog
