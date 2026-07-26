%global source0_hash 143639a897390c6f6c02ad93c7b52120faf49b14c331d07066e7f9fffd7fa38a

# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# Setup _pkgdocdir if not defined already.
%{!?_py3docdir:%global _py3docdir	%{_docdir}/python3-%{pypi_name}%{!?_pkgdocdir:-%{version}}}
%{!?_pkgdocdir:%global _pkgdocdir	%{_docdir}/%{name}-%{version}}

# Settings used for build from snapshots.
%{!?rel_build:%global commit		ab2dc2db9db979816a4a7c4fd269ad2f27ef2d0b}
%{!?rel_build:%global commit_date	20150104}
%{!?rel_build:%global shortcommit	%(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global gitver		git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global gitrel		.git%{commit_date}.%{shortcommit}}

# Proper naming for the tarball from github.
%global gittar %{name}-%{version}%{!?rel_build:-%{gitver}}.tar.gz

# Upstream name
%global pypi_name django-angular

Name:			python-%{pypi_name}
Version:		2.0.3
Release:		27%{?gitrel}%{?dist}
Summary:		Classes and utility functions to integrate AngularJS with Django

License:		MIT
URL:			https://github.com/jrief/%{pypi_name}
# Sources for release-builds.
%{?rel_build:Source0:	%{url}/archive/%{version}.tar.gz#/%{gittar}}
# Sources for snapshot-builds.
%{!?rel_build:Source0:	%{url}/archive/%{commit}.tar.gz#/%{gittar}}

BuildArch:		noarch

%description
Django-Angular is a collection of utilities, which aim to ease the
integration of Django with AngularJS by providing reusable components.

%package -n python3-%{pypi_name}
Summary:		Classes and utility functions to integrate AngularJS with Django

BuildRequires: make
BuildRequires:		python3-devel
BuildRequires:		python3-setuptools

Requires:		python3-six
Requires:		python3-django

Obsoletes:		python2-%{pypi_name} < 1.1.2-2
Obsoletes:		python-%{pypi_name} < 1.1.2-2

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Django-Angular is a collection of utilities, which aim to ease the
integration of Django with AngularJS by providing reusable components.

%package -n python3-%{pypi_name}-doc
Summary:		Documentation-files for python3-%{pypi_name}

BuildRequires:		dos2unix
BuildRequires:		python3-sphinx

Obsoletes:		python2-%{pypi_name}-doc < 1.1.2-2
Obsoletes:		python-%{pypi_name}-doc < 1.1.2-2

%{?python_provide:%python_provide python3-%{pypi_name}-doc}

%description -n python3-%{pypi_name}-doc
This package contains the documentation-files for python3-%{pypi_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?rel_build}
%autosetup -n %{pypi_name}-%{version} -p 1
%else
%autosetup -n %{pypi_name}-%{commit} -p 1
%endif

# Remove bundled egg-info and unneded files.
%{__rm} -rf *.egg-info examples/.coveragerc

# Fix hashbangs.
for _file in $(%{__grep} -Rle '^#![ \t]*/usr/bin/env[ \t]*python' .)
do
  %{__sed} -e 's~^#![ \t]*/usr/bin/env[ \t]*python.*$~#!%{__python3}~'	\
	< ${_file} > ${_file}.new
  /bin/touch -r ${_file} ${_file}.new
  %{__mv} -f ${_file}.new ${_file}
done

%build
%py3_build

# Documentation
pushd docs
%make_build html SPHINXBUILD=sphinx-build-3
%{__rm} -f _build/html/{.buildinfo,objects.inv}
%{_bindir}/find _build/html -type f -print0 |				\
	%{_bindir}/xargs -0 %{_bindir}/dos2unix -k -o -s
popd

%install
%py3_install

# Documentation
%{__mkdir} -p %{buildroot}%{?_py3docdir}
%{__cp} -a CONTRIBUTING.md README.md docs/_build/html client examples	\
		%{buildroot}%{?_py3docdir}
%if 0%{?rhel} && 0%{?rhel} <= 6
%{__cp} -a LICENSE.txt %{buildroot}%{?_py3docdir}
%endif

%check
# noop

%files -n python3-%{pypi_name}
%doc %dir %{?_py3docdir}
%if 0%{fedora} || 0%{?rhel} >= 7
%license LICENSE.txt
%else
%doc %{?_py3docdir}/LICENSE.txt
%endif
%{python3_sitelib}/djng
%{python3_sitelib}/django_angular-%{version}-py%{python3_version}.egg-info

%files -n python3-%{pypi_name}-doc
%if 0%{fedora} || 0%{?rhel} >= 7
%license %{_datadir}/licenses/python3-%{pypi_name}*
%endif
%doc %{?_py3docdir}

%changelog
%autochangelog
