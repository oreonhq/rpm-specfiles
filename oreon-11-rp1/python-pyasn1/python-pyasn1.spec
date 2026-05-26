%global module pyasn1
%global modules_version 0.4.1

Name:           python-pyasn1
Version:        0.6.2
Release:        1%{?dist}
Summary:        ASN.1 tools for Python
License:        BSD-2-Clause
Source0:        https://github.com/pyasn1/pyasn1/archive/v%{version}.tar.gz
Source1:        https://github.com/pyasn1/pyasn1-modules/archive/v%{modules_version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 3f57055e9caa26338e353ee8c1107882ad36f60f300a3e65f33d5fbb12cf8846
%global source0_file v0.6.2.tar.gz
%global source1_sha256 8cf7cfdf1bb976f8b60c7bd06439902d2c132412235c288af4b68a7a74378a78
%global source1_file v0.4.1.tar.gz
# oreon url source checksums end
URL:            https://github.com/pyasn1/pyasn1
BuildArch:      noarch

%description
This is an implementation of ASN.1 types and codecs in the Python programming
language.

%package -n python3-pyasn1
Summary:    ASN.1 tools for Python 3
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-pyasn1
This is an implementation of ASN.1 types and codecs in the Python 3 programming
language.

%package -n python3-pyasn1-modules
Summary:    Modules for pyasn1
Requires:   python3-pyasn1 >= 0.4.7, python3-pyasn1 < 0.7.0

%description -n python3-pyasn1-modules
ASN.1 types modules for python3-pyasn1.

%package doc
Summary:        Documentation for pyasn1
BuildRequires:  make
BuildRequires:  python3-sphinx

%description doc
%{summary}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/v0.6.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3f57055e9caa26338e353ee8c1107882ad36f60f300a3e65f33d5fbb12cf8846" || { echo "oreon: Source0 SHA256 mismatch for v0.6.2.tar.gz" >&2; exit 1; })
%(f=%{_sourcedir}/v0.4.1.tar.gz; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8cf7cfdf1bb976f8b60c7bd06439902d2c132412235c288af4b68a7a74378a78" || { echo "oreon: Source1 SHA256 mismatch for v0.4.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -n %{module}-%{version} -q -b1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

pushd ../pyasn1-modules-%{modules_version}
%pyproject_wheel
popd

pushd docs
PYTHONPATH=%{buildroot}%{python3_sitelib} make SPHINXBUILD=sphinx-build-3 html
popd


%install
%pyproject_install


%check
%pytest


%files -n python3-pyasn1
%doc README.md
%license LICENSE.rst
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}.dist-info/

%files -n python3-pyasn1-modules
%{python3_sitelib}/%{module}_modules/
%{python3_sitelib}/%{module}_modules-%{modules_version}.dist-info/

%files doc
%license LICENSE.rst
%doc docs/build/html/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.2-1
- Prepare for Oreon 11 (RP1)
