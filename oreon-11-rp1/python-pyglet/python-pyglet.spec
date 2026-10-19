%global source0_hash ca90ee05532ced8330b8a8087ac2a7b69589b7fa7fb67f85aabe24aaf4ae42c0
Name:           python-pyglet
Version:        2.1.16
Release:        1%{?dist}
Summary:        pyglet is a cross-platform games and multimedia package.
License:        ...
URL:            https://pyglet.org
Source0:        https://files.pythonhosted.org/packages/source/p/pyglet/pyglet-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
BuildRequires:  python3dist(flit-core) >= 3.2
Requires:       python3-pyglet = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pyglet
Summary:        pyglet is a cross-platform games and multimedia package.
%description -n python3-pyglet

%prep
%global oreon_srcdir pyglet-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pyglet usr/lib/python3*/site-packages/pyglet* usr/lib64/python3*/site-packages/pyglet* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pyglet* usr/lib64/python3*/site-packages/pyglet* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pyglet -f %{oreon_filedir}/python3-pyglet.list

%changelog

%autochangelog
