%global source0_hash 71d07ccc9514cb22fe59d98999577665eaab57e16f644d04336ae0b4bae234bc

%global srcname doit

Name:           python-%{srcname}
Version:        0.36.0
Release:        7%{?dist}
Summary:        Automation Tool

License:        MIT
URL:            https://pydoit.org/
Source0:        https://pypi.io/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
Patch1:         python-doit_ignore_versions.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  strace
BuildRequires:  python3-devel

%global _description %{expand:
python-doit is a build tool (in the same class as make, cmake, scons,
ant and others)

python-doit can be used as:
  * a build tool (generic and flexible)
  * home of your management scripts (it helps you organize and combine
   shell scripts and python scripts)
  * a functional tests runner (combine together different tools)
  * a configuration management system
  * manage computational pipelines}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_enable_dependency_generator}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%package -n python3-%{srcname}-doc
Summary:        Documentation for %{name}
Requires:       python3-%{srcname} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{srcname}-doc}

%description -n python3-%{srcname}-doc
%{name} documentation

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

find -type f -exec sed -i '1s=^#! /usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%generate_buildrequires
%pyproject_buildrequires dev_requirements.txt doc_requirements.txt -r

%build
%pyproject_wheel

cd doc
PYTHONPATH=.. make html SPHINXBUILD=sphinx-build-3
rm -rf _build/html/_sources/ _build/html/.buildinfo
cd -

%install
%pyproject_install

install -p -D -m 0644 bash_completion_doit %{buildroot}%{_sysconfdir}/bash_completion.d/doit
%pyproject_save_files %{srcname}

%check
# Is impossible to run tests because the testsuite is not ready for Python 3
# environment and there is also one unresolved test dependency doit-py
# %{__python3} -m pytest
%py3_check_import %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/doit
%license LICENSE
%doc README.rst
%{_sysconfdir}/bash_completion.d/doit

%files -n python3-%{srcname}-doc
%license LICENSE
# doc is not present in the tar ball (reported upstream)
#%doc doc/tutorial
%doc doc/_build/html
%doc CHANGES
%doc TODO.txt

%changelog
%autochangelog
