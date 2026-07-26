%global source0_hash 8697b192bc4e9f2d75de4bdd1071d466d85e81092f1527b253fa893266fcc3fb

%global srcname colorlog
%global desc "colorlog.ColoredFormatter is a formatter for use with Python's logging module that outputs records using terminal colors."

Name:           python-%{srcname}
Version:        6.10.1
Release:        %autorelease
Summary:        Colored formatter for the Python logging module

License:        MIT
URL:            https://github.com/borntyping/python-colorlog
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%generate_buildrequires
%pyproject_buildrequires

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{pytest} -v

%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.dist-info/

%changelog
%autochangelog
