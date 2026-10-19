%global source0_hash cca3e59494558640af52add7b8636cfa82eba72871a21cbbdc0a6f2000a4e5b7
Name:           python-jinja2-cli
Version:        1.0.1
Release:        1%{?dist}
Summary:        The CLI for Jinja2
License:        ...
URL:            https://github.com/mattrobenolt/jinja2-cli
Source0:        https://files.pythonhosted.org/packages/source/j/jinja2_cli/jinja2_cli-%{version}.tar.gz
BuildArch:      noarch
Patch:          138.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.10.0
BuildRequires:  python3dist(uv-build) >= 0.9.0
Requires:       python3-jinja2-cli = %{version}-%{release}
# /oreon:deps
%package -n       python3-jinja2-cli+yaml
Summary:        Metapackage for python3-jinja2-cli yaml extras
Requires:       python3-jinja2-cli = %{version}-%{release}
Provides:       python3dist(jinja2-cli[yaml]) = %{version}-%{release}

%description -n python3-jinja2-cli+yaml
Metapackage for python3-jinja2-cli yaml extras.

%package -n       python3-jinja2-cli+toml
Summary:        Metapackage for python3-jinja2-cli toml extras
Requires:       python3-jinja2-cli = %{version}-%{release}
Provides:       python3dist(jinja2-cli[toml]) = %{version}-%{release}

%description -n python3-jinja2-cli+toml
Metapackage for python3-jinja2-cli toml extras.

%package -n       python3-jinja2-cli+xml
Summary:        Metapackage for python3-jinja2-cli xml extras
Requires:       python3-jinja2-cli = %{version}-%{release}
Provides:       python3dist(jinja2-cli[xml]) = %{version}-%{release}

%description -n python3-jinja2-cli+xml
Metapackage for python3-jinja2-cli xml extras.

%package -n       python3-jinja2-cli+hjson
Summary:        Metapackage for python3-jinja2-cli hjson extras
Requires:       python3-jinja2-cli = %{version}-%{release}
Provides:       python3dist(jinja2-cli[hjson]) = %{version}-%{release}

%description -n python3-jinja2-cli+hjson
Metapackage for python3-jinja2-cli hjson extras.

%package -n       python3-jinja2-cli+json5
Summary:        Metapackage for python3-jinja2-cli json5 extras
Requires:       python3-jinja2-cli = %{version}-%{release}
Provides:       python3dist(jinja2-cli[json5]) = %{version}-%{release}

%description -n python3-jinja2-cli+json5
Metapackage for python3-jinja2-cli json5 extras.

%description

%package -n     python3-jinja2-cli
Summary:        The CLI for Jinja2
# oreon:reqs
Requires:       python3dist(jinja2) >= 3.1
# /oreon:reqs
%description -n python3-jinja2-cli

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir jinja2_cli-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-jinja2-cli usr/lib/python3*/site-packages/jinja2_cli* usr/lib64/python3*/site-packages/jinja2_cli* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/jinja2_cli* usr/lib64/python3*/site-packages/jinja2_cli* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-jinja2-cli -f %{oreon_filedir}/python3-jinja2-cli.list

%changelog

%autochangelog
