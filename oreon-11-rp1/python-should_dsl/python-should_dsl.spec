%global source0_hash 36f753d90fbdf84ef2b7a9e07813e3efac725376feb7a793549f3fff7a03232a

Summary:	Should assertions in Python in as clear and readable a way as possible
Name:		python-should_dsl
Version:	2.1.2
Release:	24%{?dist}
License:	MIT
URL:		https://github.com/nsi-iff/should-dsl
Source0:	https://files.pythonhosted.org/packages/source/s/should_dsl/should_dsl-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel

%global _description %{expand:
The goal of Should-DSL is to write should expectations in Python in as clear
and readable a way as possible, using "almost" natural language (limited -
sometimes - by the Python language constraints).}

%description %_description

%package -n python3-should_dsl
Summary:	Should assertions in Python in as clear and readable a way as possible

%description -n python3-should_dsl %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n should_dsl-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files should_dsl

%check
# run_all_examples.py references non-existent files and hence fails
%{py3_test_envvars} %{python3} run_examples.py README.rst

%files -n python3-should_dsl -f %{pyproject_files}
%license LICENSE
%doc CONTRIBUTORS README.rst

%changelog
%autochangelog
