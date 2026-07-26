%global source0_hash d73b895324e35aad37728e3c0a6e660b8187ff64390dc946b92828393dadb833

%global         srcname         pyrdfa3
%global         forgeurl        https://github.com/prrvchr/pyrdfa3
Version:        3.6.5
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        RDFa 1.1 distiller/parser library

License:        W3C
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/%{tag}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel

BuildArch: noarch

%global _description %{expand:
pyRdfa distiller/parser library.
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
# Remove pre-generated files
rm -r doc
rm -r src/pyrdfa3.egg-info

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyRdfa -l

%check
# No tests associated with distribution
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
