%global source0_hash 26166de53d9da3eccc52570bf8c2853e60efefd9e90e26fdfc7124fe0bd873af
%global modname scour
%global sum     An SVG scrubber
Name:               python-scour
Version:            0.38.2
Release:        1%{?dist}
Summary:        An SVG scrubber
License:            Apache-2.0 AND BSD-3-Clause
URL:                https://github.com/scour-project/scour
Source0:        https://github.com/scour-project/scour/archive/refs/tags/v0.38.2.tar.gz#/scour-0.38.2.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-scour = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-%{modname}
Summary:            %{sum}
%{?python_provide:%python_provide python3-%{modname}}
Requires: python3-packaging
%description -n python3-%{modname}
Scour is an SVG optimizer/cleaner written in Python that reduces the
size of scalable vector graphics by optimizing structure and removing
unnecessary data.

It can be used to create streamlined vector graphics suitable for web
deployment, publishing/sharing or further processing.

The goal of Scour is to output a file that renders identically at a
fraction of the size by removing a lot of redundant information created
by most SVG editors. Optimization options are typically lossless but can
be tweaked for more aggressive cleaning.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{modname}-%{version}

# Better safe than sorry
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'
find . -type f -name '*.py' -exec sed -i /env\ python/d {} ';'

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/scour* usr/lib64/python3*/site-packages/scour* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-scour -f %{oreon_filedir}/python3-scour.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.38.2-17
- Prepare for Oreon 11 (RP1)
