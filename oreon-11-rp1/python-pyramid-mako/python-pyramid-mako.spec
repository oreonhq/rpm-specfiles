%global source0_hash 0066c863441f1c3ddea60cee1ccc50d00a91a317a8052ca44131da1a12a840e2
Name:           python-pyramid-mako
Version:        1.1.0
Release:        1%{?dist}
Summary:        Mako template bindings for the Pyramid web framework
License:        ...
URL:            https://docs.pylonsproject.org/projects/pyramid_mako/en/latest/
Source0:        https://files.pythonhosted.org/packages/source/p/pyramid_mako/pyramid_mako-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyramid-mako = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyramid-mako
Summary:        Mako template bindings for the Pyramid web framework
%description -n python3-pyramid-mako

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir pyramid_mako-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyramid-mako usr/lib/python3*/site-packages/pyramid_mako* usr/lib64/python3*/site-packages/pyramid_mako* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyramid_mako* usr/lib64/python3*/site-packages/pyramid_mako* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyramid-mako -f %{oreon_filedir}/python3-pyramid-mako.list

%changelog

%autochangelog
