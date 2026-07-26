%global source0_hash f09edd5e2a40e4d66f918f083a792cc9cc4bed5d820b037fd42db9ad67793e90

%global srcname simpleeval

Name:           python-%{srcname}
Version:        1.0.3
Release:        7%{?dist}
Summary:        An expression evaluator library for Python

License:        MIT
URL:            https://github.com/danthedeckie/simpleeval
Source0:        %{url}/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
An short, easy to use, safe and reasonably extensible expression evaluator.
Designed for things like in a website where you want to allow the user to
generate a string, or a number from some other input, without allowing full
eval() or other unsafe or needlessly complex linguistics.

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
An short, easy to use, safe and reasonably extensible expression evaluator.
Designed for things like in a website where you want to allow the user to
generate a string, or a number from some other input, without allowing full
eval() or other unsafe or needlessly complex linguistics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{__python3} test_simpleeval.py

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENCE
%doc README.rst

%changelog
%autochangelog
