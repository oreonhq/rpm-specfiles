%global source0_hash 72d2b99a5e50ca852c4fe85d21e1b818a29ca6a9430399c3b8c4d8a3d8d6cca5

Name:           shyaml
Version:        0.6.2
Release:        %autorelease
Summary:        YAML for command line

License:        BSD-2-Clause
URL:            https://github.com/0k/shyaml
Source0:        https://github.com/0k/shyaml/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Avoids the need to run autogen.sh during setup (which requires the complete
# git repository). Recreate by running './autogen.sh' in a local git checkout
Patch0:         %{name}.autogen.patch
# Remove CHANGELOG from the files to install, as it does not exist.
Patch1:         %{name}.filelist.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%generate_buildrequires
%pyproject_buildrequires

%description
Simple scripts that allow read access to YAML files through command line.  This
can be handy, if you want to get access to YAML data in your shell scripts.
This scripts supports only read access and it might not support all the
subtleties of YAML specification. But it should support some handy basic query
of YAML file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%{_bindir}/shyaml

%changelog
%autochangelog
