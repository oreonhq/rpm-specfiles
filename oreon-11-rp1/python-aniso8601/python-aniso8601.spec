%global source0_hash 25488f8663dd1528ae1f54f94ac1ea51ae25b4d531539b8bc707fed184d16845
Name:           python-aniso8601
Version:        10.0.1
Release:        1%{?dist}
Summary:        A library for parsing ISO 8601 strings.
License:        ...
URL:            https://codeberg.org/nielsenb-jf/aniso8601
Source0:        https://files.pythonhosted.org/packages/source/a/aniso8601/aniso8601-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-aniso8601 = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-aniso8601
Summary:        A library for parsing ISO 8601 strings.
%description -n python3-aniso8601

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir aniso8601-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-aniso8601 usr/lib/python3*/site-packages/aniso8601* usr/lib64/python3*/site-packages/aniso8601* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/aniso8601* usr/lib64/python3*/site-packages/aniso8601* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-aniso8601 -f %{oreon_filedir}/python3-aniso8601.list

%changelog

%autochangelog
