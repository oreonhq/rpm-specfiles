%global source0_hash b1df640b7d5658b8d3807b42d51291ed3f24e43d4a059092c11495a3f7714fc9
Name:           python-annotated-doc
Version:        0.0.5
Release:        1%{?dist}
Summary:        Document parameters, class attributes, return types, and variables inline
License:        MIT
URL:            https://github.com/fastapi/annotated-doc
Source0:        https://github.com/fastapi/annotated-doc/archive/%{version}/annotated-doc-%{version}.tar.gz
BuildArch:      noarch
%global common_description %{expand:
Document parameters, class attributes, return types, and variables inline, with
Annotated.}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-annotated-doc = %{version}-%{release}
# /oreon:deps
%description %{common_description}

%package -n     python3-annotated-doc
Summary:        Document parameters, class attributes, return types, and variables inline
%description -n python3-annotated-doc %{common_description}

%prep

%autosetup -p1
# Do not upper-bound (SemVer-bound) the version of uv_build; we must work with
# what we have, and compatibility across SemVer boundaries is good in practice.
sed -r -i 's/"(uv_build *>= *[^:]+), *<[^"]+"/"\1"/' pyproject.toml

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-annotated-doc usr/lib/python3*/site-packages/annotated_doc* usr/lib64/python3*/site-packages/annotated_doc* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/annotated_doc* usr/lib64/python3*/site-packages/annotated_doc* usr/bin/*

%check

%pytest -v
%files
%files -n python3-annotated-doc -f %{oreon_filedir}/python3-annotated-doc.list

%changelog

%autochangelog
