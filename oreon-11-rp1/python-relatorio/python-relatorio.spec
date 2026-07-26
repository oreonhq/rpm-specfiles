%global source0_hash a0c72302d50d5dfa433ddab191672eec1dde1c6ed26330a378b720e5a3012e23

%global pypi_name relatorio
%global sum A templating library able to output odt and pdf files

Name:           python-%{pypi_name}
Version:        0.10.1
Release:        16%{?dist}
Summary:        %{sum}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pypi.org/project/relatorio/
Source0:	%{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-magic
BuildRequires:	pyproject-rpm-macros
%py_provides python3-%{pypi_name}

%description
A templating library which provides a way to easily output all kind of
different files (odt, ods, png, svg, ...). Adding support for more filetype
is easy: you just have to create a plugin for this.

relatorio also provides a report repository allowing you to link python
objects and report together, find reports by mimetypes/name/python objects.

%package -n python3-%{pypi_name}
Summary:        %{sum}

%description -n python3-%{pypi_name}
A templating library which provides a way to easily output all kind of
different files (odt, ods, png, svg, ...). Adding support for more filetype
is easy: you just have to create a plugin for this.

relatorio also provides a report repository allowing you to link python
objects and report together, find reports by mimetypes/name/python objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install	
%pyproject_install
%pyproject_save_files relatorio

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README
%{_bindir}/relatorio-render

%changelog
%autochangelog
