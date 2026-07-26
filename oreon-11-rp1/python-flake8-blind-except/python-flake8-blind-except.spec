%global source0_hash d418273d9595f18d25ef8bd43af27f78aa5a29753207990854bf3ecb198cd955

%global srcname flake8-blind-except

Name:           python-%{srcname}
Version:        0.2.1
Release:        9%{?dist}
Summary:        A flake8 extension that checks for catch-all except statements

License:        MIT
URL:            https://github.com/elijahandrews/flake8-blind-except
Source0:        https://github.com/elijahandrews/flake8-blind-except/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
A flake8 extension that checks for blind, catch-all "except:" and
"except Exception:" statements.

As of pycodestyle 2.1.0, "E722 do not use bare except, specify exception
instead" is built-in. However, bare Exception and BaseException are still
allowed. This extension flags them as B902.

Using except without explicitly specifying which exceptions to catch is
generally considered bad practice, since it catches system signals like
SIGINT. You probably want to handle system interrupts differently than
exceptions occurring in your code.}

%description %_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  %{py3_dist pycodestyle}
BuildRequires:  %{py3_dist pytest}
Requires:       %{py3_dist flake8}
Requires:       %{py3_dist pycodestyle}

%description -n python%{python3_pkgversion}-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l flake8_blind_except

%check
%pytest --doctest-modules flake8_blind_except.py

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
