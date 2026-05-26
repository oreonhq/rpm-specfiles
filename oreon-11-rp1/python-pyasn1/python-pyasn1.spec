# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 3f57055e9caa26338e353ee8c1107882ad36f60f300a3e65f33d5fbb12cf8846
%global source1_sha256 8cf7cfdf1bb976f8b60c7bd06439902d2c132412235c288af4b68a7a74378a78
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source1_sha256:%(test -z "%{source1_sha256}" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_sha256}" || { echo "oreon: Source1 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global module pyasn1
%global modules_version 0.4.1

Name:           python-pyasn1
Version:        0.6.2
Release:        1%{?dist}
Summary:        ASN.1 tools for Python
License:        BSD-2-Clause
Source0:        https://github.com/pyasn1/pyasn1/archive/v%{version}.tar.gz
Source1:        https://github.com/pyasn1/pyasn1-modules/archive/v%{modules_version}.tar.gz
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
%oreon_verify_sources
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
