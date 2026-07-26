%global source0_hash ca7111557df3ecda3cb48b6c5fb3290fa8b45b6226a34867d2a85cbee5747266

Name:           pybox2d
Version:        2.3.2
Release:        34%{?dist}
Summary:        A 2D rigid body simulation library for Python

License:        zlib
URL:            https://github.com/pybox2d/%{name}
Source0:        https://github.com/pybox2d/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Replace deprecated use of _swigconstant
# Upstream pull request: https://github.com/pybox2d/pybox2d/pull/90
Patch0:		replace-deprecated-swigconstant.patch

BuildRequires:  gcc gcc-c++
BuildRequires:  python3-devel
BuildRequires:  swig

%description
Programmer's can use Box2D in their games to make objects move in
believable ways and make the world seem more interactive. From the
game's point of view a physics engine is just a system for procedural
animation.

%package -n python3-%{name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
Programmer's can use Box2D in their games to make objects move in
believable ways and make the world seem more interactive. From the
game's point of view a physics engine is just a system for procedural
animation.

This package provides the Python 3 build of %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files Box2D
 
%files -n python3-%{name} -f %{pyproject_files}
%license LICENSE
%doc README.md examples/*

%changelog
%autochangelog
