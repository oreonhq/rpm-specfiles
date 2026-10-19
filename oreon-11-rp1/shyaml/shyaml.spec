%global source0_hash 72d2b99a5e50ca852c4fe85d21e1b818a29ca6a9430399c3b8c4d8a3d8d6cca5
Name:           shyaml
Version:        0.6.2
Release:        1%{?dist}
Summary:        YAML for command line
License:        BSD-2-Clause
URL:            https://github.com/0k/shyaml
Source0:        https://github.com/0k/shyaml/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}.autogen.patch
Patch1:         %{name}.filelist.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-shyaml = %{version}-%{release}
# /oreon:deps
%description
Simple scripts that allow read access to YAML files through command line.  This
can be handy, if you want to get access to YAML data in your shell scripts.
This scripts supports only read access and it might not support all the
subtleties of YAML specification. But it should support some handy basic query
of YAML file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%files

%changelog

%autochangelog
