%global source0_hash 55ffe3329e48f54f8a75aa36ece08f365e09d61f8a209773ef09a1d4760e699a

%global pypi_name dj-email-url
%global pkg_name django-email-url

Name:           python-%{pkg_name}
Version:        1.0.6
Release:        %autorelease
Summary:        Use an URL to configure email backend settings in your Django Application

# From README.rst
# - All original source code is licensed under BSD-2-Clause.
# - All documentation is licensed under CC-BY-4.0.
# - Some configuration and data files are licensed under CC0-1.0.
License:        BSD-2-Clause AND CC-BY-4.0 AND CC0-1.0
URL:            https://github.com/migonzalvar/dj-email-url
Source:         %{pypi_source}

BuildArch:      noarch

%description
This utility allows to utilize the 12factor inspired environments variable to
configure the email backend in a Django application.

%package -n     python3-%{pkg_name}
Summary:        %{summary}

BuildRequires:  python3-devel

%description -n python3-%{pkg_name}
This utility allows to utilize the 12factor inspired environments variable to
configure the email backend in a Django application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L dj_email_url

%check
%pyproject_check_import

%files -n python3-%{pkg_name} -f %{pyproject_files}
%license LICENSES/*
%doc README.rst

%changelog
%autochangelog
