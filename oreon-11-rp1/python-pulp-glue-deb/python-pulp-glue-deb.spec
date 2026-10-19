%global source0_hash 5a0304326316beb4e66dc9af38d2ad6cc5340cd2784c9ade4247c11e5981f443
Name:           python-pulp-glue-deb
Version:        0.5.0
Release:        1%{?dist}
Summary:        Version agnostic glue library to talk to pulpcore_s REST API. _deb plugin_
License:        GPL-2.0-or-later
URL:            https://github.com/pulp/pulp-cli-deb
Source0:        https://files.pythonhosted.org/packages/source/p/pulp_glue_deb/pulp_glue_deb-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pulp-glue-deb = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pulp-glue-deb
Summary:        Version agnostic glue library to talk to pulpcore_s REST API. _deb plugin_
# oreon:reqs
Requires:       python3dist(pulp-glue) < 0.41
Requires:       python3dist(pulp-glue) >= 0.23.2
# /oreon:reqs
%description -n python3-pulp-glue-deb

%prep
%global oreon_srcdir pulp_glue_deb-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pulp-glue-deb usr/lib/python3*/site-packages/pulp_glue_deb* usr/lib64/python3*/site-packages/pulp_glue_deb* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pulp_glue_deb* usr/lib64/python3*/site-packages/pulp_glue_deb* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pulp-glue-deb -f %{oreon_filedir}/python3-pulp-glue-deb.list

%changelog

%autochangelog
