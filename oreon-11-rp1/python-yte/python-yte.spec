%global source0_hash b55072f942bfbaa37bcf67455201c14be0ff9f3f85c267bb95c39a9515cc3647
Name:           python-yte
Version:        1.9.4
Release:        1%{?dist}
Summary:        YAML template engine with Python expressions
License:        MIT
URL:            https://github.com/yte-template-engine/yte
Source0:        https://github.com/yte-template-engine/yte/archive/v%{version}/yte-%{version}.tar.gz
Source1:        yte.1
BuildArch:      noarch
%global common_description %{expand:
YTE is a template engine for YAML format that utilizes the YAML structure in
combination with Python expressions for enabling to dynamically build YAML
documents.
The key idea of YTE is to rely on the YAML structure to enable conditionals,
loops and other arbitrary Python expressions to dynamically render YAML files.
Python expressions are thereby declared by prepending them with a ? anywhere in
the YAML. Any such value will be automatically evaluated by YTE, yielding plain
YAML as a result. Importantly, YTE templates are still valid YAML files (for
YAML, the ? expressions are just strings).
Documentation of YTE can be found at https://yte-template-engine.github.io.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-yte = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n python3-yte
Summary:        YAML template engine with Python expressions
# oreon:reqs
Requires:       python3dist(argparse-dataclass) < 3
Requires:       python3dist(argparse-dataclass) >= 2.0.0
Requires:       python3dist(dpath) < 3.0
Requires:       python3dist(dpath) >= 2.1
Requires:       python3dist(pyyaml) < 7.0
Requires:       python3dist(pyyaml) >= 6.0
# /oreon:reqs
%description -n python3-yte %{common_description}

%install
%pyproject_install
install -t '%{buildroot}%{_mandir}/man1' -m 0644 -p -D '%{SOURCE1}'
%oreon_autofiles python3-yte usr/lib/python3*/site-packages/yte* usr/lib64/python3*/site-packages/yte* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/yte* usr/lib64/python3*/site-packages/yte* usr/bin/*

%prep
%oreon_prep
%build

%pyproject_wheel
%check

%pytest -v
%files
%files -n python3-yte -f %{oreon_filedir}/python3-yte.list

%changelog

%autochangelog
