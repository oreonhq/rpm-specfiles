%global source0_hash 33f48c8d2337db539865265ce33c7c50e4d521aacbd31ac7b7e8b189d771ce1d

%global pname fypp

Name: python-%{pname}
Version: 3.2
Release: 12%{?dist}
Summary: Fortran preprocessor
License: BSD-2-Clause
URL: https://github.com/aradi/fypp
Source0: %{url}/archive/%{version}/%{pname}-%{version}.tar.gz
BuildArch: noarch

%global desc Fypp is a Python powered preprocessor. It can be used for any programming\
languages but its primary aim is to offer a Fortran preprocessor, which helps\
to extend Fortran with condititional compiling and template metaprogramming\
capabilities. Instead of introducing its own expression syntax, it uses Python\
expressions in its preprocessor directives, offering the consistency and\
versatility of Python when formulating metaprogramming tasks. It puts strong\
emphasis on robustness and on neat integration into developing toolchains.

%description
%{desc}

%package -n python3-%{pname}
Summary: %{summary}
BuildRequires: python3-devel

%description -n python3-%{pname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pname}

%check
%pyproject_check_import
test/runtests.sh %{__python3}

%files -n python3-%{pname} -f %{pyproject_files}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%{_bindir}/%{pname}

%changelog
%autochangelog
