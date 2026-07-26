%global source0_hash adcfe623c02a595c107c314072f67a2278fe4eb40b72c0d1a2c903cc78af3439

%global srcname click-threading
%global pyname click_threading
%global sum Multithreaded support for python click apps

Name:           python-%{srcname}
Version:        0.5.0
Release:        18%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/click-contrib/%{srcname}
Source0:        https://files.pythonhosted.org/packages/df/ea/0b20b8e09a6ba1df6defc29479c462437a8e8a3b6f4203fcad8b0a5e3fa3/click-threading-0.5.0.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-click >= 0.5

%description
Multithreaded support for python click (CLI creation kit) applications.

%package -n     python3-%{srcname}
Summary:        %{sum}
Requires:       python3-click >= 0.5

%description -n python3-%{srcname}
Multithreaded support for python 3 click (CLI creation kit) applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pyname}

%check
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
